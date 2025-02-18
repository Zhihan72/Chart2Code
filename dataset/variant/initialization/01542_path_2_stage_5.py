import matplotlib.pyplot as plt

objectives = ['Research', 'Exploration', 'Climate', 'Pollution']
proportions = [30, 25, 15, 10]
new_colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd']
explode = (0.1, 0, 0, 0)

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

plt.title("Ocean Exploration Priorities", fontsize=16, fontweight='normal', pad=15)
plt.setp(autotexts, size=9, weight="heavy")

ax.legend(wedges, objectives, title="Goals", loc="upper right", bbox_to_anchor=(1, 1, 0.3, 0.5), frameon=False)
fig.tight_layout()

plt.show()