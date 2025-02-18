import os
import random
from tqdm import tqdm
import time
import json
import jsonlines
import base64
import itertools
from openai import OpenAI

with open('./code_generation/rule_and_dimension/chart_type_dict.json', 'r') as fp:
    chart_type_dict = json.loads(fp.read())

with open('./code_generation/rule_and_dimension/dim_rule_dict.json', 'r') as fp:
    dim_rule_dict = json.loads(fp.read())

with open('./code_generation/variant_generation/prompt_code_variant_generation.txt', 'r') as fp:
    prompt_code_variant_generation = fp.read()

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

# find the layout from comments
def find_subplot_layout(code):
    for line in code.split('\n'):
        if '.subplots' in line:
            subplot = line.split('subplots')[-1].split('figsize')[0].replace('(', '').replace(')', '').replace('=', '').replace('nrows', '').replace('ncols', '')
            subplot_config = [x.strip() for x in subplot.split(',') if len(x.strip())!=0]
            if len(subplot_config)==2:
                try:
                    return (int(subplot_config[0]), int(subplot_config[1]))
                except:
                    return (1, 1)
            else:
                return (1, 1)
    return (1, 1)

def is_related_type(orig_type_dict):
    available_keys = []
    for key in orig_type_dict.keys():
        mini_type = orig_type_dict[key]['mini_type']
        if len(chart_type_dict[key][mini_type]['related_type'])!=0:
            available_keys.append(key)
    if len(available_keys)==0:
        return '', ''
    else:
        ramdom_key = random.sample(available_keys, 1)[0]
        mini_type = orig_type_dict[ramdom_key]['mini_type']
        random_minitype = random.sample(chart_type_dict[ramdom_key][mini_type]['related_type'], 1)[0]
        return ramdom_key, random_minitype

def get_direction(num_direc, code, remove_direc, orig_type_dict):
    candidate_direc = ['type', 'data', 'layout','color', 'text', 'style']
    subplot_config = find_subplot_layout(code)
    if subplot_config==(1, 1):
        candidate_direc.remove('layout')
    for x in remove_direc:
        if x in candidate_direc:
            candidate_direc.remove(x)
    
    random_key, random_minitype = is_related_type(orig_type_dict)
    if random_key=='':
        candidate_direc.remove('type')
    
    if len(candidate_direc) < num_direc:
        return '', ''

    random_direc = random.sample(candidate_direc, num_direc)
    direct_list = []
    for k in range(num_direc):
        if random_direc[k]=='type':
            type_name = chart_type_dict[random_key][random_minitype]['name']
            direct_ = f"{k+1}. " + dim_rule_dict[random_direc[k]][0].format(type_name=type_name)
            if subplot_config!=(1, 1): # For debug, see 01827
                direct_ += ' (Keep the number and arrangement of subplots unchanged)'
            direct_list.append(direct_)
        else:
            direct_list.append(f"{k+1}. " + random.sample(dim_rule_dict[random_direc[k]], 1)[0])
    return ';'.join(random_direc), '\n'.join(direct_list)

def get_dict_format(sys_msg, prompt, custom_id, model_engine, sys_bool=1):
    if sys_bool==1:
        messages = [{ "role": "system", "content": sys_msg},{"role": "user",  "content": prompt}]
    else:
        messages = [{"role": "user",  "content": prompt}]
    dict_ = {
        "custom_id":custom_id,
        "method": "POST",
        "url": "/v1/chat/completions",
        "body": {
            "model": model_engine,
            "messages": messages,
            "max_tokens": 2048,
            }
        }
    return dict_

def resp_to_code(response):
    if '```python' in response:
        code = response.split('```python')[-1].split('```')[0].strip()
        explanation = response.split('```python')[0] + '\n\n' + response.split('```')[-1]
    elif '```Python' in response:
        code = response.split('```Python')[-1].split('```')[0].strip()
        explanation = response.split('```Python')[0] + '\n\n' + response.split('```')[-1]
    return code, explanation

###################### Sample direction and rules in each path ######################

orig_dir = './dataset/example/iteration_1'
variant_dir = './dataset/variant/iteration_1'
py_files = [x for x in os.listdir(orig_dir) if '_' not in x and '.py' in x]

n_path = 2
n_stage = 5
model_engine = 'gpt-4o'

