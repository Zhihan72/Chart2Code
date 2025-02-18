#!/bin/bash
PROJECT_PATH=./Training
cd ${PROJECT_PATH}
export PROJECT_PATH=${PROJECT_PATH}
export NCCL_P2P_DISABLE=1
export TOKENIZERS_PARALLELISM="false"

MODEL_NAME="./LLaVA/ckpt/llava-v1.6-mistral-7b"
OUTPUT_DIR="./LLaVA/ckpt/lora_your_output_name"
DATA_PATH="your_training_data_file"
IMAGE_FOLDER="image_foler_of_corresponding_data_file"

deepspeed --include localhost:1,2 ./LLaVA/llava/train/train_mem.py \
    --lora_enable True \
    --lora_r 128 \
    --lora_alpha 256 \
    --mm_projector_lr 2e-5 \
    --model_name_or_path ${MODEL_NAME} \
    --version v1 \
    --data_path ${DATA_PATH} \
    --image_folder ${IMAGE_FOLDER} \
    --vision_tower ./LLaVA/ckpt/clip-vit-large-patch14-336 \
    --deepspeed ./LLaVA/scripts/zero3.json \
    --mm_projector_type mlp2x_gelu \
    --mm_vision_select_layer -2 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --image_aspect_ratio pad \
    --group_by_modality_length True \
    --bf16 True \
    --output_dir ${OUTPUT_DIR} \
    --num_train_epochs 4 \
    --per_device_train_batch_size 16 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 50000 \
    --save_total_limit 1 \
    --learning_rate 2e-4 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 2048 \
    --gradient_checkpointing True \
    --dataloader_num_workers 4 \
    --lazy_preprocess True \
    --report_to wandb
