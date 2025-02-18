import json
import os
import pandas as pd

def get_code_passed_files(modelagent, dataset):
    template_type = modelagent.split("_")[-1].split("Agent")[0].lower()
    file_dir = "./Evaluation/results/{}/chart2code_{}_results/{}_checker".format(dataset, modelagent, template_type)
    filter_files = os.listdir(file_dir)
    filter_files = [ item.split(".pdf")[0] for item in filter_files if ".pdf" in item]
    return filter_files

dataset = 'reachqa' # chartmimic, reachqa, customizemimic, matplotbench
image_evaluator = 'batch_gpt-4o' # gpt-4o-mini, gpt-4o

models=[
    "llava-v1.6-mistral-7b",
]

denominator = 500
agents = ["DirectAgent"] # "DirectAgent", "HintEnhancedAgent", "ScaffoldAgent", "SelfRevisionAgent"
model_agents = [ "{}_{}".format(model, agent) for model in models for agent in agents ]
filter_type = "code_pass" # no_filter, code_pass, chartedit, different_level

if filter_type == "no_filter":
    filter_files_dict = None
elif filter_type == "code_pass":
    filter_files_dict = { model_agent: get_code_passed_files(model_agent, dataset) for model_agent in model_agents}
else:
    raise ValueError("filter_type not supported")

# construct a dataframe, "model" column is the model name
result_df = pd.DataFrame(columns=[
    "model_agent", "example_count","ExecRate", 
    "TextScore", "LayoutScore", "TypeScore", "ColorScore", "Average", 
    "GPT4VScore", "Overall", 
    "Phi_TextScore", "Phi_TypetScore", "Phi_LayoutScore", "Phi_DataScore", "Phi_StyleScore", "Phi_ColorScore", "Phi_Score"])
result_df["model_agent"] = [ model + "_" + agent for model in models for agent in agents]
result_df.set_index("model_agent", inplace=True)

### Code Evaluation

files = []
for model in models:
    for agent in agents:
        filename =  f"./Evaluation/results/{dataset}/chart2code_" + model + "_" + agent +"_results_code4evaluation.json"
        if os.path.exists(filename) or dataset=='matplotbench':
            files.append(filename)
        else:
            raise FileNotFoundError("File not found: {}".format(filename))

for idx, file in enumerate(files):
    if dataset=='matplotbench':
        filter_files = filter_files_dict[model_agents[idx]]
        result_df.loc[model_agents[idx], "ExecRate"] = len(filter_files) / denominator * 100
        print("Execution Rate:", len(filter_files) / denominator)
        continue
    print("Processing file:", os.path.basename(file))
    data = pd.read_json(file, lines=True)
    data["orginial"] = data["orginial"].apply(lambda x: x.split("/")[-1])
    data["generated"] = data["generated"].apply(lambda x: x.split("/")[-1])

    if filter_files_dict is not None:
        filter_files = filter_files_dict[model_agents[idx]]
        data = data[ data["orginial"].apply(lambda x: any([item == x.replace('.py','') for item in filter_files])) ]
        print("Length of filter files:", len(filter_files))
    print("Length of Data:", len(data))
    print("Denominator:", denominator)

    result_df.loc[model_agents[idx], "example_count"] = len(data)
    result_df.loc[model_agents[idx], "ExecRate"] = len(filter_files) / denominator * 100
    print("Execution Rate:", len(filter_files) / denominator)

    f1s = []
    text_metrics = data["text_metrics"]
    avg_f1 = text_metrics.apply(lambda x: x["f1"]).sum()*100 / denominator
    result_df.loc[model_agents[idx], "TextScore"] = avg_f1
    f1s.append(avg_f1)

    layout_metrics = data['layout_metrics']
    avg_f1 = layout_metrics.apply(lambda x: x["f1"]).sum()*100 / denominator
    result_df.loc[model_agents[idx], "LayoutScore"] = avg_f1
    f1s.append(avg_f1)

    chart_type_metrics = data["chart_type_metrics"]
    avg_f1 = chart_type_metrics.apply(lambda x: x["f1"]).sum()*100 / denominator
    result_df.loc[model_agents[idx], "TypeScore"] = avg_f1
    f1s.append(avg_f1)

    color_metrics = data["color_metrics"]
    avg_f1 = color_metrics.apply(lambda x: x["f1"]).sum()*100 / denominator
    result_df.loc[model_agents[idx], "ColorScore"] = avg_f1
    f1s.append(avg_f1)

    result_df.loc[model_agents[idx], "Average"] = sum(f1s)/len(f1s)
    print("Average fl-scores:", sum(f1s)/len(f1s))

