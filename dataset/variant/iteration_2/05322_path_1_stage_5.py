import matplotlib.pyplot as plt
import numpy as np

regions = ['N. Am.', 'Eur.', 'Asia']

wheat_na = [3.2, 3.5, 3.6, 4.0, 4.2, 3.9, 4.1, 3.8, 4.0, 3.7]
corn_na = [10.5, 11.0, 11.2, 10.8, 10.9, 11.1, 10.7, 10.8, 11.3, 10.9]
rice_na = [7.8, 8.0, 7.9, 8.2, 8.3, 8.1, 8.0, 7.8, 8.2, 8.1]

wheat_eu = [5.5, 5.4, 5.6, 5.7, 5.8, 5.5, 5.6, 5.4, 5.7, 5.5]
corn_eu = [9.0, 8.8, 8.9, 9.2, 9.1, 8.7, 9.0, 9.1, 8.8, 8.9]
rice_eu = [6.5, 6.6, 6.7, 6.5, 6.8, 6.4, 6.6, 6.5, 6.6, 6.7]

wheat_as = [3.8, 3.9, 4.0, 4.1, 4.2, 4.0, 4.1, 3.9, 4.0, 4.1]
corn_as = [5.5, 5.6, 5.7, 5.6, 5.5, 5.7, 5.6, 5.5, 5.4, 5.6]
rice_as = [9.2, 9.3, 9.1, 9.2, 9.3, 9.1, 9.2, 9.0, 9.3, 9.1]

data_wheat = [wheat_na, wheat_eu, wheat_as]
data_corn = [corn_na, corn_eu, corn_as]
data_rice = [rice_na, rice_eu, rice_as]

fig, axes = plt.subplots(1, 3, figsize=(18, 8), sharey=True)

axes[0].set_title('Wheat 2022', fontsize=14, fontstyle='italic')
axes[1].set_title('Rice 2022', fontsize=14, fontweight='light')
axes[2].set_title('Corn 2022', fontsize=14, fontweight='bold')

box_wheat = axes[0].boxplot(data_wheat, vert=False, patch_artist=True, labels=regions, notch=False)
for patch in box_wheat['boxes']:
    patch.set_facecolor('#FFA07A')  # New color: Light Salmon
axes[0].set_xlabel('Yield (t/ha)', fontsize=12, color='darkred')

box_rice = axes[1].boxplot(data_rice, vert=False, patch_artist=True, labels=regions, notch=True)
for patch in box_rice['boxes']:
    patch.set_facecolor('#4682B4')  # New color: Steel Blue
axes[1].set_xlabel('Yield (t/ha)', fontsize=12, color='navy')

box_corn = axes[2].boxplot(data_corn, vert=True, patch_artist=True, labels=regions, notch=True, boxprops=dict(linestyle='-'))
for patch in box_corn['boxes']:
    patch.set_facecolor('#98FB98')  # New color: Pale Green
axes[2].set_xlabel('Yield (t/ha)', fontsize=12, color='green')

for ax in axes:
    ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.4)
    ax.set_axisbelow(True)
    ax.spines['top'].set_linestyle('--')
    ax.spines['right'].set_linestyle('--')

fig.suptitle('Crop Yields 2022', fontsize=18, fontweight='heavy', style='italic', y=1.02)
plt.tight_layout(rect=[0, 0, 1, 0.955])
plt.show()