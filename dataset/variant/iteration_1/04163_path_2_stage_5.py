import numpy as np
import matplotlib.pyplot as plt

categories = ['Temperature', 'Humidity', 'Visibility', 'Air Quality', 'Traffic']
bike = [8, 5, 7, 6, 8]
bus = [7, 6, 5, 7, 5]
car = [9, 4, 8, 5, 9]
walking = [6, 5, 6, 7, 6]

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
bike += bike[:1]
bus += bus[:1]
car += car[:1]
walking += walking[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

color = 'blue'  # Single color for all data groups

ax.fill(angles, bike, color=color, alpha=0.3)
ax.fill(angles, bus, color=color, alpha=0.3)
ax.fill(angles, car, color=color, alpha=0.3)
ax.fill(angles, walking, color=color, alpha=0.3)

ax.plot(angles, bike, linestyle='--', color=color, linewidth=1.5, marker='o')
ax.plot(angles, bus, linestyle='-.', color=color, linewidth=1.5, marker='x')
ax.plot(angles, car, linestyle=':', color=color, linewidth=1.5, marker='s')
ax.plot(angles, walking, linestyle='-', color=color, linewidth=1.5, marker='d')

ax.set_yticklabels([])
ax.set_xticks([])
plt.legend(loc='upper left', bbox_to_anchor=(0.9, 0.9))

ax.grid(color='gray', linestyle='dashed')

plt.tight_layout()
plt.show()