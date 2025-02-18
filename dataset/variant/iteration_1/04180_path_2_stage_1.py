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
for yields in data:
    pos = positions + data.index(yields)
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=True)

    # Apply a single consistent color to all data groups
    consistent_color = '#ffa500'  # Orange for all boxes
    for patch in bp['boxes']:
        patch.set_facecolor(consistent_color)

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

# Legend indicating vegetable types - not needed anymore as the color is consistent
# handles = [plt.Line2D([0], [0], color=consistent_color, lw=4)]  # Single color for legend (but we're removing it)
# ax.legend(handles, vegetables, title='Vegetable Types', loc='upper left', fontsize=12)

plt.tight_layout()

plt.show()