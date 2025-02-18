import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

age_groups = ['10-20', '21-30', '31-40', '41-50', '51-60', '61-70']
smartphone_usage = [
    [2.8, 2, 3, 2.7, 2.5, 3.2, 4, 2.2, 3.5],
    [3.5, 4, 3, 4.5, 3.9, 4.7, 4.2, 5, 4.1, 3.8],
    [2.5, 2.2, 1.5, 2.4, 2, 2.6, 2.3, 3, 2.8],
    [1.8, 1.5, 1, 1.6, 1.9, 1.4, 2, 1.7, 1.2],
    [1.2, 1, 0.8, 1.3, 1.4, 1.5, 1.2, 1.1, 1.1],
    [0.7, 0.5, 0.5, 1, 0.6, 1, 0.9, 0.8, 0.6]
]

fig, ax = plt.subplots(figsize=(8, 7))
boxplot = ax.boxplot(smartphone_usage, patch_artist=True, notch=False, vert=False, showmeans=False)

colors = ['lightpink', 'lightsalmon', 'lightgreen', 'lightyellow', 'lightblue', 'lightcoral']
for patch, color in zip(boxplot['boxes'], colors):
    patch.set_facecolor(color)
for median in boxplot['medians']:
    median.set(color='orange', linewidth=2)
for whisker in boxplot['whiskers']:
    whisker.set(color='darkgreen', linestyle='-.', linewidth=1)
for cap in boxplot['caps']:
    cap.set(color='darkred', linewidth=1)

ax.set_title("Smartphone Usage Across Different Age Groups in Techville", fontsize=14, fontstyle='italic')
ax.set_ylabel("Age Group", fontsize=11)
ax.set_xlabel("Hours of Smartphone Use per Day", fontsize=11)
ax.set_yticklabels(age_groups)
ax.xaxis.grid(True, linestyle='-', which='both', color='lightgrey', alpha=0.7)

# Adjusted legend styling
legend_elements = [
    plt.Line2D([0], [0], color='darkgreen', linestyle='-.', lw=1, label='Whisker'),
    plt.Line2D([0], [0], color='orange', lw=2, label='Median'),
    mpatches.Patch(facecolor='lightpink', edgecolor='r', label='Age Group 10-20'),
    mpatches.Patch(facecolor='lightsalmon', edgecolor='r', label='Age Group 21-30')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10, frameon=True, shadow=True)

plt.tight_layout()
plt.show()