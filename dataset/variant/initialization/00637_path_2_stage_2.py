import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

bodies = ['Mars', 'Europa', 'Titan', 'Ganymede', 'Callisto', 'Mercury', 'Venus', 'Phobos', 'Deimos', 'Enceladus']
distances = np.array([225, 628, 1221, 1070, 1182, 77, 42, 78, 76, 583])
colonization_time = np.array([20, 40, 50, 60, 70, 30, 10, 15, 25, 45])
population_capacity = np.array([10, 5, 15, 8, 7, 3, 12, 6, 4, 9])
tech_readiness = np.array([8, 5, 6, 4, 3, 7, 9, 6, 4, 5])

colors = tech_readiness / tech_readiness.max()

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(distances, colonization_time, tech_readiness,
                s=population_capacity * 50, c=colors, cmap='plasma', alpha=0.7, edgecolors='w')

ax.view_init(elev=30, azim=120)

ax.set_title('Celestial Bodies for Colonization', fontsize=16, pad=20)
ax.set_xlabel('Dist. (Mil km)', fontsize=12, labelpad=10)
ax.set_ylabel('Time (Yrs)', fontsize=12, labelpad=10)
ax.set_zlabel('Readiness (1-10)', fontsize=12, labelpad=10)

for i, body in enumerate(bodies):
    ax.text(distances[i], colonization_time[i], tech_readiness[i] + 0.5, body, fontsize=9)

cbar = plt.colorbar(sc, ax=ax, pad=0.1)
cbar.set_label('Tech Readiness', fontsize=12)

pop_sizes = [3, 5, 10, 15]
pop_labels = [plt.Line2D([0], [0], marker='o', color='w', label=f'{v}M',
                         markerfacecolor='gray', markersize=np.sqrt(v * 50), alpha=0.5)
              for v in pop_sizes]
ax.legend(title='Pop. Cap.', handles=pop_labels, loc='upper right', fontsize=9)

plt.tight_layout()
plt.show()