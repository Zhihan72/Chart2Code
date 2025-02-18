import os
import json
import jsonlines
import base64
import shortuuid
from tqdm import tqdm
import google.generativeai as genai
# from google import genai
import PIL

os.environ["GEMINI_API_KEY"] = "your_gemini_key"
genai.configure(api_key=os.environ["GEMINI_API_KEY"], transport='rest')
client = genai.GenerativeModel(model_name='gemini-1.5-pro')

def encode_base_image(file):
    with open(file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def call_model(msg, image_pt, model):
    completion = client.generate_content(
        [
            {
                "mime_type": "image/jpeg",
                "data": encode_base_image(image_pt),
            },
            msg,
        ],
    )
    reply = completion.text
    return reply

dataset = 'reachqa' # reachqa, chartmimic
model = 'gemini-1.5-pro'
question_file = f'./Evaluation/dataset/{dataset}/chart2code_direct_mimic.json'
image_folder = f'./Evaluation/dataset/{dataset}/images/ori'
answers_file = f'./baseline/results/{dataset}/chart2code_{model}_DirectAgent_results.json'

questions = json.load(open(os.path.expanduser(question_file), "r"))
answers_file = os.path.expanduser(answers_file)
os.makedirs(os.path.dirname(answers_file), exist_ok=True)
ans_file = open(answers_file, "w")
flag = 0
for i, line in enumerate(tqdm(questions)):
    id_ = line["id"]
    question = line['conversations'][0]['value'].replace('<image>', '').strip()
    image_file = os.path.join(image_folder, line["image"])
    outputs = call_model(question, image_file, model)

    ans_file.write(json.dumps({"file": os.path.join(image_folder, line["image"].replace('.png','.pdf').replace('.jpg','.pdf')),
                                "response": outputs,
                                "num_token": 0,
                                }) + "\n")
    ans_file.flush()
ans_file.close()