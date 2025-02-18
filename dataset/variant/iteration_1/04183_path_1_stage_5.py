import matplotlib.pyplot as plt
import numpy as np

vegetables = ['Tomatoes', 'Carrots', 'Peppers', 'Zucchinis']
yields = {
    'Tomatoes': [15, 20, 22, 18, 25, 30, 35, 24, 28, 23, 19, 29, 31, 27, 21],
    'Carrots': [9, 11, 13, 15, 14, 12, 10, 16, 18, 11, 14, 15, 17, 19, 12],
    'Peppers': [6, 8, 7, 11, 9, 12, 13, 10, 14, 12, 11, 9, 8, 13, 7],
    'Zucchinis': [20, 22, 24, 26, 28, 30, 25, 27, 23, 29, 21, 24, 26, 28, 22]
}

data = [yields[veg] for veg in vegetables]
average_yields = [np.mean(yields[veg]) for veg in vegetables]

fig, ax = plt.subplots(figsize=(14, 8))
box = ax.boxplot(data, patch_artist=True, notch=True, vert=False, positions=range(1, len(vegetables) + 1), widths=0.6)

colors = ['#FFD700', '#ADFF2F', '#FFDEAD', '#9370DB']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
for whisker in box['whiskers']:
    whisker.set(color='black', linestyle='-', linewidth=1.5)
for cap in box['caps']:
    cap.set(color='black', linewidth=1.5)
for median in box['medians']:
    median.set(color='red', linewidth=2)
for flier in box['fliers']:
    flier.set(markerfacecolor='orange', marker='o', markersize=6)

ax.scatter(average_yields, range(1, len(vegetables) + 1), color='blue', s=100, zorder=3)

ax.xaxis.grid(False)
for spine in ax.spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()