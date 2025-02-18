import matplotlib.pyplot as plt
import numpy as np

age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70']
smartphone_usage = [
    [2.7, 2.2, 4, 3.2, 2, 3.5, 2.5, 3, 2.8],
    [3.5, 4.1, 5, 4.7, 3.9, 3, 4.5, 4.2, 3.8],
    [2.4, 2.3, 3, 2.8, 2, 1.5, 2.6, 2.5, 2.2],
    [1.5, 1.9, 2, 1.4, 1.6, 1.8, 1.2, 1.7, 1],
    [1.4, 1.3, 1, 1.1, 1.2, 0.8, 1.5, 1.1, 0.5],
    [0.9, 0.6, 0.7, 1, 0.8, 0.5, 0.7, 0.6, 0.5]
]

all_ages_usage = sum(smartphone_usage, [])

fig, axs = plt.subplots(1, 2, figsize=(15, 7))

boxplot = axs[0].boxplot(smartphone_usage, patch_artist=True, notch=True, vert=False, showmeans=True)
new_colors = ['salmon', 'lightseagreen', 'gold', 'plum', 'peachpuff', 'lightskyblue']
for patch, color in zip(boxplot['boxes'], new_colors):
    patch.set_facecolor(color)
for median in boxplot['medians']:
    median.set(color='purple', linewidth=1.5)
for mean in boxplot['means']:
    mean.set(marker='o', markerfacecolor='darkblue', markeredgecolor='darkblue')

axs[0].set_yticklabels(age_groups)
axs[0].xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

axs[1].hist(all_ages_usage, bins=np.arange(0, 6, 0.5), color='mediumaquamarine', edgecolor='black', alpha=0.7)
axs[1].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

plt.tight_layout()
plt.show()