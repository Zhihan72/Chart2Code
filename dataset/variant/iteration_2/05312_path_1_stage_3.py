import matplotlib.pyplot as plt
import numpy as np

creatures = ['Sphinx', 'Goblin', 'Mermaid', 'Phoenix', 'Yeti']

scores = {
    'Sphinx': [95, 85, 90, 92, 85],
    'Goblin': [70, 95, 80, 60, 90],
    'Mermaid': [80, 60, 75, 85, 50],
    'Phoenix': [60, 85, 95, 70, 90],
    'Yeti': [75, 80, 70, 75, 85]
}

box_plot_data = [scores[creature] for creature in creatures]

fig, ax = plt.subplots(figsize=(14, 8))

# Shuffled colors for each data group
box_colors = ['lightcyan', 'lightgrey', 'lightgreen', 'lightblue', 'lightpink']

boxprops_list = [
    dict(linestyle='-', linewidth=2, color='darkblue', facecolor=color)
    for color in box_colors
]

ax.boxplot(box_plot_data, labels=creatures, patch_artist=True, vert=False,
           boxprops=boxprops_list[0], medianprops=dict(linestyle='-', linewidth=2, color='darkred'),
           whiskerprops=dict(linestyle='--', linewidth=1.5, color='darkblue'),
           capprops=dict(linestyle='-', linewidth=2, color='darkblue'),
           flierprops=dict(marker='o', color='darkgreen', markersize=5, alpha=0.5),
           notch=True,)

# Modify patch colors
for patch, color in zip(ax.artists, box_colors):
    patch.set_facecolor(color)

ax.set_title("Enchanted Lands Statistics:\nArcane Creature Evaluations", fontsize=16, fontweight='bold', loc='center')
ax.set_xlabel('Mystery Index (0-100)', fontsize=12)
ax.set_ylabel('Arcane Beings', fontsize=12)
ax.grid(axis='x', linestyle='--', alpha=0.7)

ax.annotate('Legendary Wisdom', xy=(scores['Sphinx'][3], 1), xytext=(scores['Sphinx'][3] + 5, 1.2),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='darkblue')
ax.annotate('Remarkable Dexterity', xy=(scores['Goblin'][4], 2), xytext=(scores['Goblin'][4] + 5, 2.2),
            arrowprops=dict(facecolor='gray', arrowstyle='->'), fontsize=10, color='darkgreen')

plt.tight_layout()
plt.show()