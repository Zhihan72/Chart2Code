import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cities = ['New York', 'London', 'Tokyo']
years = np.array(['2018', '2019', '2020', '2021', '2022'])

data = np.array([
    [[30, 25, 40], [35, 28, 38], [38, 30, 35], [40, 32, 32], [42, 34, 30]],
    [[20, 18, 22], [22, 20, 24], [24, 22, 26], [26, 24, 28], [28, 26, 30]],
    [[15, 10, 12], [16, 11, 14], [18, 13, 16], [20, 15, 18], [22, 17, 20]],
])

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

x_pos = np.arange(len(years))
y_pos = np.arange(len(cities))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.ravel()
y_pos = y_pos.ravel()
z_pos = np.zeros_like(x_pos)

# New set of colors
colors = ['#3498db', '#f39c12', '#2ecc71']

for plant_idx in range(len(data)):
    dz = data[plant_idx].reshape(-1)
    ax.bar3d(x_pos, y_pos, z_pos, dx=0.5, dy=0.5, dz=dz, color=colors[plant_idx], alpha=0.8)
    z_pos += dz

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

ax.view_init(elev=25, azim=-60)
plt.tight_layout()
plt.show()