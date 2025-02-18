import matplotlib.pyplot as plt
import numpy as np

# Data for each category
carrots_yield = [
    [1.3, 1.5, 1.6, 1.8, 1.4],
    [2.0, 2.2, 2.1, 2.3, 2.4],
    [1.0, 1.2, 1.1, 1.3, 1.2]
]

potatoes_yield = [
    [3.0, 3.2, 3.3, 3.4, 3.1],
    [4.0, 4.2, 4.1, 4.3, 4.4],
    [2.5, 2.7, 2.6, 2.8, 2.7]
]

tomatoes_yield = [
    [5.0, 5.3, 5.1, 5.4, 5.2],
    [6.0, 6.3, 6.1, 6.4, 6.2],
    [4.0, 4.2, 4.1, 4.3, 4.2]
]

cabbages_yield = [
    [2.5, 2.7, 2.8, 2.9, 2.6],
    [3.0, 3.3, 3.2, 3.4, 3.5],
    [1.8, 2.0, 1.9, 2.1, 2.0]
]

# Grouped data
data = [carrots_yield, potatoes_yield, tomatoes_yield, cabbages_yield]

fig, ax = plt.subplots(figsize=(14, 8))

# Define positions for each category
group_spacing = 4  # Space between categories
subgroup_spacing = 1  # Space between subgroups within a category
positions = []

for i in range(len(data)):  # For each category
    start_pos = i * group_spacing
    positions.extend([start_pos + j * subgroup_spacing for j in range(len(data[i]))])

# Colors for each category
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

# Plot each category
for i, yields in enumerate(data):
    start_pos = i * group_spacing
    pos = [start_pos + j * subgroup_spacing for j in range(len(yields))]
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=True)
    
    # Apply colors and styles
    for patch, color in zip(bp['boxes'], [colors[i]] * len(yields)):
        patch.set_facecolor(color)
        patch.set_edgecolor('blue')

    for whisker in bp['whiskers']:
        whisker.set(color='purple', linewidth=1.0, linestyle='-.')
    for cap in bp['caps']:
        cap.set(color='purple', linewidth=1.0, linestyle=':')
    for median in bp['medians']:
        median.set(color='orange', linewidth=3)

# Set x-ticks and labels
category_positions = [i * group_spacing + (len(data[i]) - 1) / 2 * subgroup_spacing for i in range(len(data))]
ax.set_xticks(category_positions)
ax.set_xticklabels(['Carrots', 'Potatoes', 'Tomatoes', 'Cabbages'], fontsize=12)

ax.set_title("Yield Distribution by Crop", fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel("Yield (kg per plant)", fontsize=14)
ax.grid(axis='y', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()