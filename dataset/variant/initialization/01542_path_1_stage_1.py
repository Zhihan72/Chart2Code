import matplotlib.pyplot as plt

# Data definition for ocean exploration objectives
objectives = ['Scientific Research', 'Biodiversity\nAssessment', 'Resource\nExploration', 'Climate\nMonitoring', 'Pollution\nStudies']
proportions = [30, 20, 25, 15, 10]
colors = ['#66B3FF', '#FF6347', '#99FF99', '#FF9999', '#FFD700']  # Altered colors

fig, ax = plt.subplots(figsize=(9, 9))
wedges, texts, autotexts = ax.pie(
    proportions, 
    labels=objectives, 
    autopct='%1.1f%%', 
    startangle=100,  # Changed start angle for a different orientation
    colors=colors, 
    explode=(0, 0, 0, 0.1, 0.1),  # Changed slices to emphasize different categories
    shadow=False,  # Removed shadow
    textprops=dict(color="black"),  # Altered text color
    wedgeprops=dict(edgecolor='grey', linewidth=1)
)

plt.title("Ocean Exploration Mission Priorities", fontsize=14, fontweight='medium', pad=10)
plt.setp(autotexts, size=9, fontweight="light")

# Legend inside the chart for diversity
ax.legend(wedges, objectives, title="Objectives", loc="upper left", bbox_to_anchor=(0.9, 0.9))

# Display the plot
plt.show()