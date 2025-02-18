import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data
decades = np.array([1970, 1980, 1990])
civilizations = ['Meso', 'Indus', 'Maya']
artifacts_data = np.array([
    [650, 700, 800],
    [450, 500, 600],
    [350, 600, 750]
])
colors = ['#8D8741', '#659DBD', '#DAAD86']

# Plot
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

for i in range(len(civilizations)):
    xs = decades
    ys = np.full(xs.shape, i * 3)
    zs = np.zeros(decades.shape)

    for j, color in enumerate(colors):
        height = artifacts_data[i, j]
        ax.bar3d(xs[j], ys[j], zs[j], dx=8, dy=0.8, dz=height, color=color, alpha=0.8)
        zs[j] += height

# Labels on axes
ax.set_xlabel('Dec', fontsize=12, labelpad=10)
ax.set_ylabel('Civ', fontsize=12, labelpad=10)
ax.set_zlabel('Artifacts', fontsize=12, labelpad=10)
ax.set_yticks([i * 3 for i in range(len(civilizations))])
ax.set_yticklabels(civilizations)

# Removing stylistic elements: legends, grids, and the outer border
ax.grid(False)

plt.show()