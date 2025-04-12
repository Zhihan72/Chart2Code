This repository releases the official data and code for the under-review paper addressing chart-to-code generation via iterative preference learning and dual rewarding mechanism. More details of our project are on the way.

# About Chart2Code

Chart-to-code generation—the process of converting chart images into executable plotting scripts—provides a lossless representation of chart information, requiring models to accurately capture and summarize all visual and structural elements. However, this remains a significant challenge for multimodal large language models (MLLMs), which are not inherently well-aligned with code generation tasks.

To bridge this gap, we introduce Chart2Code, a novel iterative dual preference learning framework designed to enhance MLLMs’ chart-to-code generation capabilities through structured code variant generation and fine-grained dual reward signals. We validate Chart2Code across three MLLMs and find that iterative preference learning consistently improves out-of-distribution chart-to-code generation quality.

Throughout this process, our dual scoring method, which evaluates both the textual code structure and its visual representation, leads to greater performance improvements, even with a reduced preference dataset size. Further analysis explores the key components of our framework and highlights the interplay between chart-to-code generation and broader chart reasoning, paving the way for future advancements in chart comprehension.

# Installation

<details>
<summary>LLaVA-v1.6-Mistral-7B</summary>

This build process is based on [LLaVA](https://github.com/haotian-liu/LLaVA):
  
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
# Replace dop_trainer.py with dop_trainer.py in the 'Training/scripts_llava' folder.
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

This build process is based on [InternVL](https://github.com/OpenGVLab/InternVL):

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
4. Prepare training and evaluation script.
```
mkdir ./Training/InternVL/scripts
mv ./scripts_internvl/training/finetune_lora_sft.sh ./Training/InternVL/scripts
mv ./scripts_internvl/training/finetune_lora_dpo.sh ./Training/InternVL/scripts
mv ./scripts_internvl/training/custom_dataset_sft.json ./Training/InternVL/scripts
mv ./scripts_internvl/training/custom_dataset_dpo.json ./Training/InternVL/scripts
mkdir ./Training/InternVL/internvl_chart/eval/chart2code
mv ./scripts_internvl/evaluation/evaluate_vqa.py ./Training/InternVL/internvl_chart/eval/chart2code
mv ./scripts_internvl/evaluation/evaluate_vqa_chartqa.py ./Training/InternVL/internvl_chart/eval/chart2code
mv ./scripts_internvl/evaluation/evaluation_sampling.sh ./Training/InternVL/scripts
```
</details>

<details>
<summary>Qwen2-VL-7B</summary>

This build process is based on [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory):

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
4. Prepare training and evaluation script.
```
mkdir ./Training/Qwen/scripts
mv ./scripts_qwen/training/finetune_lora_sft.sh ./Training/Qwen/scripts
mv ./scripts_qwen/training/finetune_lora_dpo.sh ./Training/Qwen/scripts
mv ./scripts_qwen/evaluation/evaluate_chart2code.py ./Training/Qwen/evaluate
mkdir ./Training/Qwen/evaluate
mv ./scripts_qwen/evaluation/evaluate_chartqa.py ./Training/Qwen/evaluate
mv ./scripts_qwen/evaluation/evaluation_sampling.sh ./Training/Qwen/scripts
```
</details>

# Dataset

Find the plotting scrips of our dataset in ```./dataset``` folder. Plotting scripts in ```./dataset/example``` and ```./dataset/variant``` are gold codes and variants, respectively.

## Gold Code Generation

Check ```./code_generation/gold_code_generation``` folder for codes and prompt templates.
```
python ./code_generation/gold_code_generation/generate_new_examples.py
```

## Variant Generation

Check ```./code_generation/variant_generation``` folder for codes and prompt templates. The rules and chart types are saved in ```./code_generation/rule_and_dimension```.
```
python ./code_generation/variant_generation/generate_code_variants.py
```

# Iterative Preference Training

1. Collect model-generated codes 
```
python ./Training/${model_name}/scripts/evaluate_chart2code.py
# Set the question file and image folder to the gold code at the current Iteration.
```
2. Collect reward signals
If using our trained evaluator or GPT-4o, use the following script:
```
bash ./preference_construction/generate_score.sh
```
If using heuristic F1-based code scoring, use the codes contributed by [ChartMimic](https://github.com/ChartMimic/ChartMimic):
```
cd ./Evaluation/eval_metrcis
git clone https://github.com/ChartMimic/ChartMimic.git
mv ./Evaluation/eval_metrcis/ChartMimic/* ./Evaluation/eval_metrcis/chart2code 
```
4. Make preference datasets
```
python ./preference_construction/collect_score_metadata.py
```
5. Train the model with DPO loss function.
```
bash ./Training/${model_name}/scripts/finetune_lora_dpo.py
# Set the question file and image folder to the variant code at the current Iteration.
```

Note that ```model_name``` can be ```LLaVA```, ```Qwen```, or ```InternVL```. For ```InternVL```, the question file and image folder should be saved in ```./Training/InternVL/scripts/custom_dataset_dpo.json```. For ```Qwen```, they should be added in the ```./Training/Qwen/data/dataset_info.json```.

# Evaluation

The inference codes for baselines can be found in ```./Evaluation/baselines```.

Download the evaluation datasets into ```./Evaluation/datasets``` from [ChartMimic](https://github.com/ChartMimic/ChartMimic), [ReachQA](https://github.com/hewei2001/ReachQA), and [CharXiv](https://github.com/princeton-nlp/CharXiv).

The implementations of evaluation metrics are the same as reward signal collection during iterative preference learning.

# Acknowledgement

The code is based on [LLaVA](https://github.com/haotian-liu/LLaVA), [InternVL](https://github.com/OpenGVLab/InternVL), and [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory). We adapted part of the [ChartMimic](https://github.com/ChartMimic/ChartMimic)'s codebase in generating rewarding signals and downstream evaluation. We greatly appreciate all their contributions to the MLLM community.
