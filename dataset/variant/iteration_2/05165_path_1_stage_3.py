import matplotlib.pyplot as plt
import numpy as np

# Data
north_rivers = [85, 87, 90, 88, 83, 82, 85, 90, 95, 89]
east_rivers = [78, 75, 80, 72, 74, 79, 76, 77, 75, 78]
south_rivers = [88, 80, 85, 87, 83, 84, 86, 82, 85, 88]
west_rivers = [65, 62, 70, 68, 72, 71, 69, 64, 66, 67]
central_rivers = [90, 88, 92, 91, 89, 95, 93, 94, 90, 92]
river_qualities = [north_rivers, east_rivers, south_rivers, west_rivers, central_rivers]

fig, ax = plt.subplots(figsize=(12, 7))

# Horizontal box plot creation
box = ax.boxplot(river_qualities, patch_artist=True, notch=True, vert=False,
                 boxprops=dict(facecolor='lightgrey', color='darkblue'),
                 medianprops=dict(color='orange'),
                 whiskerprops=dict(color='darkblue', linestyle=':'),
                 capprops=dict(color='darkblue'),
                 flierprops=dict(marker='x', color='darkblue', alpha=0.7))

# Set custom colors for each box
colors = ['#FFB6C1', '#ADD8E6', '#90EE90', '#DB7093', '#ADFF2F']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Removing textual elements
# The code for title, xlabel, ylabel, and ytick labels is removed

# Grid adjustments
ax.yaxis.grid(True, linestyle='-.', color='lightgrey', alpha=0.7)

# Enhanced border with spine customization
for spine in ax.spines.values():
    spine.set_edgecolor('grey')
    spine.set_linewidth(1.2)

# Tight layout
plt.tight_layout()

plt.show()