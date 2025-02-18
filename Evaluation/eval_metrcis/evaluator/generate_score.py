import os
import json
import jsonlines
from tqdm import tqdm
from PIL import Image 
import requests 
import argparse

import torch
from accelerate import Accelerator
from accelerate.utils import gather_object
from datasets import load_dataset
from peft import LoraConfig
from transformers import (
    AutoModelForCausalLM,
    AutoProcessor,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
)
from peft import PeftModel
import base64
import copy


with open('./code_generator/instruction/prompt_pointwise_scoring.txt', 'r') as fp:
    prompt_pointwise_scoring = fp.read()

def patch_clip_for_lora(model):
    # remove unused parameters and then monkey patch
    def get_img_features(self, img_embeds):
        clip_vision_model = self.img_processor.vision_model
        hidden_states = clip_vision_model.embeddings(img_embeds)
        hidden_states = clip_vision_model.pre_layrnorm(hidden_states)
        patch_feature = clip_vision_model.encoder(
            inputs_embeds=hidden_states, output_hidden_states=True
        ).hidden_states[-1][:, 1:]
        return patch_feature

    image_embedder = model.model.vision_embed_tokens
    layer_index = image_embedder.layer_idx
    clip_layers = image_embedder.img_processor.vision_model.encoder.layers
    if layer_index < 0:
        layer_index = len(clip_layers) + layer_index
    del clip_layers[layer_index + 1 :]
    del image_embedder.img_processor.vision_model.post_layernorm
    image_embedder.get_img_features = get_img_features.__get__(image_embedder)

def load_phi_model(model_id, lora_path):
    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        device_map="cuda", 
        trust_remote_code=True, 
        torch_dtype="auto", 
        _attn_implementation='flash_attention_2'    
    )
    if len(lora_path)!=0:
        print(f"Loading lora: {lora_path} ...\n\n")
        patch_clip_for_lora(model)
        model.load_adapter(lora_path)

    # for best performance, use num_crops=4 for multi-frame, num_crops=16 for single-frame.
    processor = AutoProcessor.from_pretrained(model_id, 
        trust_remote_code=True, 
        num_crops=16, # 4
    )
    return model, processor

def generate_response(id_, image_path_list, model, processor):
    message = prompt_pointwise_scoring+'\n\nThis is the reference image\n<|image_1|>\n\nThis is the AI-generated image\n<|image_2|>'
    try:
        images = [Image.open(x) for x in image_path_list]
    except Exception as e:
        return f'Error raised. {e}'
    messages = [{"role": "user", "content": message},]
    prompt = processor.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = processor(prompt, images, return_tensors="pt").to('cuda')

    generate_ids = model.generate(**inputs, eos_token_id=processor.tokenizer.eos_token_id, do_sample=False, temperature=0.0, max_new_tokens=512)
    generate_ids = generate_ids[:, inputs['input_ids'].shape[1]:] # remove input tokens 
    response = processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return response

def get_gpt_conversation(id_, image_path_list,):
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt_pointwise_scoring},
                {"type": "text", "text": "This is the reference image"},
                {"type": "image", "image_url": image_path_list[0]},
                {"type": "text", "text": "This is the AI-generated image"},
                {"type": "image", "image_url": image_path_list[1]},
            ],
        }
    ]
    def encode_base_image(file):
        with open(file, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    converted_conversation = []
    for message in conversation:
        converted_message = {}
        converted_message["role"] = message["role"]
        converted_message["content"] = []
        for content in message["content"]:
            if content["type"] == "text":
                converted_message["content"].append(
                    {"type": "text", "text": content["text"]}
                )
            elif content["type"] == "image":
                base64_image = encode_base_image(content["image_url"])
                converted_message["content"].append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    }
                )
            else:
                raise NotImplementedError
        converted_conversation.append(converted_message)
    return converted_conversation

def get_gpt_batch_format(messages, custom_id, model_engine,):
    dict_ = {
        "custom_id": custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": model_engine,
            "messages": messages,
            "max_tokens": 2048,
            }
        }
    return dict_

def get_pointwise_score(evaluator, response):
    line_list = response.lower().split('. **')
    dim_dict = {'type': 0, 'layout': 0, 'text': 0, 'data': 0, 'style': 0, 'color': 0,} #  'final': 0
    for k in range(len(line_list)):
        head_ = line_list[k].split('**')[0]
        for key_ in dim_dict.keys():
            if key_ in head_:
                if evaluator=='Phi':
                    subscore = line_list[k].split('subscore')[-1].split('\n')[0].replace('*','').replace(':','').replace('.','').strip()
                elif evaluator=='gpt':
                    subscore = line_list[k].split('**')[0].split(' (')[-1].split(')')[0].split('/')[0].split()[0].strip()
                try:
                    if float(subscore) in [0.0, 1.0]:
                        dim_dict[key_] = int(subscore)
                    elif float(subscore) in [0.5, 5.0]: # For debug
                        dim_dict[key_] = 0
                    else:
                        dim_dict[key_] = 0
                except:
                    dim_dict[key_] = -1
    sum_list = []
    for x in dim_dict.keys():
        sum_list.append(dim_dict[x])
    if -1 in sum_list:
        dim_dict.update({'final': -1})
    else:
        dim_dict.update({'final': sum(sum_list)})
    return dim_dict

############ Scoring ############

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument( '--base-model', type=str, default='Phi-3.5-vision-instruct', help='model path or gpt model engine',)
    parser.add_argument( '--lora-path', type=str, default='', help='',)
    parser.add_argument( '--dataset', type=str, default=1, help='',)
    parser.add_argument( '--model-name', type=str, default='', help='',)
    args = parser.parse_args()

    if 'Phi' in args.base_model:
        output_file = f'./Evaluation/results/{args.dataset}/chart2code_{args.model_name}_DirectAgent_results_phi4evaluation.jsonl'
        model, processor = load_phi_model(args.base_model, args.lora_path)
    elif 'gpt' in args.base_model:
        output_file = f'./self_instruction/dataset/s{args.stage_name}_examples/scoring/upload_{args.model_name}_by_gpt.jsonl'

    gold_py_dir = f'./Evaluation/dataset/{args.dataset}/images/ori'
    resp_py_dir = f'./Evaluation/results/{args.dataset}/chart2code_{args.model_name}_DirectAgent_results/direct'
    print(f"Saving file: {output_file} ...\n\n")

    id_list = [x.replace('.py','') for x in os.listdir(gold_py_dir) if 'py' in x]
    for id_ in tqdm(id_list):
        image_path_list = [f'{gold_py_dir}/{id_}.png', f'{resp_py_dir}/{id_}.png']
        
        if 'Phi' in args.base_model:
            response = generate_response(id_, image_path_list, model, processor)
            dim_dict = get_pointwise_score('Phi', response)
            save_dict = {'question_id': id_, 'response': response, 'dim_dict': copy.deepcopy(dim_dict)}
        elif 'gpt' in args.base_model:
            conv_ = get_gpt_conversation(id_, image_path_list,)
            save_dict =  get_gpt_batch_format(conv_, f'{id_}_0124', args.base_model)

        with jsonlines.open(output_file, mode='a') as writer:
            writer.write(save_dict)