print(f"Saving Path: {variant_dir}/metadata/metadata.json")
metadata_dict = {}
for py_fl in py_files:
    custom_id = py_fl.split('.py')[0].strip()
    metadata_dict[custom_id] = {}
    with open(f"{orig_dir}/{py_fl}", 'r') as fp:
        code = fp.read()
    metadata_dict[custom_id]['type'] = find_chart_type(code)

    for n_p in range(n_path):
        remove_dim = []
        metadata_dict[custom_id][f'path_{str(n_p+1)}'] = {}
        code_gold_dict = {'type': 1, 'layout': 1, 'text': 1, 'data': 1, 'style': 1, 'color': 1, 'final': 6}
        for n_s in range(n_stage):
            dimension, rule = get_direction(1, code, remove_dim, metadata_dict[custom_id]['type'])
            if dimension=='':
                break
            remove_dim.append(dimension)
            code_gold_dict[dimension] = 0
            code_gold_dict['final'] = code_gold_dict['final'] - 1
            
            metadata_dict[custom_id][f'path_{str(n_p+1)}'][f'stage_{str(n_s+1)}'] = {
                    'dimension': dimension,
                    'rule': rule.replace('1.', '').strip(),
                }
            save_dict = code_gold_dict.copy()
            metadata_dict[custom_id][f'path_{str(n_p+1)}'][f'stage_{str(n_s+1)}']['code_score'] = {'gold': save_dict, 'evaluator': {},}
            metadata_dict[custom_id][f'path_{str(n_p+1)}'][f'stage_{str(n_s+1)}']['image_score'] = {'gold': {}, 'evaluator': {},}

with open(f'{variant_dir}/metadata/metadata.json', "w") as fp:
    json.dump(metadata_dict, fp, indent=4)

###################### Prepare metadata to OpenAI stage by stage ######################

orig_dir = './dataset/example/iteration_1'
variant_dir = './dataset/variant/iteration_1'
py_files = [x for x in os.listdir(orig_dir) if '_' not in x and '.py' in x]

num_stage = 5
save_path = f'{variant_dir}/metadata/stage_{str(num_stage)}_variant.jsonl'

print(f"Processing: {variant_dir}/metadata/metadata.json")
print(f"Gold Code Dir: {orig_dir}\n\n")
with open(f'{variant_dir}/metadata/metadata.json', "r") as fp:
    metadata_dict = json.load(fp)

for py_fl in py_files:
    custom_id = py_fl.split('.py')[0].strip()

    for num_path in range(1, n_path+1):
        if f'stage_{str(num_stage)}' not in list(metadata_dict[custom_id][f'path_{str(num_path)}'].keys()):
            continue
        rule = metadata_dict[custom_id][f'path_{str(num_path)}'][f'stage_{str(num_stage)}']['rule']
        if num_stage==1:
            with open(f"{orig_dir}/{py_fl}", 'r') as fp:
                code = fp.read()
        else:
            with open(f"{variant_dir}/{custom_id}_path_{str(num_path)}_stage_{str(num_stage-1)}.py", 'r') as fp:
                code = fp.read()
        prompt = prompt_code_variant_generation.format(rule=rule, code=code)
        dict_ = get_dict_format('', prompt, f"{custom_id}_path_{str(num_path)}_stage_{str(num_stage)}", model_engine, sys_bool=0)
        with jsonlines.open(save_path, mode='a') as writer:
            writer.write(dict_)

###################### Collect results from OpenAI and update metadata ######################

orig_dir = './dataset/example/iteration_1'
variant_dir = './dataset/variant/iteration_1'
with open(f'{variant_dir}/metadata/metadata_wExplanation.json', "r") as fp: # metadata_wExplanation, metadata
    metadata_dict = json.load(fp)

num_stage = 5
batch_result_file = f'{variant_dir}/metadata/stage_{str(num_stage)}_variant_completed.jsonl'
with open(batch_result_file, "r") as fp:
    batch_result = json.load(fp)
for key in tqdm(batch_result.keys()):
    custom_id = key.split('_')[0]
    n_p = key.split('_')[2]
    n_s = key.split('_')[4]
    response = batch_result[key]['response']['body']['choices'][0]['message']['content']
    try:
        code, explanation = resp_to_code(response)
    except:
        print(custom_id)
        continue
    # save in .py file
    with open(f"{variant_dir}/{custom_id}_path_{n_p}_stage_{n_s}.py", 'w') as fp:
        fp.write(code)
    # update metadata
    metadata_dict[custom_id][f'path_{n_p}'][f'stage_{n_s}']['explanation'] = explanation

with open(f'{variant_dir}/metadata/metadata_wExplanation.json', "w") as fp:
    json.dump(metadata_dict, fp, indent=4)