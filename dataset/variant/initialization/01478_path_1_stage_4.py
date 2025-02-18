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

# New set of colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

fig = plt.figure(figsize=(10, 12))
ax = fig.add_subplot(111, projection='3d')

for i, region in enumerate(regions):
    xs = np.repeat(years, market_share_data.shape[1])
    ys = np.full(xs.shape, i * 5)
    zs = np.zeros(years.shape)

    for j, color in enumerate(colors):
        height = market_share_data[:, j]
        ax.bar3d(xs[j::3], ys[j::3], zs, dx=0.7, dy=0.7, dz=height, color=color, alpha=0.9, linestyle='--')
        zs += height

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.view_init(elev=30, azim=145)

plt.tight_layout()

plt.show()