import numpy as np
import matplotlib.pyplot as plt

# Define the data including a new group for Brazil
sales_data = np.array([
    [120, 100, 110, 140, 150, 130, 145, 180, 160, 175, 190, 210],  # USA
    [90, 85, 100, 95, 105, 115, 120, 130, 140, 150, 160, 170],     # Canada
    [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],  # Germany
    [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170],      # Australia
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190],    # India
    [110, 95, 100, 115, 125, 135, 140, 155, 165, 175, 185, 195]    # Brazil
])

average_sales = sales_data.mean(axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
index = np.arange(sales_data.shape[1])

# Updated colors for the additional data series
shuffled_colors = ['#4682B4', '#32CD32', '#FFD700', '#FF6347', '#800080', '#FF69B4']

for i in range(len(sales_data)):
    ax.barh(index + i * bar_height, sales_data[i], bar_height, color=shuffled_colors[i], alpha=0.75)

# Randomized average sales line styles
line_styles = [':', '-.', '--', '-']
for j, avg in enumerate(average_sales):
    ax.plot([avg]*len(index), index + 2*bar_height, color='black', linestyle=line_styles[j % len(line_styles)], 
            marker=marker_styles[j % len(marker_styles)], linewidth=2, markersize=6)

ax.set_yticks([])
ax.set_yticklabels([])

plt.grid(axis='x', color='gray', linestyle='dotted')
plt.tight_layout()
plt.show()