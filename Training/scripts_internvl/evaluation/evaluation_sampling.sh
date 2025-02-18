#!/bin/bash
PROJECT_PATH=./Evaluation
cd ${PROJECT_PATH}
export NCCL_P2P_DISABLE=1
export TOKENIZERS_PARALLELISM="false"
export CUDA_VISIBLE_DEVICES=2

export PYTHONPATH="./Training/InternVL/internvl_chat"
export MASTER_PORT=33229
export TF_CPP_MIN_LOG_LEVEL=3


model=InternVL2_5-2B

DATASET=chartmimic
python ./Training/InternVL/internvl_chat/eval/chart2code/evaluate_vqa.py \
    --model-path ./Training/InternVL/ckpt/${model} \
    --question-file ./dataset/${DATASET}/chart2code_direct_mimic.json \
    --image-folder ./dataset/${DATASET}/images/ori \
    --answers-file ./results/${DATASET}/chart2code_${model}_DirectAgent_results.json \

DATASET=reachqa
python ./Training/InternVL/internvl_chat/eval/chart2code/evaluate_vqa.py \
    --model-path ./Training/InternVL/ckpt/${model} \
    --question-file ./dataset/${DATASET}/chart2code_direct_mimic.json \
    --image-folder ./dataset/${DATASET}/images/ori \
    --answers-file ./results/${DATASET}/chart2code_${model}_DirectAgent_results.json