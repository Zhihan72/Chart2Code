#!/bin/bash
SAVE_PATH=./Evaluation/results
PROJECT_PATH=./Evaluation/eval_metrcis
OPENAI_API_KEY=your_api_key
cd ${PROJECT_PATH}
export PROJECT_PATH=${PROJECT_PATH}
export SAVE_PATH=${SAVE_PATH}
export OPENAI_API_KEY=${OPENAI_API_KEY}

DATASET=reachqa # reachqa, chartmimic
export DATASET_NM=${DATASET}

models=(
    llava-v1.6-mistral-7b
)

for model in "${models[@]}"; do
    echo "$model"

    # Step 1: Run the Code in the Response
    python ./chart2code/utils/post_process/code_checker.py \
    --input_file ${SAVE_PATH}/${DATASET}/chart2code_${model}_DirectAgent_results.json \
    --template_type direct

    python ./chart2code/utils/post_process/code_interpreter.py \
    --input_file ${SAVE_PATH}/${DATASET}/chart2code_${model}_DirectAgent_results.json \
    --template_type direct

    # Step 2: Get Lowlevel Score
    python ./chart2code/main.py \
    --cfg_path ./eval_configs/code4evaluation_direct.yaml \
    --tasks code4evaluation \
    --model "${model}" \

    # Step 3: Get Highlevel Score
    python ./chart2code/main.py \
    --cfg_path ./eval_configs/gpt4generation_direct_batch.yaml \
    --tasks gpt4evaluation_batch \
    --model gpt-4o \
    --evaluation_dir ${SAVE_PATH}/${DATASET}/chart2code_${model}_DirectAgent_results/direct
done