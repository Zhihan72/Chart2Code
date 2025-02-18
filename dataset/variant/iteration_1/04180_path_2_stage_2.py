import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Carrots', 'Potatoes', 'Tomatoes']
soil_types = ['Clay', 'Loamy', 'Sandy']

carrots_yield = [
    [1.3, 1.5, 1.6, 1.8, 1.4],
    [2.0, 2.2, 2.1, 2.3, 2.4],
    [1.0, 1.2, 1.1, 1.3, 1.2]
]

potatoes_yield = [
    [3.0, 3.2, 3.3, 3.4, 3.1],
    [4.0, 4.2, 4.1, 4.3, 4.4],
    [2.5, 2.7, 2.6, 2.8, 2.7]
]

tomatoes_yield = [
    [5.0, 5.3, 5.1, 5.4, 5.2],
    [6.0, 6.3, 6.1, 6.4, 6.2],
    [4.0, 4.2, 4.1, 4.3, 4.2]
]

data = [carrots_yield, potatoes_yield, tomatoes_yield]

fig, ax = plt.subplots(figsize=(14, 8))

positions = np.array(range(len(soil_types))) * 4
for yields, veg, marker, linestyle in zip(data, vegetables, ['o', 's', '^'], ['-', '--', '-.']):
    pos = positions + data.index(yields)
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=False)

    for patch in bp['boxes']:
        patch.set_facecolor(np.random.rand(3,))  # Random colors

    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1, linestyle=linestyle)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1)
    for median in bp['medians']:
        median.set(color='black', linewidth=2, linestyle=linestyle)

ax.set_xticks(positions + 1)
ax.set_xticklabels(soil_types, fontsize=12)

ax.set_title("Impact of Soil Types on Vegetable Yield:\nAnalysis of Carrot, Potato, and Tomato Yields", fontsize=16, fontweight='bold')
ax.set_ylabel("Yield (kg per plant)", fontsize=14)
ax.set_xlabel("Soil Types", fontsize=14)

# Randomly decide grid visibility and line style
ax.grid(axis='y', linestyle=':', alpha=0.5)

# Add back legend with random positions and markers
for veg, marker in zip(vegetables, ['o', 's', '^']):
    ax.plot([], [], label=veg, marker=marker, linestyle='None')
ax.legend(title='Vegetable Types', loc='upper right', fontsize=12)

# Random linestyle for axes
for spine in ax.spines.values():
    spine.set_linestyle('dotted')

plt.tight_layout()

plt.show()