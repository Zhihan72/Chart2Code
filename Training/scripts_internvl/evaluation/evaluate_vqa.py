import sys
sys.path.append('./Training/InternVL')

import argparse
import itertools
import json
import os
import random
import subprocess
import time
from functools import partial
from typing import Optional

import torch
from internvl.model import load_model_and_tokenizer
from internvl.train.dataset import build_transform, dynamic_preprocess
from internvl.model.internvl_chat import InternVLChatConfig, InternVLChatModel
from transformers import AutoTokenizer
from PIL import Image
import math
from tqdm import tqdm

def split_model(num_layers, vit_alpha=0.5):
    device_map = {}
    world_size = torch.cuda.device_count()
    # Since the first GPU will be used for ViT, treat it as half a GPU.
    num_layers_per_gpu = math.ceil(num_layers / (world_size - vit_alpha))
    num_layers_per_gpu = [num_layers_per_gpu] * world_size
    num_layers_per_gpu[0] = math.ceil(num_layers_per_gpu[0] * (1 - vit_alpha))
    layer_cnt = 0
    for i, num_layer in enumerate(num_layers_per_gpu):
        for j in range(num_layer):
            device_map[f'language_model.model.layers.{layer_cnt}'] = i
            layer_cnt += 1
    device_map['vision_model'] = 0
    device_map['mlp1'] = 0
    device_map['language_model.model.tok_embeddings'] = 0
    device_map['language_model.model.embed_tokens'] = 0
    device_map['language_model.output'] = 0
    device_map['language_model.model.norm'] = 0
    device_map['language_model.lm_head'] = 0
    device_map[f'language_model.model.layers.{num_layers - 1}'] = 0
    device_map['language_model.model.rotary_emb'] = 0

    return device_map

def split_list(lst, n):
    """Split a list into n (roughly) equal-sized chunks"""
    chunk_size = math.ceil(len(lst) / n)  # integer division
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def get_chunk(lst, n, k):
    chunks = split_list(lst, n)
    return chunks[k]

def eval_model(args):
    # model, tokenizer = load_model_and_tokenizer(args)
    if args.auto:
        config = InternVLChatConfig.from_pretrained(args.checkpoint)
        num_hidden_layers = config.llm_config.num_hidden_layers
        device_map = split_model(num_hidden_layers)
        # device_map = 'cuda'
    kwargs = {'device_map': device_map} if args.auto else {}
    tokenizer = AutoTokenizer.from_pretrained(args.checkpoint, trust_remote_code=True, use_fast=False)
    model = InternVLChatModel.from_pretrained(
        args.checkpoint, low_cpu_mem_usage=True, torch_dtype=torch.bfloat16,
        load_in_8bit=args.load_in_8bit, load_in_4bit=args.load_in_4bit, **kwargs).eval()
    if not args.load_in_8bit and not args.load_in_4bit and not args.auto:
        model = model.cuda()
    
    image_size = model.config.force_image_size or model.config.vision_config.image_size
    use_thumbnail = model.config.use_thumbnail
    transform = build_transform(is_train=False, input_size=image_size)

    total_params = sum(p.numel() for p in model.parameters()) / 1e9
    if total_params > 20 or args.dynamic:
        args.num_beams = 1
        print(f'[test] total_params: {total_params}B, use num_beams: {args.num_beams}')
    else:
        print(f'[test] total_params: {total_params}B')
    print(f'[test] image_size: {image_size}')
    print(f'[test] template: {model.config.template}')
    print(f'[test] dynamic_image_size: {args.dynamic}')
    print(f'[test] use_thumbnail: {use_thumbnail}')

    questions = json.load(open(os.path.expanduser(args.question_file), "r"))
    questions = get_chunk(questions, args.num_chunks, args.chunk_idx)
    answers_file = os.path.expanduser(args.answers_file)
    os.makedirs(os.path.dirname(answers_file), exist_ok=True)
    ans_file = open(answers_file, "w")
    for i, line in enumerate(tqdm(questions)):
        image_file = line["image"]
        question = line['conversations'][0]['value'].replace('<image>', '').strip()
        question_id = line["id"]

        image = Image.open(os.path.join(args.image_folder, image_file)).convert('RGB')

        if args.dynamic:
            images = dynamic_preprocess(image, image_size=image_size,
                                        use_thumbnail=use_thumbnail,
                                        max_num=6)
        else:
            images = [image]
        
        pixel_values = [transform(image) for image in images]
        pixel_values = torch.stack(pixel_values).to(torch.bfloat16).cuda()
 
        generation_config = dict(
            num_beams=args.num_beams,
            max_new_tokens=2048, # 512
            min_new_tokens=1,
            do_sample=True if args.temperature > 0 else False,
            temperature=args.temperature,
        )
        pred = model.chat(
            tokenizer=tokenizer,
            pixel_values=pixel_values,
            question=question,
            generation_config=generation_config,
            verbose=True
        )
        ans_file.write(json.dumps({"file": os.path.join(args.image_folder, line["image"].replace('.png','.pdf').replace('.jpg','.pdf')),
                                   "response": pred,
                                   }) + "\n")
        ans_file.flush()
    ans_file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="facebook/opt-350m")
    parser.add_argument("--image-folder", type=str, default="")
    parser.add_argument("--question-file", type=str, default="tables/question.json")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    parser.add_argument("--num-chunks", type=int, default=1)
    parser.add_argument('--batch-size', type=int, default=1)
    parser.add_argument('--num-workers', type=int, default=1)
    parser.add_argument("--chunk-idx", type=int, default=0)
    parser.add_argument('--num-beams', type=int, default=1)
    parser.add_argument('--temperature', type=float, default=0.0)
    parser.add_argument('--out-dir', type=str, default='results')
    parser.add_argument('--few-shot', type=int, default=0)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--dynamic', action='store_true')
    parser.add_argument('--max-num', type=int, default=6)
    parser.add_argument('--load-in-8bit', action='store_true')
    parser.add_argument('--load-in-4bit', action='store_true')
    parser.add_argument('--auto', action='store_true')
    args = parser.parse_args()

    args.checkpoint = args.model_path

    print('datasets:', args.question_file)
    assert args.batch_size == 1, 'Only batch size 1 is supported'
    eval_model(args)