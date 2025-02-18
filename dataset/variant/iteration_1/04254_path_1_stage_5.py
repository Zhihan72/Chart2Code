import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pandora']
missions = np.array([
    [2, 5, 10, 7, 3, 1, 0, 0, 1],
    [3, 6, 12, 9, 4, 2, 0, 0, 2],
    [4, 8, 15, 12, 6, 3, 1, 0, 3],
    [6, 12, 18, 15, 8, 4, 2, 1, 4],
    [10, 15, 20, 18, 12, 7, 4, 2, 5],
    [15, 20, 25, 22, 15, 10, 6, 4, 7],
    [20, 25, 30, 28, 18, 12, 8, 5, 9]
])

fig, ax = plt.subplots(figsize=(16, 9))
single_color = '#1976d2'
bar_height = 0.10
indices = np.arange(len(planets))

for i in range(len(decades)):
    ax.barh(indices + i * bar_height, missions[i], bar_height, color=single_color)

ax.set_yticks(indices + 3.5 * bar_height)
ax.set_yticklabels([])  # Remove y-axis labels

ax.set_frame_on(False)

plt.tight_layout()
plt.show()