#!/bin/bash
PROJECT_PATH=./Evaluation
cd ${PROJECT_PATH}
export PROJECT_PATH=${PROJECT_PATH}
export NCCL_P2P_DISABLE=1
export TOKENIZERS_PARALLELISM="false"
export CUDA_VISIBLE_DEVICES=1

model=llava-v1.6-mistral-7b

DATASET=chartmimic
python ./Training/LLaVA/llava/eval/model_vqa_chart2code.py \
    --model-path ./Training/LLaVA/ckpt/${model} \
    --question-file ./dataset/${DATASET}/chart2code_direct_mimic.json \
    --image-folder ./dataset/${DATASET}/images/ori \
    --answers-file ./results/${DATASET}/chart2code_${model}_DirectAgent_results.json \
    --temperature 0 \
    --conv-mode mistral_instruct

DATASET=reachqa
python ./Training/LLaVA/llava/eval/model_vqa_chart2code.py \
    --model-path ./Training/LLaVA/ckpt/${model} \
    --question-file ./dataset/${DATASET}/chart2code_direct_mimic.json \
    --image-folder ./dataset/${DATASET}/images/ori \
    --answers-file ./results/${DATASET}/chart2code_${model}_DirectAgent_results.json \
    --temperature 0 \
    --conv-mode mistral_instruct