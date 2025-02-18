import matplotlib.pyplot as plt
import numpy as np

districts = ['Cntrl', 'East', 'West', 'N. Hill', 'S. Field', 'Lake']

central_parks = [2, 5, 7, 10, 15, 18, 22, 25, 28, 30]
eastside_parks = [3, 4, 6, 8, 9, 12, 13, 15, 17, 20]
westend_parks = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
north_hills_parks = [1, 3, 4, 6, 8, 11, 14, 18, 19, 22]
southfield_parks = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
lakeside_parks = [2, 4, 7, 8, 10, 11, 14, 15, 18, 21]

park_sizes = [central_parks, eastside_parks, westend_parks, north_hills_parks, southfield_parks, lakeside_parks]

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF6666', '#B3B3CC']

boxes = ax.boxplot(park_sizes, patch_artist=True, notch=False, vert=False,
                   boxprops=dict(color='black', linewidth=1.5),
                   medianprops=dict(color='blue', linewidth=2),
                   whiskerprops=dict(color='green', linewidth=1.5),
                   capprops=dict(color='black', linewidth=1.5),
                   flierprops=dict(marker='x', color='orange', alpha=0.8, markersize=8))

for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_title('Park Size Distribution 2023', fontsize=16, fontweight='bold')
ax.set_ylabel('Dist.', fontsize=12)
ax.set_xlabel('Size (Acres)', fontsize=12)
ax.set_yticks(np.arange(1, len(districts) + 1))
ax.set_yticklabels(districts, rotation=30, ha='right', fontsize=10)

ax.xaxis.grid(True, linestyle=':', which='major', color='black', alpha=0.3)

plt.tight_layout()

plt.show()