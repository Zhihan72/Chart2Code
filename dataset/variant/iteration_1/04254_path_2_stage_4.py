import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
dwarf_planets = ['Pluto', 'Ceres', 'Eris', 'Haumea', 'Makemake']

missions = np.array([
    [2, 5, 10, 7, 3, 1, 0, 0, 0, 0, 0, 0, 0],   # Adding 5 data points for the new series
    [3, 6, 12, 9, 4, 2, 0, 0, 1, 0, 0, 0, 0],
    [4, 8, 15, 12, 6, 3, 1, 0, 1, 1, 0, 0, 0],
    [6, 12, 18, 15, 8, 4, 2, 1, 2, 1, 0, 0, 0],
    [10, 15, 20, 18, 12, 7, 4, 2, 3, 2, 1, 0, 0],
    [15, 20, 25, 22, 15, 10, 6, 4, 5, 3, 2, 1, 0],
    [20, 25, 30, 28, 18, 12, 8, 5, 8, 5, 3, 2, 1]
])

all_planets = planets + dwarf_planets

sorted_indices = np.argsort(-missions, axis=1)
sorted_missions = np.take_along_axis(missions, sorted_indices, axis=1)
sorted_planets = np.array([[all_planets[idx] for idx in row] for row in sorted_indices])

fig, ax = plt.subplots(figsize=(16, 9))

colors = ['#ffeb3b', '#4caf50', '#e91e63', '#a1887f', '#ce93d8', '#ff5722', '#03a9f4', '#9e9e9e', 
          '#ff9800', '#607d8b', '#33ff57', '#f4a460', '#9400d3']  # added colors for new series

bar_width = 0.09  # Reduced to fit the additional data
indices = np.arange(len(decades))

for i in range(missions.shape[1]):
    ax.bar(indices + i * bar_width, sorted_missions[:, i], bar_width, 
           label=[sorted_planets[j][i] for j in range(len(decades))][0], 
           edgecolor='grey', linestyle='--', hatch='x', color=colors[i])

ax.set_title('Space Missions to Planetary Bodies per Decade (Sorted & Expanded)', fontsize=18, fontweight='bold', color='darkblue')
ax.set_xlabel('Decades', fontsize=13, style='italic')
ax.set_ylabel('Missions Count', fontsize=13, style='italic')
ax.set_xticks(indices + 6 * bar_width)  # Adjusted for the number of series
ax.set_xticklabels(decades, rotation=45, ha='right')
ax.legend(title='Celestial Objects', bbox_to_anchor=(0.5, -0.2), loc='upper center', ncol=4, frameon=True)
ax.yaxis.grid(True, linestyle='--', linewidth=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i in range(len(decades)):
    for j in range(len(all_planets)):
        ax.text(i + j * bar_width, sorted_missions[i, j] + 0.5, 
                f'{sorted_missions[i, j]}', ha='center', va='bottom', 
                fontsize=9, color='purple', rotation=45)

plt.tight_layout()
plt.show()