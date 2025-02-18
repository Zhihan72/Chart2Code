import matplotlib.pyplot as plt
import numpy as np

species = ['Rose', 'Tulip', 'Daisy']
growth_rates = [
    [2.5, 2.7, 2.8, 3.0, 2.6, 3.1, 2.9, 2.8, 3.0, 2.7, 2.5, 3.0, 2.6, 2.8, 3.1],
    [1.5, 1.6, 1.7, 1.6, 1.8, 1.7, 1.9, 1.8, 1.6, 1.7, 1.8, 1.9, 1.7, 1.8, 1.9],
    [2.0, 2.1, 2.3, 2.2, 2.4, 2.3, 2.2, 2.5, 2.4, 2.3, 2.5, 2.6, 2.4, 2.5, 2.6]
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(growth_rates, patch_artist=True, notch=True, vert=True, showmeans=True)

colors = ['#ff9999', '#99ff99', '#66b3ff']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

for median, mean in zip(box['medians'], box['means']):
    median.set_color('black')
    median.set_linewidth(2)
    mean.set_markerfacecolor('red')
    mean.set_markeredgecolor('red')

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()