import matplotlib.pyplot as plt

# Define growth data for each sector
ai_growth = [22, 27, 19, 25, 30]
cyber_growth = [12, 18, 15, 22, 17]
fintech_growth = [35, 28, 40, 33, 45]
edtech_growth = [8, 15, 10, 14, 9]
healthtech_growth = [25, 23, 20, 26, 27]
agritech_growth = [15, 20, 18, 23, 21]  # New data series
cleantech_growth = [30, 34, 32, 33, 31]  # New data series

growth_data = [
    ai_growth, cyber_growth, fintech_growth, edtech_growth, 
    healthtech_growth, agritech_growth, cleantech_growth
]

# Define distinct colors
colors = ['lightcoral', 'lightblue', 'lightgreen', 'peachpuff', 
          'lightsalmon', 'lightsteelblue', 'lightpink']

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create a boxplot with shuffled colors
ax.boxplot(growth_data, vert=False, notch=True, patch_artist=True,
           boxprops=dict(facecolor=colors[0], color=colors[0]),
           whiskerprops=dict(color=colors[0]),
           capprops=dict(color=colors[0]),
           medianprops=dict(color=colors[0], linewidth=2),
           flierprops=dict(marker='o', color=colors[0], markersize=8, alpha=0.5))

# Set tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])

# Other plot configurations
plt.yticks([])
plt.xticks([])
plt.tight_layout()

plt.show()