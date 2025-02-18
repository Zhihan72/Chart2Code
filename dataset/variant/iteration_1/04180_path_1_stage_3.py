import matplotlib.pyplot as plt
import numpy as np

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
positions = np.array(range(3)) * 4

for i, yields in enumerate(data):
    pos = positions + i
    bp = ax.boxplot(yields, positions=pos, widths=0.6, patch_artist=True, notch=True)
    
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    for patch, color in zip(bp['boxes'], [colors[i]] * 3):
        patch.set_facecolor(color)
        patch.set_edgecolor('blue')

    for whisker in bp['whiskers']:
        whisker.set(color='purple', linewidth=1.0, linestyle='-.')
    for cap in bp['caps']:
        cap.set(color='purple', linewidth=1.0, linestyle=':')
    for median in bp['medians']:
        median.set(color='orange', linewidth=3)

ax.set_xticks(positions + 1)
ax.set_xticklabels([''] * 3, fontsize=12)

ax.grid(axis='y', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()