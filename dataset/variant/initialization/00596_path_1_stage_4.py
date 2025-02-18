import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

years = np.array([2015, 2016, 2017, 2018, 2019, 2020])
continents = ['N. America', 'S. America', 'Europe', 'Asia']
consumption = np.array([
    [28, 29, 30, 31, 33, 34],
    [45, 46, 47, 49, 50, 52],
    [50, 52, 54, 57, 59, 60],
    [18, 19, 21, 23, 24, 25],
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

_x, _y = np.meshgrid(np.arange(len(years)), np.arange(len(continents)))
x, y = _x.flatten(), _y.flatten()
z = np.zeros_like(x)
dx = dy = 0.4
dz = consumption.flatten()

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

for i in range(len(continents)):
    ax.bar3d(x[y == i], y[y == i], z[y == i], dx, dy, dz[y == i], color=colors[i], alpha=0.8)

ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Continent', labelpad=10)
ax.set_zlabel('Consumption\n(Million Bags)', labelpad=10)

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(continents)))
ax.set_yticklabels(continents)

ax.view_init(elev=20, azim=120)
ax.set_title('Coffee Consumption\n(2015-2020)', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()