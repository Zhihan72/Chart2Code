import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
missions = np.array([
    [2, 5, 10, 7, 3, 1, 0, 0],
    [3, 6, 12, 9, 4, 2, 0, 0],
    [4, 8, 15, 12, 6, 3, 1, 0],
    [6, 12, 18, 15, 8, 4, 2, 1],
    [10, 15, 20, 18, 12, 7, 4, 2],
    [15, 20, 25, 22, 15, 10, 6, 4],
    [20, 25, 30, 28, 18, 12, 8, 5]
])

fig, ax = plt.subplots(figsize=(16, 9))
colors = ['#d32f2f', '#f57c00', '#fbc02d', '#388e3c', '#1976d2', '#7b1fa2', '#5d4037', '#607d8b']
bar_height = 0.10
indices = np.arange(len(planets))

for i, decade in enumerate(decades):
    ax.barh(indices + i * bar_height, missions[i], bar_height, color=colors[i % len(colors)])

ax.set_title('Interstellar Exploration Missions per Decade per Planet', fontsize=20, fontweight='bold')
ax.set_xlabel('Number of Missions', fontsize=15)
ax.set_ylabel('Planets', fontsize=15)
ax.set_yticks(indices + 3.5 * bar_height)
ax.set_yticklabels(planets)

for i in range(len(planets)):
    for j in range(len(decades)):
        ax.text(missions[j, i] + 0.5, i + j * bar_height, f'{missions[j, i]}', va='center', ha='left', fontsize=10, color='black')

ax.set_frame_on(False)  # Remove plot borders

plt.tight_layout()
plt.show()