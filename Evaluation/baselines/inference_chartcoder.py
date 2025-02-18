import sys
sys.path.append('./baseline/ChartCoder')

from llava.model import *
from llava.model.builder import load_pretrained_model
from llava.mm_utils import tokenizer_image_token, process_images, get_model_name_from_path
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from llava.conversation import conv_templates, SeparatorStyle

import os
import torch
from PIL import Image
import argparse
import requests
from transformers import AutoProcessor, LlavaForConditionalGeneration
import base64
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
    tokenizer, model, image_processor, max_length = load_pretrained_model(args.model_path, None, 'llava_deepseekcoder', device_map='auto')
    model.eval()
    # processor = AutoProcessor.from_pretrained(args.model_path)
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
        
        prompt = f"### Instruction:\n{DEFAULT_IMAGE_TOKEN}\n{question}\n### Response:\n"
        input_ids = tokenizer_image_token(prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).cuda()
        image_tensor = process_images([image], image_processor, model.config)[0]
        with torch.inference_mode():
            output_ids = model.generate(
                input_ids,
                images=image_tensor.unsqueeze(0).half().cuda(),
                image_sizes=[image.size],
                do_sample=True,
                temperature=0.1,
                top_p=0.95,
                max_new_tokens=2048,
                use_cache=True)
        outputs = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0].strip()

        ans_file.write(json.dumps({"file": os.path.join(args.image_folder, line["image"].replace('.png','.pdf').replace('.jpg','.pdf')),
                                   "response": outputs,
                                   }) + "\n")
        ans_file.flush()
    ans_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="./baseline/ChartCoder/ckpt")
    parser.add_argument("--image-folder", type=str, default="")
    parser.add_argument("--question-file", type=str, default="tables/question.json")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    parser.add_argument("--num-chunks", type=int, default=1)
    parser.add_argument("--chunk-idx", type=int, default=0)
    args = parser.parse_args()

    eval_model(args)