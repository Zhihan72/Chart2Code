import matplotlib.pyplot as plt
import numpy as np

bodies = ['Mars', 'Europa', 'Titan', 'Ganymede', 'Callisto', 'Mercury', 'Venus', 'Phobos', 'Deimos', 'Enceladus']
distances = np.array([225, 628, 1221, 1070, 1182, 77, 42, 78, 76, 583])
colonization_time = np.array([20, 40, 50, 60, 70, 30, 10, 15, 25, 45])

fig, ax = plt.subplots(figsize=(14, 9))
ax.barh(bodies, distances, color='royalblue', alpha=0.7, edgecolor='w')

ax.set_title('Distance to Celestial Bodies', fontsize=16)
ax.set_xlabel('Distance (Million km)', fontsize=12)
ax.set_ylabel('Celestial Bodies', fontsize=12)

plt.tight_layout()
plt.show()