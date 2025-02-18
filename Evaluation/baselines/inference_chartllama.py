from PIL import Image
import requests
from transformers import AutoProcessor, LlavaForConditionalGeneration
import torch
import base64
import argparse
import torch
import os
import json
from tqdm import tqdm
import shortuuid
import math

def encode_base_image(file):
    with open(file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def split_list(lst, n):
    """Split a list into n (roughly) equal-sized chunks"""
    chunk_size = math.ceil(len(lst) / n)  # integer division
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def get_chunk(lst, n, k):
    chunks = split_list(lst, n)
    return chunks[k]

def eval_model(args):
    model = LlavaForConditionalGeneration.from_pretrained(args.model_path, torch_dtype=torch.float16)
    model.load_adapter(args.lora_path)
    processor = AutoProcessor.from_pretrained(args.model_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    questions = json.load(open(os.path.expanduser(args.question_file), "r"))
    questions = get_chunk(questions, args.num_chunks, args.chunk_idx)
    answers_file = os.path.expanduser(args.answers_file)
    os.makedirs(os.path.dirname(answers_file), exist_ok=True)
    ans_file = open(answers_file, "w")
    for i, line in enumerate(tqdm(questions)):
        idx = line["id"]
        question = '<image>\n Question: ' + line['conversations'][0]['value'].replace('<image>', '').strip() + ' Answer: '
        image_file = os.path.join(args.image_folder, line["image"])
        image = Image.open(image_file).convert("RGB")
        inputs = processor(text=question, images=image, return_tensors="pt")
        inputs = {k: v.to(device) for k, v in inputs.items()}
        inputs['pixel_values'] = inputs['pixel_values'].to(torch.float16)
        prompt_length = inputs['input_ids'].shape[1]
        generate_ids = model.generate(**inputs, num_beams=4, max_new_tokens=2048)
        outputs = processor.batch_decode(generate_ids[:, prompt_length:], skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

        ans_file.write(json.dumps({"file": os.path.join(args.image_folder, line["image"].replace('.png','.pdf').replace('.jpg','.pdf')),
                                   "response": outputs,
                                   }) + "\n")
        ans_file.flush()
    ans_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="./baseline/llava-v1.5-7b-hf")
    parser.add_argument("--lora-path", type=str, default="./baseline/ChartLlama_LoRA")
    parser.add_argument("--image-folder", type=str, default="")
    parser.add_argument("--question-file", type=str, default="tables/question.json")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    parser.add_argument("--num-chunks", type=int, default=1)
    parser.add_argument("--chunk-idx", type=int, default=0)
    args = parser.parse_args()

    eval_model(args)