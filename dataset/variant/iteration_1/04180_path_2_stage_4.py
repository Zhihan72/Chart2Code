import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Carrots', 'Potatoes', 'Tomatoes']
soil_types = ['Clay', 'Loamy', 'Sandy']

# Alter contents within data groups
carrots_yield = [
    [1.7, 1.2, 1.5, 1.8, 1.3],  # shuffled within group
    [2.3, 2.0, 2.2, 2.4, 2.1],  # shuffled within group
    [1.1, 1.3, 1.2, 1.0, 1.2]   # shuffled within group
]

potatoes_yield = [
    [3.4, 3.2, 3.3, 3.1, 3.0],  # shuffled within group
    [4.1, 4.2, 4.0, 4.4, 4.3],  # shuffled within group
    [2.7, 2.5, 2.6, 2.8, 2.7]   # within the same group, similar shuffle
]

tomatoes_yield = [
    [5.3, 5.0, 5.1, 5.4, 5.2],  # shuffled within group
    [6.1, 6.3, 6.0, 6.4, 6.2],  # shuffled within group
    [4.2, 4.1, 4.0, 4.3, 4.2]   # shuffled within group
]

data = [carrots_yield, potatoes_yield, tomatoes_yield]

fig, ax = plt.subplots(figsize=(14, 8))

positions = np.array(range(len(vegetables))) * 4

for yields, soil, linestyle, marker in zip(zip(*data), soil_types, ['-', '--', '-.'], ['o', 's', '^']):
    pos = positions + list(zip(*data)).index(yields)
    
    # Transpose the yields data to make horizontal boxes
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=False, vert=False)

    # Shuffling and fixed colors/linestyles
    for patch in bp['boxes']:
        patch.set_facecolor('lightblue')
    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1, linestyle=linestyle)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1)
    for median in bp['medians']:
        median.set(color='black', linewidth=2, linestyle=linestyle)

ax.set_yticks(positions + 1)
ax.set_yticklabels(vegetables, fontsize=12)

ax.set_title("Impact of Soil Types on Vegetable Yield:\nAnalysis of Carrot, Potato, and Tomato Yields", fontsize=16, fontweight='bold')
ax.set_xlabel("Yield (kg per plant)", fontsize=14)
ax.set_ylabel("Vegetable Types", fontsize=14)

ax.grid(axis='x', linestyle=':', alpha=0.5)

# Add back legend with shuffled positions and markers
for soil, marker in zip(soil_types, ['o', 's', '^']):
    ax.plot([], [], label=soil, marker=marker, linestyle='None')
ax.legend(title='Soil Types', loc='upper right', fontsize=12)

for spine in ax.spines.values():
    spine.set_linestyle('dotted')

plt.tight_layout()

plt.show()