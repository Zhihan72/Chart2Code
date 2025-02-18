import matplotlib.pyplot as plt
import numpy as np

vegetables = ['RootVeg', 'Tubers', 'Fruits']
soil_types = ['Thick', 'Rich', 'Grainy']

carrots_yield = [
    [1.7, 1.2, 1.5, 1.8, 1.3],
    [2.3, 2.0, 2.2, 2.4, 2.1],
    [1.1, 1.3, 1.2, 1.0, 1.2]
]

potatoes_yield = [
    [3.4, 3.2, 3.3, 3.1, 3.0],
    [4.1, 4.2, 4.0, 4.4, 4.3],
    [2.7, 2.5, 2.6, 2.8, 2.7]
]

tomatoes_yield = [
    [5.3, 5.0, 5.1, 5.4, 5.2],
    [6.1, 6.3, 6.0, 6.4, 6.2],
    [4.2, 4.1, 4.0, 4.3, 4.2]
]

data = [carrots_yield, potatoes_yield, tomatoes_yield]

fig, ax = plt.subplots(figsize=(14, 8))

positions = np.array(range(len(vegetables))) * 4

for yields, soil, linestyle, marker in zip(zip(*data), soil_types, ['-', '--', '-.'], ['o', 's', '^']):
    pos = positions + list(zip(*data)).index(yields)
    
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=False, vert=False)

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

ax.set_title("Soil Variety Effects on Plant Yield:\nRoots, Tubers, and Fruits Comparison", fontsize=16, fontweight='bold')
ax.set_xlabel("Yield (mass per unit)", fontsize=14)
ax.set_ylabel("Plant Categories", fontsize=14)

ax.grid(axis='x', linestyle=':', alpha=0.5)

for soil, marker in zip(soil_types, ['o', 's', '^']):
    ax.plot([], [], label=soil, marker=marker, linestyle='None')
ax.legend(title='Ground Types', loc='upper right', fontsize=12)

for spine in ax.spines.values():
    spine.set_linestyle('dotted')

plt.tight_layout()

plt.show()