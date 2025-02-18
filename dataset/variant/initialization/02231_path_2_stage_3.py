import matplotlib.pyplot as plt
import numpy as np

ingredients = ['Dragon', 'Unicorn', 'Phoenix', 'Mandrake', 'Elven']
potencies = [
    [59, 51, 54, 50, 53, 56, 52, 55, 58, 52],  # Manually shuffled
    [80, 78, 77, 83, 75, 76, 82, 81, 78, 79],  # Manually shuffled
    [68, 65, 72, 71, 67, 68, 70, 66, 65, 69],  # Manually shuffled
    [45, 41, 40, 43, 42, 42, 44, 39, 40, 41],  # Manually shuffled
    [93, 95, 96, 91, 94, 97, 92, 90, 93, 95]   # Manually shuffled
]
average_potencies = [54, 79, 67, 43, 92]

fig, ax = plt.subplots(figsize=(12, 8))

boxes = ax.boxplot(potencies, patch_artist=True, notch=True, vert=True, showmeans=True)
single_color = '#99d8c9'

for patch in boxes['boxes']:
    patch.set_facecolor(single_color)

for mean_point in boxes['means']:
    mean_point.set(marker='o', markeredgecolor='black', markerfacecolor='white', markersize=7)

for median in boxes['medians']:
    median.set(color='darkblue', linewidth=2)

ax.plot(range(1, len(average_potencies) + 1), average_potencies, marker='s', linestyle='-', color='darkred', linewidth=2, label='Avg Potency')

ax.set_title('Potency Distribution & Avg Potency', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Ingredients', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Potency', fontsize=12, fontweight='bold', labelpad=10)
ax.set_xticks(range(1, len(ingredients) + 1))
ax.set_xticklabels(ingredients, fontsize=10, rotation=15, ha='right')
ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.legend([boxes['boxes'][0], mean_point, median, ax.get_lines()[0]], ['Range', 'Mean', 'Median', 'Avg Potency'],
          loc='upper left', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()