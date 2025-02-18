This repository releases the official data and code for the paper "Enhancing Chart-to-Code Generation in Multimodal Large Language Models via Iterative Dual Preference Learning". 

This repository is used for double-blind reviewing process. ANYONE is NOT allowed to distribute our data and code at ANYTIME during the reviewing process.

# About Chart2Code

Chart-to-code generation—the process of converting chart images into executable plotting scripts—provides a lossless representation of chart information, requiring models to accurately capture and summarize all visual and structural elements. However, this remains a significant challenge for multimodal large language models (MLLMs), which are not inherently well-aligned with code generation tasks.

To bridge this gap, we introduce Chart2Code, a novel iterative dual preference learning framework designed to enhance MLLMs’ chart-to-code generation capabilities through structured code variant generation and fine-grained dual reward signals. We validate Chart2Code across three MLLMs and find that iterative preference learning consistently improves out-of-distribution chart-to-code generation quality.

Throughout this process, our dual scoring method, which evaluates both the textual code structure and its visual representation, leads to greater performance improvements, even with a reduced preference dataset size. Further analysis explores the key components of our framework and highlights the interplay between chart-to-code generation and broader chart reasoning, paving the way for future advancements in chart comprehension.

# Installation

Taking LLaVA-v1.6-Mistral-7B for example, this build process based on LLaVA: 

1. Clone this respository and navigate to LLaVA folder

```
   puts "Hello World"
```

<details>
<summary>InternVL</summary>

This build process based on LLaVA:

1. Clone this respository and navigate to LLaVA folder

```
   puts "Hello World"
```

</details>

# Dataset

## Gold Code Generation


## Variant Generation

Variant Path Sampling


# Experiment

## Iterative Preference Training

This dataset is built on xxx.

List DPO training process.

## Evaluation

List scripts for evaluation

# Acknowledgement

The code is based on LLaVA-NeXT, InternVL, and llama-factory. Thanks for all these great works and open sourcing!
