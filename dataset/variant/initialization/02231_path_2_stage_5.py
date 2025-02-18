import matplotlib.pyplot as plt
import numpy as np

ingredients = ['Dragon', 'Unicorn', 'Phoenix', 'Mandrake', 'Elven']
potencies = [
    [59, 51, 54, 50, 53, 56, 52, 55, 58, 52],
    [80, 78, 77, 83, 75, 76, 82, 81, 78, 79],
    [68, 65, 72, 71, 67, 68, 70, 66, 65, 69],
    [45, 41, 40, 43, 42, 42, 44, 39, 40, 41],
    [93, 95, 96, 91, 94, 97, 92, 90, 93, 95]
]
average_potencies = [54, 79, 67, 43, 92]

fig, ax = plt.subplots(figsize=(12, 8))

boxes = ax.boxplot(potencies, patch_artist=True, notch=False, vert=True, showmeans=False)
varied_colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

for i, patch in enumerate(boxes['boxes']):
    patch.set_facecolor(varied_colors[i])

for mean_point in boxes['means']:
    mean_point.set(marker='x', markeredgecolor='darkgreen', markerfacecolor='orange', markersize=8)

for median in boxes['medians']:
    median.set(color='red', linewidth=3)

ax.plot(average_potencies, range(1, len(average_potencies) + 1), marker='d', linestyle='--', color='blue', linewidth=3, label='Avg Potency')

ax.set_title('Ingredient Potency Analysis', fontsize=14, fontweight='normal', pad=15)
ax.set_ylabel('Magical Ingredients', fontsize=11, fontweight='normal', labelpad=8)
ax.set_xlabel('Measured Potency', fontsize=11, fontweight='normal', labelpad=8)

ax.set_yticks(range(1, len(ingredients) + 1))
ax.set_yticklabels(ingredients[::-1], fontsize=9, ha='left')
ax.grid(axis='y', linestyle='-.', alpha=0.5)

ax.legend(['Avg Potency', 'Median'], loc='upper center', fontsize=9, frameon=True)

plt.tight_layout()
plt.show()