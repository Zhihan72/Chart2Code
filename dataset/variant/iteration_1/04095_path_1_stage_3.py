import matplotlib.pyplot as plt
import numpy as np

species = ['Rose', 'Sunflower', 'Tulip', 'Daisy', 'Lavender']
growth_rates = [
    [2.8, 2.5, 2.9, 3.0, 2.7, 2.6, 3.1, 3.0, 2.8, 2.7, 2.9, 2.5, 3.0, 2.6, 2.8],
    [3.7, 3.5, 3.9, 3.6, 4.1, 4.0, 3.8, 3.7, 4.0, 3.8, 3.9, 4.1, 3.9, 3.6, 3.8],
    [1.6, 1.5, 1.9, 1.8, 1.7, 1.8, 1.7, 1.6, 1.9, 1.7, 1.6, 1.8, 1.9, 1.7, 1.8],
    [2.3, 2.0, 2.4, 2.5, 2.1, 2.2, 2.2, 2.6, 2.5, 2.3, 2.6, 2.4, 2.5, 2.3, 2.4],
    [1.4, 1.2, 1.5, 1.3, 1.3, 1.6, 1.4, 1.2, 1.3, 1.5, 1.6, 1.4, 1.3, 1.5, 1.4]
]

fig, ax = plt.subplots(figsize=(12, 8))
box = ax.boxplot(growth_rates, patch_artist=True, notch=False, vert=True, showmeans=True)

colors = ['#99ccff', '#ffb3e6', '#c2f0c2', '#ffcc80', '#e6e6e6']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.set_title('Weekly Growth Rates of Plant Species', fontsize=16, fontstyle='italic')
ax.set_ylabel('Weekly Growth Rate (cm)', fontsize=14)
ax.set_xlabel('Plant Species', fontsize=14)
ax.set_xticks(np.arange(1, len(species) + 1))
ax.set_xticklabels(species)

for median, mean in zip(box['medians'], box['means']):
    median.set_color('green')
    median.set_linewidth(1)
    mean.set_markerfacecolor('blue')
    mean.set_markeredgecolor('blue')
    mean.set_markeredgewidth(1)
    mean.set_marker('*')

mean_legend = plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='blue', markersize=10, label='Mean')
median_legend = plt.Line2D([0], [0], color='green', lw=1, label='Median')
ax.legend(handles=[mean_legend, median_legend], loc='lower left', fontsize=12, frameon=False)

ax.yaxis.grid(True, linestyle='-.', linewidth=0.7, alpha=0.6)

fig.patch.set_facecolor('#fefbd8')

plt.tight_layout()
plt.show()