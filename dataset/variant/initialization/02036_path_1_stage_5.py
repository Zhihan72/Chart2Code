import matplotlib.pyplot as plt
import numpy as np

innovation_data = [
    [65, 72, 78, 85, 90, 92, 95, 97, 100, 105],
    [50, 55, 62, 65, 70, 78, 80, 82, 85, 88],
    [30, 35, 42, 50, 60, 70, 75, 80, 85, 90],
    [70, 72, 74, 75, 77, 80, 85, 88, 90, 92],
    [40, 50, 58, 65, 72, 80, 85, 89, 93, 95],
    [45, 55, 65, 70, 75, 78, 81, 85, 88, 91],
    [60, 68, 72, 78, 82, 85, 87, 89, 92, 94]
]

fig, ax = plt.subplots(figsize=(12, 8))

bp = ax.boxplot(innovation_data, vert=False, patch_artist=True, 
                notch=True, showmeans=True, meanline=True,
                meanprops=dict(linestyle='--', linewidth=2.5, color='orange'))

colors = ['#FFCC99', '#99FF99', '#FF9999', '#FFD700', '#66B3FF', '#C0C0C0', '#8A2BE2']
hatches = ['/', '\\', '|', '-', '+', 'x', '*']
for patch, color, hatch in zip(bp['boxes'], colors, hatches):
    patch.set(facecolor=color, hatch=hatch, alpha=0.7)

for median in bp['medians']:
    median.set(color='blue', linewidth=3)
for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=2, linestyle='--')
for cap in bp['caps']:
    cap.set(color='black', linewidth=2)

plt.tight_layout()
plt.show()