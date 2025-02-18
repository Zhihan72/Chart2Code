import matplotlib.pyplot as plt
import numpy as np

age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70']
smartphone_usage = [
    [2.8, 2, 3, 2.7, 2.5, 3.2, 4, 2.2, 3.5],  # Manually shuffled values
    [3.5, 4, 3, 4.5, 3.9, 4.7, 4.2, 5, 4.1, 3.8],  # Manually shuffled values
    [2.5, 2.2, 1.5, 2.4, 2, 2.6, 2.3, 3, 2.8],  # Manually shuffled values
    [1.8, 1.5, 1, 1.6, 1.9, 1.4, 2, 1.7, 1.2],  # Manually shuffled values
    [1.2, 1, 0.8, 1.3, 1.4, 1.5, 1.2, 1.1, 1.1],  # Manually shuffled values
    [0.7, 0.5, 0.5, 1, 0.6, 1, 0.9, 0.8, 0.6]  # Manually shuffled values
]

fig, ax = plt.subplots(figsize=(8, 7))
boxplot = ax.boxplot(smartphone_usage, patch_artist=True, notch=True, vert=False, showmeans=True)

colors = ['lightgreen', 'lightsalmon', 'lightpink', 'lightyellow', 'lightcoral', 'lightblue']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
for median in boxplot['medians']:
    median.set(color='purple', linewidth=1.5)
for mean in boxplot['means']:
    mean.set(marker='o', markerfacecolor='darkblue', markeredgecolor='darkblue')

ax.set_title("Smartphone Usage Across Different Age Groups\nin Techville", fontsize=15, fontweight='bold')
ax.set_ylabel("Age Group", fontsize=12)
ax.set_xlabel("Hours of Smartphone Use per Day", fontsize=12)
ax.set_yticklabels(age_groups)
ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.5)

plt.tight_layout()
plt.show()