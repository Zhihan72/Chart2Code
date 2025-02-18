import os
import random
import json
import jsonlines
import os
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = "your_api_key"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

json_file_path = './code_generation/gold_code_generation/chart2code_reachqa_train.json'
with open(json_file_path, 'r') as fp:
    reachqa_train = json.load(fp)

################# Find Chart Type to all examples #################

with open('./code_generation/rule_and_dimension/chart_type_dict.json', 'r') as fp:
    chart_type_dict = json.loads(fp.read())

# find the chart type from comments
def find_chart_type(code):
    type_dict = {}
    if 'import networkx' in code:
        # networks -> graph
        type_dict['graph'] = {
            'comment': 'import networkx',
            'mini_type': '',
        }
    elif 'import squarify' in code:
        # squarify -> treemap
        type_dict['treemap'] = {
            'comment': 'import squarify',
            'mini_type': '',
        }
    comments = [x for x in code.split('\n') if len(x)!=0 and x[0]=='#']
    for x in comments:
        # For debug
        if 'grid' in x.lower():
            continue
        for type_ in chart_type_dict.keys():
            if type_ in type_dict.keys():
                for mini_type_ in chart_type_dict[type_].keys():
                    if mini_type_ in x.lower():
                        type_dict[type_]['mini_type'] = mini_type_
            elif type_ in x.lower():
                if type_ not in type_dict.keys():
                    type_dict[type_] = {
                        'comment': '',
                        'mini_type': '',
                    }
                type_dict[type_]['comment'] += '\n' + x
                for mini_type_ in chart_type_dict[type_].keys():
                    if mini_type_ in x.lower():
                        type_dict[type_]['mini_type'] = mini_type_
    for key in type_dict.keys():
        if type_dict[key]['mini_type']=='':
            type_dict[key]['mini_type'] = 'base'
    return type_dict

type_dict = {}
for example_ in reachqa_train:
    id_ = example_["id"]
    code = example_["conversations"][1]["value"]
    type_ = find_chart_type(code)
    for key_ in type_.keys():
        if key_ not in list(type_dict.keys()):
            type_dict[key_] = {}
        if  key_ in list(type_dict.keys()) and type_[key_]['mini_type'] not in list(type_dict[key_].keys()):
            type_dict[key_][type_[key_]['mini_type']] = []
        type_dict[key_][type_[key_]['mini_type']].append(id_)

with open('./code_generation/gold_code_generation/type_dict_reachqa_train.json', 'w') as fp:
    json.dump(type_dict, fp, indent=4)


################# Create few-shot prompts #################

def get_dict_format(prompt, custom_id, model_engine='gpt-4o-2024-05-13'):
    messages = [{"role": "user",  "content": prompt}]
    dict_ = {
        "custom_id": f"{custom_id}",
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": model_engine,
            "messages": messages,
            "max_tokens": 2048,
            }
        }
    return dict_

with open('./code_generation/gold_code_generation/type_dict_reachqa_train.json', 'r') as fp:
    type_dict = json.loads(fp.read())

with open('./code_generation/gold_code_generation/prompt_new_example_generation.txt', 'r') as fp:
    prompt_new_example_generation = fp.read()

total_num = 300
num_few_shot = 3
denominator = sum([len(type_dict[key][minitype]) for key in type_dict for minitype in type_dict[key]])
print(f"Denominator: {denominator}")
save_path = './dataset/example/iteration_3/metadata/few_shots_new_examples.jsonl'
for key in type_dict:
    for minitype in type_dict[key].keys():
        minitype_num = int(len(type_dict[key][minitype]) / denominator * total_num)
        if minitype_num==0:
            minitype_num = 1
        if len(type_dict[key][minitype]) < num_few_shot:
            n_shot = 1
        else:
            n_shot = num_few_shot
        print(f"{key} - {minitype}: {str(minitype_num)}")
        for k in range(minitype_num):
            id_few_shots = random.sample(type_dict[key][minitype], n_shot)
            code_few_shots = [conv_["conversations"][1]["value"] for conv_ in reachqa_train if conv_["id"] in id_few_shots]
            if len(code_few_shots)==num_few_shot:
                prompt_ = prompt_new_example_generation.format(type=key, example_1=code_few_shots[0], example_2=code_few_shots[1], example_3=code_few_shots[2])
            else:
                prompt_ = prompt_new_example_generation.format(type=key, example_1=code_few_shots[0], example_2='', example_3='')
            dict_ = get_dict_format(prompt_, f"{key}-{minitype}-{k}")
            with jsonlines.open(save_path, mode='a') as writer:
                writer.write(dict_)