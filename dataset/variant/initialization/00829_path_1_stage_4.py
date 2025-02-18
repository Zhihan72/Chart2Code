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
linestyles = ['-', '--', '-.', ':', '-', '--']
markerstyles = ['o', 's', 'D', '^', '*', '+']

boxes = ax.boxplot(park_sizes, patch_artist=True, notch=False, vert=True,
                   boxprops=dict(color='black', linewidth=1.5),
                   medianprops=dict(color='blue', linewidth=2),
                   whiskerprops=dict(color='green', linewidth=1.5),
                   capprops=dict(color='black', linewidth=1.5),
                   flierprops=dict(marker='x', color='orange', alpha=0.8, markersize=8))

for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for i, (data, marker) in enumerate(zip(park_sizes, markerstyles), start=1):
    y = np.array(data)
    x = np.random.normal(i, 0.05, size=len(y))
    ax.scatter(x, y, marker=marker, alpha=0.6, edgecolor='w', s=80, label=f'{districts[i-1]} Points' if i == 1 else "")

ax.set_title('Park Size Distribution 2023', fontsize=16, fontweight='bold')
ax.set_xlabel('Dist.', fontsize=12)
ax.set_ylabel('Size (Acres)', fontsize=12)
ax.set_xticks(np.arange(1, len(districts) + 1))
ax.set_xticklabels(districts, rotation=30, ha='right', fontsize=10)

ax.yaxis.grid(True, linestyle=':', which='major', color='black', alpha=0.3)

mean_sizes = [np.mean(d) for d in park_sizes]
for i, (mean, linestyle) in enumerate(zip(mean_sizes, linestyles), start=1):
    ax.axhline(mean, ls=linestyle, color=colors[i-1], alpha=0.7, linewidth=1.5, label=f'{districts[i-1]} Mean' if i == 1 else "")

ax.text(0.95, 0.02, "Equal green access.",
        transform=ax.transAxes, fontsize=10, verticalalignment='bottom', horizontalalignment='right',
        bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3))

plt.tight_layout()
ax.legend(loc='lower center', fontsize=9, ncol=3)

plt.show()