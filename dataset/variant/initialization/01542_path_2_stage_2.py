import matplotlib.pyplot as plt

objectives = ['Scientific Research', 'Biodiversity\nAssessment', 'Resource\nExploration', 'Climate\nMonitoring', 'Pollution\nStudies']
proportions = [30, 20, 25, 15, 10]
new_colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
explode = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=objectives, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=new_colors, 
    explode=explode,
    shadow=True,
    textprops=dict(color="w"),
    wedgeprops=dict(width=0.3, edgecolor='w', linewidth=2)
)

plt.title("Priorities in Ocean Exploration Missions:\nA Decadal Overview", fontsize=16, fontweight='bold', pad=20)
plt.setp(autotexts, size=10, weight="bold")

ax.legend(wedges, objectives, title="Objectives", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
fig.tight_layout()

plt.show()