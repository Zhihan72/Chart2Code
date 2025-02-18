import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

planets = ['Zog', 'Vega', 'Orion']
cuisines = ['Martian Delicacies', 'Venusian Pastries', 'Saturnine Savories']
popularity_scores = np.array([
    [70, 85, 90],
    [60, 75, 95],
    [80, 65, 70]
])

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

xpos, ypos = np.meshgrid(np.arange(len(planets)), np.arange(len(cuisines)), indexing="ij")
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)

dx = dy = 0.6
dz = popularity_scores.flatten()

colors = plt.cm.viridis(np.linspace(0, 1, len(cuisines)))

for i, (_, score_row) in enumerate(zip(planets, popularity_scores)):
    ax.bar3d(xpos[i::len(planets)], ypos[i::len(planets)], zpos[i::len(planets)], dx, dy, score_row, color=colors, alpha=0.8)

ax.set_xticks(np.arange(len(planets)))
ax.set_yticks(np.arange(len(cuisines)))
ax.set_xticklabels(planets)
ax.set_yticklabels(cuisines, rotation=45, ha='right')
ax.set_xlabel('Planets')
ax.set_ylabel('Cuisines')
ax.set_zlabel('Popularity Score (0 - 100)')

ax.view_init(elev=20, azim=130)

plt.show()