import os
import random
import json
import jsonlines
import shutil
import itertools
from tqdm import tqdm
from openai import OpenAI
import argparse

def get_preference_example(id, im_pt, instr, chosen_resp, rejected_resp):
    dict_ = {
      "id": str(id),
      "image": im_pt,
      "conversations": [
            {
                "from": "human", 
                'value': f'<image>\n{instr}',
            }, 
            {
                "from": "gpt",
                'value': chosen_resp,
            },
        ],
        "rejected_conversations": [
            {
                "from": "human",
                'value': f'<image>\n{instr}',
            }, 
            {
                "from": "gpt",
                'value': rejected_resp,
            },   
        ],
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

def compare_two_scores(score_a, score_b):
    if score_a==-1 or score_b==-1:
        score_from_pointwise = ''
    elif score_a > score_b:
        score_from_pointwise = 'A'
    elif score_a < score_b:
        score_from_pointwise = 'B'
    else:
        score_from_pointwise = 'tie'
    return score_from_pointwise

with open('./code_generation/instruction/prompt_chart2code_task.txt', 'r') as fp:
    prompt_chart2code_task = fp.read()

def main(args):
    scoring_file = f'./self_instruction/dataset/s{args.stage_name}_examples/scoring/{args.model_name}_by_{args.evaluator}.jsonl'
    gold_py_dir = f'./code_generator/dataset/examples/s{args.stage_name}_new_examples'
    variant_py_dir = f'./code_generator/dataset/variants/s{args.stage_name}_variants'
    resp_py_dir = f'./self_instruction/dataset/s{args.stage_name}_examples/sampling/{args.model_name}'

    metadata_save_file = scoring_file.replace('scoring/', 'scoring/metadata_').replace('.jsonl', '.json')
    log_save_path = scoring_file.replace('scoring/', 'scoring/metadata_').replace('.jsonl', '.log')
    prference_save_file = scoring_file.replace('scoring/', 'preference/').replace('.jsonl', '.json')

    dim_list = ['type', 'layout', 'text', 'data', 'style', 'color',]
    with open(f'{variant_py_dir}/metadata/metadata_wExplanation.json', "r") as fp:
        metadata_dict = json.load(fp)

    if args.evaluator=='Phi':
        with open(scoring_file, 'r') as fp:
            resp_list = fp.read().strip().split('\n')
    elif args.evaluator=='gpt':
        scoring_file = scoring_file.replace('scoring/', 'scoring/upload_').replace('.jsonl', '_completed.jsonl')
        with open(scoring_file, "r") as fp:
            scoring_dict = json.load(fp)
        resp_list = list(scoring_dict.keys())

    for resp_ in resp_list:
        if len(resp_)==0:
            continue
        if args.evaluator=='Phi':
            resp_dict = json.loads(resp_)
            label_ = resp_dict['question_id']
            response = resp_dict['response']
        elif args.evaluator=='gpt':
            label_ = resp_.split('_')[0]
            response = scoring_dict[resp_]['response']['body']['choices'][0]['message']['content']
        eval_dict = get_pointwise_score(args.evaluator, response)

        id_ = label_.split('_')[0]
        metadata_dict[id_]['model'] = {}
        metadata_dict[id_]['model']['score'] = eval_dict

    agree_pair_bool = []
    tie_pair_bool = []
    resp_image_scores = []
    preference_pair_list = []
    for id_ in metadata_dict.keys():
        if 'model' not in metadata_dict[id_].keys():
            print(id_)
            continue
        resp_image_scores.append(metadata_dict[id_]['model']['score']['final'])
        for n_path in range(1,3):
            num_stage = [k+1 for k in range(len(metadata_dict[id_][f'path_{n_path}']))]
            num_stage.append('resp')
            random.shuffle(num_stage)
            comb_stage = list(itertools.combinations(num_stage, 2))
            metadata_dict[id_][f'path_{n_path}']['pair'] = []
            for (n_s1, n_s2) in comb_stage:

                label_ = id_
                if n_s1=='resp':
                    img_score_s1 = metadata_dict[id_]['model']['score']['final']
                    label_ += '_resp'
                    with open(f"{resp_py_dir}/{id_}.py", 'r') as fp:
                        code_s1 = fp.read()
                else:
                    img_score_s1 = metadata_dict[id_][f'path_{n_path}'][f'stage_{n_s1}']['score']['gold']['final']
                    label_ += f'_p{n_path}s{n_s1}'
                    with open(f"{variant_py_dir}/{id_}_path_{n_path}_stage_{n_s1}.py", 'r') as fp:
                        code_s1 = fp.read()
                
                if n_s2=='resp':
                    img_score_s2 = metadata_dict[id_]['model']['score']['final']
                    label_ += '_resp'
                    with open(f"{resp_py_dir}/{id_}.py", 'r') as fp:
                        code_s2 = fp.read()
                else:
                    img_score_s2 = metadata_dict[id_][f'path_{n_path}'][f'stage_{n_s2}']['score']['gold']['final']
                    label_ += f'_p{n_path}s{n_s2}'
                    with open(f"{variant_py_dir}/{id_}_path_{n_path}_stage_{n_s2}.py", 'r') as fp:
                        code_s2 = fp.read()

                img_winner = compare_two_scores(img_score_s1, img_score_s2)

                if img_winner=='':
                    continue
                elif img_winner=='tie':
                    tie_pair_bool.append(1)
                    continue
                else:
                    agree_pair_bool.append(1)
                    winner = img_winner
                
                if winner=='A':
                    chosen_code = code_s1
                    rejected_code = code_s2
                elif winner=='B':
                    chosen_code = code_s2
                    rejected_code = code_s1
                
                # dict_ = get_preference_example(label_, f"{id_}.png", prompt_chart2code_task, f'```python\n{chosen_code}```', f'```python\n{rejected_code}```')
                dict_ = get_preference_example(label_, f"{id_}.jpg", prompt_chart2code_task, f'```python\n{chosen_code}```', f'```python\n{rejected_code}```')
                preference_pair_list.append(dict_)
                metadata_dict[id_][f'path_{n_path}']['pair'].append((n_s1, n_s2, winner))


    with open(log_save_path, 'w') as fp:
        tt_num = len(agree_pair_bool) + len(tie_pair_bool)
        fp.write(f'agree_pair_bool: {len(agree_pair_bool) / tt_num}\n')
        fp.write(f'tie_pair_bool: {len(tie_pair_bool) / tt_num}\n')
        fp.write(f'total_num: {tt_num}\n')

        fp.write(f'total_model_resp_num: {len(resp_image_scores)}\n')
        resp_image_scores = [x for x in resp_image_scores if x!=-1]
        fp.write(f'total_valid_model_resp_num: {len(resp_image_scores)}\n')
        fp.write(f'Avg. score: {sum(resp_image_scores)/len(resp_image_scores)}\n')

    with open(metadata_save_file, "w") as fp:
        json.dump(metadata_dict, fp, indent=4)

    random.shuffle(preference_pair_list)
    with open(prference_save_file, 'w') as fp:
        json.dump(preference_pair_list, fp, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--evaluator", type=str, required=True)
    parser.add_argument("--stage-name", type=str, default=1, help='',)
    parser.add_argument("--model-name", type=str, default='', help='',)
    args = parser.parse_args()

    main(args)