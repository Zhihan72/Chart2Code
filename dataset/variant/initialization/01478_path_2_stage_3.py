import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

years = np.arange(2025, 2036)
regions = ['Flavorland', 'New Aroma City', 'Taste Haven']

market_share_data = np.array([
    [30, 20, 25],
    [32, 19, 27],
    [34, 18, 28],
    [36, 17, 29],
    [38, 16, 30],
    [39, 15, 31],
    [40, 15, 32],
    [41, 14, 33],
    [42, 13, 34],
    [43, 12, 35],
    [44, 11, 36]
])

colors = ['#FF6F61', '#6B5B95', '#88B04B']  # Citrus, Berry, Exotic

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

for i, region in enumerate(regions):
    xs = np.repeat(years, market_share_data.shape[1])
    ys = np.full(xs.shape, i * 5)
    zs = np.zeros(years.shape)

    for j, (color, label) in enumerate(zip(colors, ['Citrus', 'Berry', 'Exotic'])):
        height = market_share_data[:, j]
        ax.bar3d(xs[j::3], ys[j::3], zs, dx=0.7, dy=0.7, dz=height, color=color, alpha=0.7, label=label if i == 0 else "")
        zs += height

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Region', fontsize=12)
ax.set_zlabel('Market Share (%)', fontsize=12)
ax.set_yticks([i * 5 for i in range(len(regions))])
ax.set_yticklabels(regions, fontstyle='italic')

# Alter view angle
ax.view_init(elev=20, azim=120)

# Adding grid and border modifications
ax.grid(True, linestyle='--', linewidth=0.6)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[:3], labels[:3], loc='lower right', fontsize=10)

plt.title('Market Share of Beverage Flavors\nin Future Markets (2025-2035)', fontsize=14, pad=10, weight='bold')

plt.show()