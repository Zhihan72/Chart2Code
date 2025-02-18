import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

distances = np.array([225, 628, 1221, 1070, 1182, 77, 42])
colonization_time = np.array([20, 40, 50, 60, 70, 30, 10])
population_capacity = np.array([10, 5, 15, 8, 7, 3, 12])
tech_readiness = np.array([8, 5, 6, 4, 3, 7, 9])

# Normalize colors based on technological readiness
colors = tech_readiness / tech_readiness.max()

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Bubble plot with the updated colormap 'viridis'
sc = ax.scatter(distances, colonization_time, tech_readiness,
                s=population_capacity*50, c=colors, cmap='viridis', alpha=0.7, edgecolors='w')

ax.view_init(elev=30, azim=120)
plt.tight_layout()
plt.show()