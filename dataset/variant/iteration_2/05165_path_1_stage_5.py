import matplotlib.pyplot as plt
import numpy as np

# Altered Data
north_rivers = [90, 85, 83, 87, 82, 95, 85, 89, 90, 88]
east_rivers = [80, 75, 78, 72, 74, 77, 79, 78, 76, 75]
south_rivers = [85, 86, 80, 82, 88, 83, 84, 85, 88, 87]
west_rivers = [66, 68, 65, 71, 69, 67, 64, 70, 62, 72]
central_rivers = [92, 90, 89, 94, 93, 88, 91, 90, 95, 92]
river_qualities = [north_rivers, east_rivers, south_rivers, west_rivers, central_rivers]

fig, ax = plt.subplots(figsize=(12, 7))

box = ax.boxplot(river_qualities, patch_artist=True, notch=True, vert=False,
                 boxprops=dict(facecolor='lightgrey', color='darkblue'),
                 medianprops=dict(color='orange'),
                 whiskerprops=dict(color='darkblue', linestyle=':'),
                 capprops=dict(color='darkblue'),
                 flierprops=dict(marker='x', color='darkblue', alpha=0.7))

# Colors are shuffled manually
colors = ['#DB7093', '#ADFF2F', '#90EE90', '#FFB6C1', '#ADD8E6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Grid adjustments
ax.yaxis.grid(True, linestyle='-.', color='lightgrey', alpha=0.7)

# Enhanced border with spine customization
for spine in ax.spines.values():
    spine.set_edgecolor('grey')
    spine.set_linewidth(1.2)

plt.tight_layout()

plt.show()