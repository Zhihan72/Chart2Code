import matplotlib.pyplot as plt

objectives = ['Scientific Research', 'Biodiversity\nAssessment', 'Resource\nExploration', 'Climate\nMonitoring', 'Pollution\nStudies']
proportions = [30, 20, 25, 15, 10]
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
explode = (0.1, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(9, 7))

wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=objectives,
    autopct='%1.1f%%', 
    startangle=100, 
    colors=new_colors, 
    explode=explode,
    shadow=False,
    textprops=dict(color="black"),
    wedgeprops=dict(width=0.4, edgecolor='gray', linestyle='--', linewidth=1),
)

plt.title("Priorities in Ocean Exploration Missions:\nA Decadal Perspective", fontsize=18, fontweight='normal', pad=15)
plt.setp(autotexts, size=9, weight="heavy")

ax.legend(wedges, objectives, title="Objectives", loc="upper right", bbox_to_anchor=(1, 1, 0.3, 0.5), frameon=False)
fig.tight_layout()

plt.show()