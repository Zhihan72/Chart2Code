set -x

PROJECT_PATH=./Training
cd ${PROJECT_PATH}
export NCCL_P2P_DISABLE=1
export NCCL_IB_DISABLE=1
export NCCL_SOCKET_IFNAME=en,eth,em,bond
export NCCL_DEBUG=INFO
export CUDA_LAUNCH_BLOCKING=1
export CUDA_VISIBLE_DEVICES=2,3

GPUS=${GPUS:-2}
BATCH_SIZE=${BATCH_SIZE:-8}
PER_DEVICE_BATCH_SIZE=${PER_DEVICE_BATCH_SIZE:-4}
GRADIENT_ACC=$((BATCH_SIZE / PER_DEVICE_BATCH_SIZE / GPUS))

export PYTHONPATH="./Training/InternVL/internvl_chat"
export MASTER_PORT=33229
export TF_CPP_MIN_LOG_LEVEL=3
export LAUNCHER=pytorch

MODEL_PATH='./InternVL/ckpt/InternVL2_5-2B'
META_PATH='./Training/scripts_internvl/training/custom_dataset_sft.json'
OUTPUT_DIR='./InternVL/ckpt/your_output_path'
DEEPSPEED_CONFIG='./InternVL/internvl_chat/zero_stage1_config.json'

if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
fi

torchrun \
  --nnodes=1 \
  --node_rank=0 \
  --master_addr=127.0.0.1 \
  --nproc_per_node=${GPUS} \
  --master_port=${MASTER_PORT} \
  ./InternVL/internvl_chat/internvl/train/internvl_chat_finetune.py \
  --model_name_or_path ${MODEL_PATH}\
  --conv_style "internvl2_5" \
  --use_fast_tokenizer False \
  --output_dir ${OUTPUT_DIR} \
  --meta_path ${META_PATH} \
  --overwrite_output_dir True \
  --force_image_size 448 \
  --max_dynamic_patch 6 \
  --down_sample_ratio 0.5 \
  --drop_path_rate 0.0 \
  --freeze_llm True \
  --freeze_mlp True \
  --freeze_backbone True \
  --use_llm_lora 128 \
  --vision_select_layer -1 \
  --dataloader_num_workers 4 \
  --bf16 True \
  --num_train_epochs 4 \
  --per_device_train_batch_size ${PER_DEVICE_BATCH_SIZE} \
  --gradient_accumulation_steps ${GRADIENT_ACC} \
  --evaluation_strategy "no" \
  --save_strategy "steps" \
  --save_steps 50000 \
  --save_total_limit 1 \
  --learning_rate 2e-4 \
  --weight_decay 0.05 \
  --warmup_ratio 0.03 \
  --lr_scheduler_type "cosine" \
  --logging_steps 1 \
  --max_seq_length 8192 \
  --do_train True \
  --grad_checkpoint True \
  --group_by_length True \
  --dynamic_image_size True \
  --use_thumbnail True \
  --ps_version 'v2' \
  --deepspeed ${DEEPSPEED_CONFIG} \
  --report_to "wandb" \
  --save_only_model
