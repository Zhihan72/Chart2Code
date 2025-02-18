export NCCL_P2P_DISABLE=1
export NCCL_IB_DISABLE=1
export NCCL_SOCKET_IFNAME=en,eth,em,bond
export NCCL_DEBUG=INFO
export CUDA_LAUNCH_BLOCKING=1
export CUDA_VISIBLE_DEVICES=1,2

GPUS=${GPUS:-2}
BATCH_SIZE=${BATCH_SIZE:-2}
PER_DEVICE_BATCH_SIZE=${PER_DEVICE_BATCH_SIZE:-1}
GRADIENT_ACC=$((BATCH_SIZE / PER_DEVICE_BATCH_SIZE / GPUS))

PYTHONPATH="./Training/Qwen/LLaMA-Factory"
export PYTHONPATH=$PYTHONPATH
cd ${PYTHONPATH}
export TRITON_CACHE_DIR="./tmp/triton/"
export MASTER_PORT=33720
export TF_CPP_MIN_LOG_LEVEL=3
export LAUNCHER=pytorch

DS_CONFIG_PATH='./Training/InternVL/internvl_chat/zero_stage1_config.json'
MODEL_PATH=' ./Training/Qwen/ckpt/Qwen2-VL-7B-Instruct'
OUTPUT_PATH='./Training/Qwen/ckpt/your_output_path'

torchrun \
    --nnodes=1 \
    --node_rank=0 \
    --master_addr=127.0.0.1 \
    --nproc_per_node=${GPUS} \
    --master_port=${MASTER_PORT} \
    ./src/train.py \
    --deepspeed $DS_CONFIG_PATH \
    --num_train_epochs 4 \
    --stage sft \
    --do_train \
    --use_fast_tokenizer \
    --flash_attn auto \
    --model_name_or_path $MODEL_PATH \
    --dataset reachqa_train \
    --image_resolution 262144 \
    --video_resolution 16384 \
    --trust_remote_code \
    --template qwen2_vl \
    --finetuning_type lora \
    --lora_target all\
    --lora_rank 128 \
    --pref_beta 0.1 \
    --pref_loss sigmoid \
    --output_dir $OUTPUT_PATH \
    --overwrite_cache \
    --overwrite_output_dir \
    --weight_decay 0.05 \
    --warmup_ratio 0.03 \
    --per_device_train_batch_size $PER_DEVICE_BATCH_SIZE \
    --gradient_accumulation_steps $GRADIENT_ACC \
    --ddp_timeout 180000000 \
    --learning_rate 2e-4 \
    --lr_scheduler_type cosine \
    --logging_steps 1 \
    --cutoff_len 4096 \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 50000 \
    --save_total_limit 1 \
    --plot_loss \
    --bf16