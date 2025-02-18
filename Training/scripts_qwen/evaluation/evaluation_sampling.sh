#!/bin/bash
PROJECT_PATH=./Evaluation
cd ${PROJECT_PATH}
export NCCL_P2P_DISABLE=1
export TOKENIZERS_PARALLELISM="false"
export CUDA_VISIBLE_DEVICES=4

export MASTER_PORT=33229
export TF_CPP_MIN_LOG_LEVEL=3

model=Qwen2-VL-7B-Instruct

DATASET=chartmimic
python ./Training/Qwen/inference/evaluate_chart2code.py \
    --model-path ./Training/Qwen/ckpt/${model} \
    --question-file ./dataset/${DATASET}/chart2code_direct_mimic.json \
    --image-folder ./dataset/${DATASET}/images/ori \
    --answers-file ./results/${DATASET}/chart2code_${model}_DirectAgent_results.json \

DATASET=reachqa
python ./Training/Qwen/inference/evaluate_chart2code.py \
    --model-path ./Training/Qwen/ckpt/${model} \
    --question-file ./dataset/${DATASET}/chart2code_direct_mimic.json \
    --image-folder ./dataset/${DATASET}/images/ori \
    --answers-file ./results/${DATASET}/chart2code_${model}_DirectAgent_results.json \