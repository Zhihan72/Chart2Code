import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
continents = ['North America', 'South America', 'Europe', 'Asia', 'Africa']
consumption = np.array([
    [28, 29, 30, 31, 33, 34],
    [45, 46, 47, 49, 50, 52],
    [50, 52, 54, 57, 59, 60],
    [18, 19, 21, 23, 24, 25],
    [8, 9, 10, 11, 12, 13],
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

_x, _y = np.meshgrid(np.arange(len(years)), np.arange(len(continents)))
x, y = _x.flatten(), _y.flatten()
z = np.zeros_like(x)
dx = dy = 0.4
dz = consumption.flatten()

colors = ['#8B4513', '#DEB887', '#D2691E', '#CD853F', '#F4A460']

for i in range(len(continents)):
    ax.bar3d(x[y == i], y[y == i], z[y == i], dx, dy, dz[y == i], color=colors[i], alpha=0.8)

# Remove labels, ticks, and legend
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.view_init(elev=20, azim=120)
plt.tight_layout()
plt.show()