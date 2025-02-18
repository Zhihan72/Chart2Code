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

# Changed colors
colors = ['#e91e63', '#ce93d8', '#ffeb3b', '#4caf50', '#03a9f4', '#ff5722', '#a1887f', '#9e9e9e']

# Changed bar width
bar_width = 0.12

indices = np.arange(len(decades))

for i, planet in enumerate(planets):
    # Changed line style and marker
    ax.bar(indices + i * bar_width, missions[:, i], bar_width, label=planet, 
           edgecolor='grey', linestyle='--', hatch='x', color=colors[i])

# Changed title and labels
ax.set_title('Space Missions to Planets per Decade', fontsize=18, fontweight='bold', color='darkblue')
ax.set_xlabel('Decades', fontsize=13, style='italic')
ax.set_ylabel('Missions Count', fontsize=13, style='italic')
ax.set_xticks(indices + 3.5 * bar_width)
ax.set_xticklabels(decades, rotation=45, ha='right')

# Changed legend location and added frame
ax.legend(title='Planetary Worlds', bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=4, frameon=True)

# Added grid and changed annotation style
ax.yaxis.grid(True, linestyle='--', linewidth=0.7)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

for i in range(len(decades)):
    for j in range(len(planets)):
        ax.text(i + j * bar_width, missions[i, j] + 0.5, 
                f'{missions[i, j]}', ha='center', va='bottom', fontsize=9, color='purple', rotation=45)

plt.tight_layout()
plt.show()