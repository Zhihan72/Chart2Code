#!/bin/bash

export CUDA_VISIBLE_DEVICES=2

models=(
    llava-v1.6-mistral-7b
)

dataset=chartmimic
for model in "${models[@]}"; do
    echo "$model"
    python ./Evaluation/eval_metrcis/evaluator/generate_score.py\
        --base-model ./Training/your_evaluator_base_model \
        --lora-path ./Training/your_evaluator_lora \
        --dataset ${dataset} \
        --model-name ${model}
done