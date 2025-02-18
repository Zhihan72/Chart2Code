import matplotlib.pyplot as plt
import numpy as np

central_parks = [2, 5, 7, 10, 15, 18, 22, 25, 28, 30]
eastside_parks = [3, 4, 6, 8, 9, 12, 13, 15, 17, 20]
westend_parks = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
north_hills_parks = [1, 3, 4, 6, 8, 11, 14, 18, 19, 22]
southfield_parks = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
park_sizes = [central_parks, eastside_parks, westend_parks, north_hills_parks, southfield_parks]

fig, ax = plt.subplots(figsize=(12, 8))

boxes = ax.boxplot(park_sizes, patch_artist=True, notch=True, vert=False,
                   boxprops=dict(color='black', linewidth=1.5),
                   medianprops=dict(color='red', linewidth=2),
                   whiskerprops=dict(color='black', linewidth=1.5),
                   capprops=dict(color='black', linewidth=1.5),
                   flierprops=dict(marker='o', color='black', alpha=0.5, markersize=8))

colors = ['#FFDEAD', '#B0E57C', '#77BFC7', '#FFCCCB', '#FFB6C1']
for patch, color in zip(boxes['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

for i, data in enumerate(park_sizes, start=1):
    x = np.array(data)
    y = np.random.normal(i, 0.04, size=len(x))
    ax.scatter(x, y, alpha=0.6, edgecolor='w', s=80)

mean_sizes = [np.mean(d) for d in park_sizes]
for i, mean in enumerate(mean_sizes, start=1):
    ax.axvline(mean, ls='--', color=colors[i-1], alpha=0.7, linewidth=1.5)

plt.tight_layout()
plt.show()