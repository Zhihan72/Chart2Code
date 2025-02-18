import matplotlib.pyplot as plt
import numpy as np

apple_yield = [30, 35, 40, 32, 33, 36, 38, 37, 34, 31]
orange_yield = [25, 28, 22, 26, 29, 24, 21, 27, 23, 26]
pear_yield = [15, 17, 13, 18, 16, 14, 19, 12, 16, 15]
cherry_yield = [10, 13, 9, 11, 14, 8, 7, 10, 12, 13]

data = [apple_yield, orange_yield, pear_yield, cherry_yield]
fruit_labels = ['Apple', 'Orange', 'Pear', 'Cherry']

fig, ax = plt.subplots(figsize=(9, 5))

boxplot = ax.boxplot(data, vert=True, patch_artist=True, labels=fruit_labels, widths=0.7, notch=False)

# Manually shuffled colors
colors = ['#FFD700', '#FF4500', '#1E90FF', '#32CD32']  
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)

for whisker in boxplot['whiskers']:
    whisker.set(color='#00008B', linewidth=2, linestyle='-.')

for cap in boxplot['caps']:
    cap.set(color='#00008B', linewidth=2)

for median in boxplot['medians']:
    median.set(color='purple', linewidth=2.5)

ax.set_title("Orchard Yield from 2010 to 2020", fontsize=16, fontweight='bold')
ax.set_xlabel('Type of Fruit', fontsize=12)
ax.set_ylabel('Yield (in tons)', fontsize=12)

ax.yaxis.grid(True, linestyle=':', alpha=0.5)
ax.set_axisbelow(False)

for i, line in enumerate(boxplot['fliers']):
    y = line.get_ydata()
    x = line.get_xdata()
    for (xi, yi) in zip(x, y):
        ax.text(xi, yi, f'{yi}', va='top', ha='left', fontsize=9, color='gray', alpha=0.9)

plt.tight_layout()
plt.show()