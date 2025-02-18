import os
import json
import argparse

def get_score_from_response(response):
    extract_ans = response.split('extract_answer')[-1].split('score')[0].replace(':','').replace(',','').replace('}','').replace('```','').replace('\"', '').strip()
    score = response.split('score')[-1].replace(':','').replace(',','').replace('}','').replace('```','').replace('\"', '').strip()
    try:
        return extract_ans, int(score)
    except Exception as e:
        print(e)
        return extract_ans, 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # input/output
    parser.add_argument('--input_file', type=str, required=True)
    args = parser.parse_args()

    output_file = args.input_file.replace('_upload_completed.jsonl', '_gpt4evaluation.json')

    with open(args.input_file, 'r') as fp:
        batch_resp_dict = json.loads(fp.read())
    
    descrip_scores = []
    reasoning_scores = []
    result_dict = {}
    for key in batch_resp_dict.keys():
        label = key.split('_')[-1].strip()
        response = batch_resp_dict[key]["response"]["body"]["choices"][0]["message"]["content"]
        ans, binary_score = get_score_from_response(response)
        result_dict[label] = {
            'response': response,
            'extract_answer': ans,
            'score': binary_score,
        }
        if 'descriptive' in label:
            descrip_scores.append(binary_score)
        elif 'reasoning' in label:
            reasoning_scores.append(binary_score)
    with open(output_file, 'w') as fp:
        json.dump(result_dict, fp, indent=4)
    
    print(output_file)
    print('Descriptive: {}, {}'.format(len(descrip_scores), sum(descrip_scores)/len(descrip_scores)))
    print('Reasoning: {}, {}'.format(len(reasoning_scores), sum(reasoning_scores)/len(reasoning_scores)))