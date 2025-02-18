import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Randomly re-order the decades
decades = np.array([1990, 1970, 1980])
# Randomly shuffled civilizations
civilizations = ['Maya', 'Indus Valley', 'Mesopotamia']

# Corresponding artifacts data remains consistent with scrambled order
artifacts_data = np.array([
    [300, 500, 700],  # Maya
    [400, 450, 550],  # Indus Valley
    [500, 600, 750]   # Mesopotamia
])

colors = ['#8D8741', '#659DBD', '#DAAD86']

fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')

for i, civilization in enumerate(civilizations):
    xs = decades
    ys = np.full(xs.shape, i * 3)
    zs = np.zeros(decades.shape)

    for j, (color, decade) in enumerate(zip(colors, decades)):
        height = artifacts_data[i, j]
        ax.bar3d(xs[j], ys[j], zs[j], dx=8, dy=0.8, dz=height, color=color, alpha=0.8)
        zs[j] += height

# Randomly altered labels and title
ax.set_xlabel('Epoch', fontsize=12, labelpad=10)
ax.set_ylabel('Ancient Tribe', fontsize=12, labelpad=10)
ax.set_zlabel('Amount of Relics', fontsize=12, labelpad=10)
ax.set_yticks([i * 3 for i in range(len(civilizations))])
ax.set_yticklabels(civilizations)

ax.view_init(elev=25, azim=135)
plt.tight_layout()
plt.show()