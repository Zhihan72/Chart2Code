import matplotlib.pyplot as plt

# Data definition for ocean exploration objectives
objectives = ['Scientific Research', 'Biodiversity\nAssessment', 'Resource\nExploration', 'Climate\nMonitoring', 'Pollution\nStudies']
proportions = [30, 20, 25, 15, 10]
single_color = '#66B3FF'  # Use a single color for all

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=objectives, 
    autopct='%1.1f%%', 
    startangle=100,
    colors=[single_color]*len(proportions),  # Apply the single color across all slices
    explode=(0, 0, 0, 0.1, 0.1),
    shadow=False,
    textprops=dict(color="black"),
    wedgeprops=dict(edgecolor='grey', linewidth=1)
)

plt.title("Ocean Exploration Mission Priorities", fontsize=14, fontweight='medium', pad=10)
plt.setp(autotexts, size=9, fontweight="light")

ax.legend(wedges, objectives, title="Objectives", loc="upper left", bbox_to_anchor=(0.9, 0.9))

plt.show()