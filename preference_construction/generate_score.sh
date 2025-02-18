#!/bin/bash
export CUDA_VISIBLE_DEVICES=3

stage_nm=1
model=llava-v1.6-mistral-7b

# Our evaluator: Multi-dimensional binary scoring
evaluator=Phi
python ./preference_construction/generate_score.py\
    --base-model ./Training/Phi_eval/ckpt/Phi-3.5-vision-instruct \
    --lora-path ./Training/Phi_eval/ckpt/lora_critic_s0_variants/checkpoint-843 \
    --stage-name ${stage_nm} \
    --model-name ${model} \

python ./preference_construction/collect_score_metadata.py \
    --evaluator ${evaluator} \
    --stage-name ${stage_nm} \
    --model-name ${model} \

# GPT continous scoring
evaluator=gpt
python ./preference_construction/generate_score.py\
    --base-model gpt-4o \
    --stage-name ${stage_nm} \
    --model-name ${model} \

evaluator=gpt
python ./preference_construction/collect_score_metadata.py \
    --evaluator ${evaluator} \
    --stage-name ${stage_nm} \
    --model-name ${model} \