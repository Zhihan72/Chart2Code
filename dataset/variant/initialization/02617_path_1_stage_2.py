import matplotlib.pyplot as plt
import numpy as np

# Data setup
crops = ['Wheat', 'Corn', 'Rice', 'Soy', 'Cott']
wheat_yield = [2.5, 3.0, 3.2, 2.8, 2.9, 3.5, 3.1, 2.7, 3.3, 2.4]
corn_yield = [5.0, 5.5, 5.2, 6.0, 5.8, 5.7, 5.1, 6.2, 5.4, 5.3]
rice_yield = [4.0, 4.2, 4.1, 4.5, 4.3, 4.4, 4.0, 4.6, 4.8, 4.5]
soy_yield = [3.0, 3.5, 3.7, 3.3, 3.6, 3.4, 3.9, 3.2, 3.1, 3.8]
cotton_yield = [1.8, 2.0, 2.1, 2.3, 2.2, 2.5, 2.4, 2.0, 1.9, 2.1]

data = [wheat_yield, corn_yield, rice_yield, soy_yield, cotton_yield]

fig, ax = plt.subplots(figsize=(10, 7))
boxprops = dict(linestyle='-', linewidth=2, color='darkblue')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')

ax.boxplot(data, vert=False, patch_artist=True, showmeans=True, notch=True,
           boxprops=boxprops, medianprops=medianprops, meanprops=meanprops,
           whiskerprops=dict(linewidth=1.5), capprops=dict(linewidth=1.5))

ax.set_yticklabels(crops, fontsize=12)
ax.set_title('Crop Yield Impact', fontsize=14, weight='bold', pad=20)
ax.set_xlabel('Yield (t/ha)', fontsize=12)
ax.set_ylabel('Crop', fontsize=12)
ax.grid(True, which='both', linestyle='--', alpha=0.5)

# Shuffled colors
colors = ['#FFCC99', '#99FF99', '#FF9999', '#FFD700', '#66B3FF']
for patch, color in zip(ax.artists, colors):
    patch.set_facecolor(color)

for i, crop in enumerate(crops):
    ax.text(data[i][-1] + 0.05, i + 1, f'{np.mean(data[i]):.2f}',
            va='center', fontsize=10, color='black', weight='bold')

plt.tight_layout()
plt.show()