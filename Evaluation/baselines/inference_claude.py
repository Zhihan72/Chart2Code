import os
import json
import jsonlines
import base64
import shortuuid
from tqdm import tqdm
import anthropic
os.environ["ANTHROPIC_API_KEY"] = "your_anthropic_key"
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def encode_base_image(file):
    with open(file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def call_model(msg, image_pt, model):
    if '.jpg' in image_pt:
        type_ = 'image/jpeg'
    elif '.png' in image_pt:
        type_ = 'image/png'
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": msg,
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": type_,
                            "data": encode_base_image(image_pt),
                        },
                    }
                ],
            }
        ]
    completion = client.messages.create(
        model=model,
        messages=messages,
        max_tokens=2048,
    )
    reply = completion.content[0].text
    num_token = str(completion.usage.output_tokens) + ';' + str(completion.usage.input_tokens)
    return reply, num_token

dataset = 'reachqa' # reachqa, chartmimic
model = 'claude-3-opus-20240229'
question_file = f'./Evaluation/dataset/{dataset}/chart2code_direct_mimic.json'
image_folder = f'./Evaluation/dataset/{dataset}/images/ori'
answers_file = f'./baseline/results/{dataset}/chart2code_{model}_DirectAgent_results.json'

questions = json.load(open(os.path.expanduser(question_file), "r"))
answers_file = os.path.expanduser(answers_file)
os.makedirs(os.path.dirname(answers_file), exist_ok=True)
ans_file = open(answers_file, "w")
for i, line in enumerate(tqdm(questions)):
    id_ = line["id"]
    question = line['conversations'][0]['value'].replace('<image>', '').strip()
    image_file = os.path.join(image_folder, line["image"])
    outputs, num_token = call_model(question, image_file, model)

    ans_file.write(json.dumps({"file": os.path.join(image_folder, line["image"].replace('.png','.pdf').replace('.jpg','.pdf')),
                                "response": outputs,
                                "num_token": num_token,
                                }) + "\n")
    ans_file.flush()
ans_file.close()