import matplotlib.pyplot as plt
import numpy as np

ingredients = ['Dragon', 'Unicorn', 'Phoenix', 'Mandrake', 'Elven']
potencies = [
    [50, 55, 53, 52, 51, 56, 54, 58, 52, 59],
    [75, 78, 77, 80, 79, 76, 81, 82, 83, 78],
    [65, 68, 70, 67, 66, 69, 71, 72, 65, 68],
    [40, 42, 41, 43, 39, 44, 40, 45, 42, 41],
    [90, 95, 92, 93, 91, 96, 94, 97, 93, 95]
]
average_potencies = [54, 79, 67, 43, 92]

fig, ax = plt.subplots(figsize=(12, 8))

# Use a single color for all box plots
boxes = ax.boxplot(potencies, patch_artist=True, notch=True, vert=True, showmeans=True)
single_color = '#99d8c9'  # Selected single color

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

# Adjust the legend to represent the single color used
ax.legend([boxes['boxes'][0], mean_point, median, ax.get_lines()[0]], ['Range', 'Mean', 'Median', 'Avg Potency'],
          loc='upper left', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()