import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Peppers', 'Carrots', 'Cucumbers', 'Tomatoes']
yields = {
    'Tomatoes': [15, 20, 22, 18, 25, 30, 35, 24, 28, 23, 19, 29, 31, 27, 21],
    'Cucumbers': [10, 15, 12, 18, 11, 17, 14, 20, 21, 16, 13, 19, 22, 10, 18],
    'Carrots': [9, 11, 13, 15, 14, 12, 10, 16, 18, 11, 14, 15, 17, 19, 12],
    'Peppers': [6, 8, 7, 11, 9, 12, 13, 10, 14, 12, 11, 9, 8, 13, 7]
}

data = [yields[veg] for veg in vegetables]
average_yields = [np.mean(yields[veg]) for veg in vegetables]

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(data, patch_artist=True, labels=vegetables, notch=True, widths=0.6, vert=False)

shuffled_colors = ['#F08080', '#FFDEAD', '#9370DB', '#ADFF2F']
for patch, color in zip(box['boxes'], shuffled_colors):
    patch.set_facecolor(color)
for whisker in box['whiskers']:
    whisker.set(color='black', linestyle='-', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
for median in box['medians']:
    median.set(color='red', linewidth=2)
for flier in box['fliers']:
    flier.set(markerfacecolor='orange', marker='o', markersize=6)

ax.scatter(average_yields, range(1, len(vegetables) + 1), color='blue', s=100, zorder=3, label='Average Yield')

ax.set_title('Urban Garden Fresh Initiative\nYields Distribution of Vegetables (in kg)', fontsize=16, fontweight='bold')
ax.set_ylabel('Types of Vegetables', fontsize=12)
ax.set_xlabel('Yields (Kg)', fontsize=12)

ax.xaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
ax.set_axisbelow(True)

color_patches = [plt.Line2D([0], [0], color=color, lw=4) for color in shuffled_colors]
ax.legend(color_patches + [plt.Line2D([0], [0], color='blue', marker='o', lw=0, markersize=10)],
          vegetables + ['Average Yield'], title='Legend', loc='upper left', fontsize=10, frameon=True)

plt.tight_layout()
plt.show()