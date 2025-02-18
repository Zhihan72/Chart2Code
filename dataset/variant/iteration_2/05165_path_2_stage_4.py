import matplotlib.pyplot as plt
import numpy as np

north_rivers = [85, 87, 90, 88, 83, 82, 85, 90, 95, 89]
east_rivers = [78, 75, 80, 72, 74, 79, 76, 77, 75, 78]
south_rivers = [88, 80, 85, 87, 83, 84, 86, 82, 85, 88]
central_rivers = [90, 88, 92, 91, 89, 95, 93, 94, 90, 92]

river_qualities = [north_rivers, east_rivers, south_rivers, central_rivers]

fig, ax = plt.subplots(figsize=(12, 7))

box = ax.boxplot(river_qualities, patch_artist=True, vert=False,
                 boxprops=dict(color='black'),
                 medianprops=dict(color='red'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 flierprops=dict(marker='o', color='black', alpha=0.5))

colors = ['#87CEFA', '#98FB98', '#FFA07A', '#FFD700']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_yticks([])  # Remove y-ticks
ax.set_xticks([])  # Remove x-ticks

plt.show()