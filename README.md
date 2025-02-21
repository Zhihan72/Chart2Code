This repository releases the official data and code for the paper "Enhancing Chart-to-Code Generation in Multimodal Large Language Models via Iterative Dual Preference Learning". 

This repository is used for double-blind reviewing process. ANYONE is NOT allowed to distribute our data and code at ANYTIME during the reviewing process.

# About Chart2Code

Chart-to-code generation—the process of converting chart images into executable plotting scripts—provides a lossless representation of chart information, requiring models to accurately capture and summarize all visual and structural elements. However, this remains a significant challenge for multimodal large language models (MLLMs), which are not inherently well-aligned with code generation tasks.

To bridge this gap, we introduce Chart2Code, a novel iterative dual preference learning framework designed to enhance MLLMs’ chart-to-code generation capabilities through structured code variant generation and fine-grained dual reward signals. We validate Chart2Code across three MLLMs and find that iterative preference learning consistently improves out-of-distribution chart-to-code generation quality.

Throughout this process, our dual scoring method, which evaluates both the textual code structure and its visual representation, leads to greater performance improvements, even with a reduced preference dataset size. Further analysis explores the key components of our framework and highlights the interplay between chart-to-code generation and broader chart reasoning, paving the way for future advancements in chart comprehension.

# Installation

<details>
<summary>LLaVA-v1.6-Mistral-7B</summary>

This build process based on [LLaVA](https://github.com/haotian-liu/LLaVA):
  
1. Clone this respository and move it to our ```./Training``` folder.

```
git clone https://github.com/haotian-liu/LLaVA.git
mv LLaVA ./Training
```
2. Install Package
```
cd ./Training/LLaVA
conda create -n llava python=3.10 -y
conda activate llava
pip install trl
```
3. Install additional packages for training cases
```
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```
4. Modify the TRL library adjust DPO for LLaVA
```
cd *your conda path*/envs/csr/lib/python3.10/site-packages/trl/trainer/
# Replace dop_trainer.py with dop_trainer.py in the 'Training/scripts_llava/dpo_llava_trainer.py' folder.
```
5. Modify the parent class of llava_trainer
```
cd ./LLaVA/llava/train

# Modify llava_trainer.py as follows:

# from trl import DPOTrainer
# ...
# ...
# ...
# class LLaVATrainer(DPOTrainer):
```
6. Prepare training and evaluation script.
```
mkdir ./Training/LLaVA/scripts
mv ./scripts_llava/training/finetune_lora_sft.sh ./Training/LLaVA/scripts
mv ./scripts_llava/training/finetune_lora_dpo.sh ./Training/LLaVA/scripts
mv ./scripts_llava/evaluation/model_vqa_chart2code.py ./Training/LLaVA/llava/eval
mv ./scripts_llava/evaluation/model_vqa_chart2qa.py ./Training/LLaVA/llava/eval
mv ./scripts_llava/evaluation/evaluation_sampling.sh ./Training/LLaVA/scripts
```
</details>

<details>
<summary>InternVL2.5-2B</summary>

This build process based on [InternVL](https://github.com/OpenGVLab/InternVL):

1. Clone this respository and move it to our ```./Training``` folder.

```
git clone https://github.com/OpenGVLab/InternVL.git
mv InternVL ./Training
```
2. Install Package
```
cd ./Training/InternVL
conda create -n internvl python=3.10 -y
conda activate internvl
```
3. Install additional packages for training cases
```
pip install -e ".requirements/internvl_chat.txt"
```
</details>

<details>
<summary>Qwen2-VL-7B</summary>

This build process based on [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory):

1. Clone this respository and navigate to LLaVA folder

```
git clone https://github.com/hiyouga/LLaMA-Factory.git
mv LLaMA-Factory ./Training/Qwen
```
2. Install Package
```
cd ./Training/Qwen
conda create -n qwen python=3.10 -y
conda activate qwen
```
3. Install additional packages for training cases
```
pip install -e "requirementst.txt"
```

</details>

# Dataset

## Gold Code Generation

The following parts will be updated soon. Thank you for your patience!

## Variant Generation

Variant Path Sampling


# Experiment

## Iterative Preference Training

This dataset is built on xxx.

List DPO training process.

## Evaluation

List scripts for evaluation

# Acknowledgement

The code is based on [LLaVA](https://github.com/haotian-liu/LLaVA), [InternVL](https://github.com/OpenGVLab/InternVL), and [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory). We adapted part of the [ChartMimic](https://github.com/ChartMimic/ChartMimic)'s codebase in downstream evaluation and generating rewarding signals. We greatly appreciate all their contributions to the MLLM community.