### Image Evaluation

files = []
for model in models:
    for agent in agents:
        file =  f"./Evaluation/results/{dataset}/chart2code_" + model + "_" + agent + f"_results_gpt4evaluation_{image_evaluator}.json"
        if os.path.exists(file):
            files.append(file)

for idx, file in enumerate(files):
    print("Processing file:", os.path.basename(file))

    data = pd.read_json(file, lines=True)
    data["orginial"] = data["orginial"].apply(lambda x: x.split("/")[-1])
    data["generated"] = data["generated"].apply(lambda x: x.split("/")[-1])
    if filter_files_dict is not None:
        filter_files = filter_files_dict[model_agents[idx]]
        data = data[ data["orginial"].apply(lambda x: any([item == x.replace('.pdf','') for item in filter_files])) ]

    gpt4v_score = [x for x in data["score"].tolist() if x!=-1]
    avg_gpt4v_score = sum(gpt4v_score) / denominator
    result_df.loc[model_agents[idx], "GPT4VScore"] = avg_gpt4v_score * 100
    print(f"Average {image_evaluator}-scores:", avg_gpt4v_score)

### Trained Image Evaluation

files = []
for model in models:
    for agent in agents:
        file =  f"./Evaluation/results/{dataset}/chart2code_" + model + "_" + agent + f"_results_trained4evaluation.jsonl"
        if os.path.exists(file):
            files.append(file)

for idx, file in enumerate(files):
    print("Processing file:", os.path.basename(file))

    # data = pd.read_json(file, lines=True)
    data = pd.read_json(file, lines=True,)
    data["orginial"] = data["question_id"]
    data["generated"] = data["question_id"]

    if filter_files_dict is not None:
        filter_files = filter_files_dict[model_agents[idx]]
        if dataset=='reachqa':
            data = data[ data["orginial"].apply(lambda x: any(['00'+str(x) in item for item in filter_files])) ]
        else:
            data = data[ data["orginial"].apply(lambda x: any([item == x.replace('.pdf','') for item in filter_files])) ]
    
    result_df.loc[model_agents[idx], "Phi_TypetScore"] = data['dim_dict'].apply(lambda x: x["type"]).sum() / denominator
    result_df.loc[model_agents[idx], "Phi_LayoutScore"] = data['dim_dict'].apply(lambda x: x["layout"]).sum() / denominator
    result_df.loc[model_agents[idx], "Phi_DataScore"] = data['dim_dict'].apply(lambda x: x["data"]).sum() / denominator
    result_df.loc[model_agents[idx], "Phi_StyleScore"] = data['dim_dict'].apply(lambda x: x["style"]).sum() / denominator
    result_df.loc[model_agents[idx], "Phi_TextScore"] = data['dim_dict'].apply(lambda x: x["text"]).sum() / denominator
    result_df.loc[model_agents[idx], "Phi_ColorScore"] = data['dim_dict'].apply(lambda x: x["color"]).sum() / denominator
    result_df.loc[model_agents[idx], "Phi_Score"] = data['dim_dict'].apply(lambda x: x["final"]).sum() / denominator

    print(f"Average Phi-scores:", result_df.loc[model_agents[idx]]["Phi_Score"])

# calculate the overall score
result_df["Overall"] = result_df[["Average", "GPT4VScore"]].mean(axis=1)
result_df.to_csv(f'.Evaluation/scripts/results_{dataset}_wPhi.csv', index=True)