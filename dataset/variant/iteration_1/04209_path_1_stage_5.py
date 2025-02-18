import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Vitamins', 'Minerals', 'Proteins', 'Fibers', 'Sugars', 'Calories']
num_vars = len(categories)

fruit_scores = {
    'Apple': [7, 6, 2, 3, 5, 4],
    'Orange': [8, 5, 2, 3, 6, 3],
    'Banana': [6, 7, 3, 2, 4, 5],
    'Strawberry': [9, 6, 2, 3, 4, 2],
    'Pineapple': [7, 5, 2, 3, 6, 4],
    'Mango': [8, 6, 3, 2, 5, 3],
    'Blueberry': [9, 7, 4, 3, 3, 2],
    'Kiwi': [8, 5, 3, 4, 6, 3]
}

fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(polar=True))
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

new_colors = ['#1E90FF', '#228B22', '#8A2BE2', '#DAA520', '#DC143C', '#00CED1', '#FF69B4', '#8B4513']
markers = ['o', 'v', '^', '<', '>', 's', 'p', '*']
linestyles = ['-', '--', '-.', ':']

for idx, (fruit, scores) in enumerate(fruit_scores.items()):
    scores += scores[:1]
    ax.plot(angles, scores, 
            label=fruit, 
            color=new_colors[idx], 
            marker=markers[idx % len(markers)], 
            linestyle=linestyles[idx % len(linestyles)] )
    ax.fill(angles, scores, alpha=0.15, color=new_colors[idx])

ax.legend(loc='upper right', fontsize=12, frameon=False)
ax.set_yticklabels([])
ax.set_rlabel_position(0)
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()