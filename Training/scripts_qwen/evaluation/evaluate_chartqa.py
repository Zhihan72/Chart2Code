import argparse
import torch
import os
import json
from tqdm import tqdm
import shortuuid
import math
from PIL import Image
from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info


def split_list(lst, n):
    """Split a list into n (roughly) equal-sized chunks"""
    chunk_size = math.ceil(len(lst) / n)  # integer division
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def get_chunk(lst, n, k):
    chunks = split_list(lst, n)
    return chunks[k]

# https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct
def get_message(args, line):
    dict_ = {
        "role": "user",
        "content": [
            {"type": "image", "image": os.path.join(args.image_folder, line["figure_path"]),},
            {"type": "text", "text": line['question'].replace('<image>', '').strip()}
        ],
    }
    return [dict_]

def eval_model(args):
    # Model
    model_path = os.path.expanduser(args.model_path)
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        attn_implementation="flash_attention_2",
        device_map="auto",
    )
    processor = AutoProcessor.from_pretrained(model_path)

    questions = json.load(open(os.path.expanduser(args.question_file), "r"))
    questions = get_chunk(questions, args.num_chunks, args.chunk_idx)
    answers_file = os.path.expanduser(args.answers_file)
    os.makedirs(os.path.dirname(answers_file), exist_ok=True)
    ans_file = open(answers_file, "w")
    for i, line in enumerate(tqdm(questions)):
        idx = line["label"]
        image_file = line["figure_path"]
        messages = get_message(args, line)
        text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        image_inputs, video_inputs = process_vision_info(messages)
        inputs = processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt",
        )
        inputs = inputs.to("cuda")
        generated_ids = model.generate(
            **inputs, 
            do_sample=True if args.temperature > 0 else False,
            temperature=args.temperature,
            max_new_tokens=1024,
            use_cache=True,
        )
        generated_ids_trimmed = [out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)]
        outputs = processor.batch_decode(
            generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )[0]

        ans_id = shortuuid.uuid()
        ans_file.write(json.dumps({
            "label": idx,
            "file": os.path.join(args.image_folder, image_file),
            "response": outputs,
            }) + "\n")
        ans_file.flush()
    ans_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="facebook/opt-350m")
    parser.add_argument("--model-base", type=str, default=None)
    parser.add_argument("--image-folder", type=str, default="")
    parser.add_argument("--question-file", type=str, default="tables/question.json")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    parser.add_argument("--conv-mode", type=str, default="llava_v0")
    parser.add_argument("--num-chunks", type=int, default=1)
    parser.add_argument("--chunk-idx", type=int, default=0)
    parser.add_argument("--temperature", type=float, default=0.2)
    args = parser.parse_args()

    eval_model(args)