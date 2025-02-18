import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Carrots', 'Potatoes', 'Tomatoes']
soil_types = ['Clay', 'Loamy', 'Sandy']

carrots_yield = [
    [1.3, 1.5, 1.6, 1.8, 1.4],  # Clay
    [2.0, 2.2, 2.1, 2.3, 2.4],  # Loamy
    [1.0, 1.2, 1.1, 1.3, 1.2]   # Sandy
]

potatoes_yield = [
    [3.0, 3.2, 3.3, 3.4, 3.1],  # Clay
    [4.0, 4.2, 4.1, 4.3, 4.4],  # Loamy
    [2.5, 2.7, 2.6, 2.8, 2.7]   # Sandy
]

tomatoes_yield = [
    [5.0, 5.3, 5.1, 5.4, 5.2],  # Clay
    [6.0, 6.3, 6.1, 6.4, 6.2],  # Loamy
    [4.0, 4.2, 4.1, 4.3, 4.2]   # Sandy
]

data = [carrots_yield, potatoes_yield, tomatoes_yield]

fig, ax = plt.subplots(figsize=(14, 8))
positions = np.array(range(len(soil_types))) * 4

for i, yields in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=True)

    # Shuffled colors for each vegetable type
    colors = ['#99ff99', '#ff9999', '#66b3ff']  # Shuffled order
    for patch, color in zip(bp['boxes'], [colors[i]] * len(soil_types)):
        patch.set_facecolor(color)

    for whisker in bp['whiskers']:
        whisker.set(color='gray', linewidth=1.5)
    for cap in bp['caps']:
        cap.set(color='gray', linewidth=1.5)
    for median in bp['medians']:
        median.set(color='black', linewidth=2)

ax.set_xticks(positions + 1)
ax.set_xticklabels(soil_types, fontsize=12)

ax.set_title("Impact of Soil Types on Vegetable Yield:\nAnalysis of Carrot, Potato, and Tomato Yields", fontsize=16, fontweight='bold')
ax.set_ylabel("Yield (kg per plant)", fontsize=14)
ax.set_xlabel("Soil Types", fontsize=14)

ax.grid(axis='y', linestyle='--', alpha=0.7)

handles = [plt.Line2D([0], [0], color=color, lw=4) for color in colors]
ax.legend(handles, vegetables, title='Vegetable Types', loc='upper left', fontsize=12)

plt.tight_layout()
plt.show()