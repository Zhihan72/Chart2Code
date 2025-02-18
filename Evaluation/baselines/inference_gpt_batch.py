# reachqa for gpt-4o
# chartmimic, reachqa for gpt-4o-mini

import os
import json
import jsonlines
import base64
import shortuuid
from tqdm import tqdm
from openai import OpenAI
os.environ['OPENAI_API_KEY'] = "your_openai_key"
api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key=api_key,)

def get_gpt_conversation(question, image_path,):
    conversation = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": question},
                {"type": "image", "image_url": image_path},
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

def call_chatgpt(messages, model_engine):
    completion = client.chat.completions.create(
        model= model_engine,
        messages=messages,
    )
    return completion.choices[0].message.content

dataset = 'chartmimic' # reachqa, chartmimic
model = 'gpt-4o-mini'
question_file = f'./Evaluation/dataset/{dataset}/chart2code_direct_mimic.json'
image_folder = f'./Evaluation/dataset/{dataset}/images/ori'
answers_file = f'./Baselines/results/{dataset}/upload_chart2code_{model}_DirectAgent_results.jsonl'

questions = json.load(open(os.path.expanduser(question_file), "r"))
answers_file = os.path.expanduser(answers_file)
os.makedirs(os.path.dirname(answers_file), exist_ok=True)
ans_file = open(answers_file, "w")
for i, line in enumerate(tqdm(questions)):
    id_ = line["id"]

    question = line['conversations'][0]['value'].replace('<image>', '').strip()
    image_file = os.path.join(image_folder, line["image"])
    conv_ = get_gpt_conversation(question, image_file,)
    save_dict =  get_gpt_batch_format(conv_, f'{shortuuid.uuid()}_{id_}', model)
    ans_file.write(json.dumps(save_dict) + "\n")
    ans_file.flush()

ans_file.close()