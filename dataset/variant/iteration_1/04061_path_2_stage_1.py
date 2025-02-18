import matplotlib.pyplot as plt
import numpy as np

age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70']
smartphone_usage = [
    [2, 2.5, 3, 2.2, 2.8, 3.5, 4, 3.2, 2.7],
    [3, 3.5, 4, 4.2, 3.8, 4.7, 5, 4.5, 4.1, 3.9],
    [1.5, 2, 2.2, 2.5, 2.3, 2.8, 3, 2.6, 2.4],
    [1, 1.2, 1.5, 1.4, 1.6, 1.7, 2, 1.8, 1.9],
    [0.8, 1, 1.2, 1.1, 1.3, 1.5, 1.4, 1.2, 1.1],
    [0.5, 0.7, 0.6, 0.8, 1, 0.9, 0.7, 0.6, 0.5]
]

all_ages_usage = sum(smartphone_usage, [])

fig, axs = plt.subplots(1, 2, figsize=(15, 7))

boxplot = axs[0].boxplot(smartphone_usage, patch_artist=True, notch=True, vert=True, showmeans=True)

# Shuffled color list
colors = ['lightgreen', 'lightsalmon', 'lightpink', 'lightyellow', 'lightcoral', 'lightblue']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
for median in boxplot['medians']:
    median.set(color='purple', linewidth=1.5)
for mean in boxplot['means']:
    mean.set(marker='o', markerfacecolor='darkblue', markeredgecolor='darkblue')

axs[0].set_title("Smartphone Usage Across Different Age Groups\nin Techville", fontsize=15, fontweight='bold')
axs[0].set_xlabel("Age Group", fontsize=12)
axs[0].set_ylabel("Hours of Smartphone Use per Day", fontsize=12)
axs[0].set_xticklabels(age_groups)
axs[0].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)
axs[0].tick_params(axis='x', rotation=45)

axs[1].hist(all_ages_usage, bins=np.arange(0, 6, 0.5), color='skyblue', edgecolor='black', alpha=0.7)
axs[1].set_title("Distribution of Smartphone Usage\nin Techville", fontsize=15, fontweight='bold')
axs[1].set_xlabel("Hours of Smartphone Use per Day", fontsize=12)
axs[1].set_ylabel("Number of People", fontsize=12)
axs[1].yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

plt.tight_layout()
plt.show()