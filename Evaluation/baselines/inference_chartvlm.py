import sys
sys.path.append('./baseline/ChartVLM')
from tools.ChartVLM import infer_ChartVLM

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
import math

def split_list(lst, n):
    """Split a list into n (roughly) equal-sized chunks"""
    chunk_size = math.ceil(len(lst) / n)  # integer division
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

def get_chunk(lst, n, k):
    chunks = split_list(lst, n)
    return chunks[k]

def eval_model(args):
    questions = json.load(open(os.path.expanduser(args.question_file), "r"))
    questions = get_chunk(questions, args.num_chunks, args.chunk_idx)
    answers_file = os.path.expanduser(args.answers_file)
    os.makedirs(os.path.dirname(answers_file), exist_ok=True)
    ans_file = open(answers_file, "w")
    for i, line in enumerate(tqdm(questions)):
        idx = line["id"]
        question = 'Redraw the chart image using Python code.'
        image_file = os.path.join(args.image_folder, line["image"])
        outputs = infer_ChartVLM(image_file, question, args.model_path)
        ans_file.write(json.dumps({"file": os.path.join(args.image_folder, line["image"].replace('.png','.pdf').replace('.jpg','.pdf')),
                                   "response": outputs,
                                   }) + "\n")
        ans_file.flush()
    ans_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-path", type=str, default="./baseline/ChartVLM/ckpt/ChartVLM-large")
    parser.add_argument("--image-folder", type=str, default="")
    parser.add_argument("--question-file", type=str, default="tables/question.json")
    parser.add_argument("--answers-file", type=str, default="answer.jsonl")
    parser.add_argument("--num-chunks", type=int, default=1)
    parser.add_argument("--chunk-idx", type=int, default=0)
    args = parser.parse_args()

    eval_model(args)
