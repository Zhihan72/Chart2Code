import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define cities and plant types
cities = ['NY', 'LDN', 'TYO']
plant_types = ['Tree', 'Shrub', 'Flower']
years = np.array(['2018', '2019', '2020', '2021', '2022'])

# Data: Number of plants planted
data = np.array([
    [[30, 25, 40], [35, 28, 38], [38, 30, 35], [40, 32, 32], [42, 34, 30]],
    [[20, 18, 22], [22, 20, 24], [24, 22, 26], [26, 24, 28], [28, 26, 30]],
    [[15, 10, 12], [16, 11, 14], [18, 13, 16], [20, 15, 18], [22, 17, 20]],
])

# Initialize figure and 3D axis
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Define positions for bars
x_pos = np.arange(len(years))
y_pos = np.arange(len(cities))
x_pos, y_pos = np.meshgrid(x_pos, y_pos)
x_pos = x_pos.ravel()
y_pos = y_pos.ravel()
z_pos = np.zeros_like(x_pos)

# Colors for plant types
colors = ['#8bc34a', '#ff9800', '#e91e63']

# Plot each plant type
for plant_idx, plant_type in enumerate(plant_types):
    dz = data[plant_idx].reshape(-1)
    ax.bar3d(x_pos, y_pos, z_pos, dx=0.5, dy=0.5, dz=dz, color=colors[plant_idx], alpha=0.8, label=plant_type)
    z_pos += dz

# Axes labels
ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(cities)))
ax.set_yticklabels(cities, fontsize=10)
ax.set_xlabel('Yr', labelpad=10)
ax.set_ylabel('City', labelpad=10)
ax.set_zlabel('Plants (k)', labelpad=10)

# Title and legend
ax.set_title('Urban Greenery\n3D Plant Analysis', pad=30, fontsize=14, weight='bold')
ax.legend(title='Plants', loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Set view angle
ax.view_init(elev=25, azim=-60)

# Adjust layout
plt.tight_layout()

# Display plot
plt.show()