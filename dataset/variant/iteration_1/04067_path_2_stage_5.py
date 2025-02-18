import matplotlib.pyplot as plt
import numpy as np

diets = ['Keto', 'Paleo', 'Vegan', 'Mediterranean', 'Intermittent Fasting']

weight_loss_data = [
    [3.3, 3.0, 3.2, 2.9, 3.1, 3.4, 3.0, 3.1, 2.9, 3.3, 2.9, 2.8, 3.0, 3.2, 2.8, 3.0],
    [2.8, 2.7, 2.8, 3.0, 2.9, 3.0, 3.0, 3.1, 3.1, 3.0, 3.1, 2.9, 2.9, 3.2, 3.0, 2.8],
    [2.6, 2.4, 2.5, 2.8, 2.5, 2.6, 2.2, 2.4, 2.7, 2.4, 2.7, 2.5, 2.8, 2.3, 2.5, 2.6],
    [3.0, 2.9, 2.9, 3.1, 2.8, 2.9, 2.8, 3.1, 2.8, 2.7, 2.8, 3.0, 3.0, 2.9, 3.0, 2.7],
    [3.7, 3.6, 3.7, 3.6, 3.9, 3.9, 3.7, 3.5, 3.7, 3.8, 3.6, 3.5, 3.8, 3.8, 3.5, 3.7]
]

fig, ax = plt.subplots(figsize=(14, 10))

ax.boxplot(weight_loss_data, vert=False, notch=True, patch_artist=True,
           boxprops=dict(facecolor='lightgreen', color='purple'),
           whiskerprops=dict(color='purple', linestyle='-'),
           capprops=dict(color='purple', linestyle='--'),
           medianprops=dict(color='black', linewidth=2),
           flierprops=dict(marker='s', color='orange', markersize=8, alpha=0.7))

means = [np.mean(data) for data in weight_loss_data]
ax.scatter(means, range(1, len(means) + 1), color='purple', marker='x', zorder=3)

ax.xaxis.grid(True, linestyle=':', which='major', color='red', alpha=0.5)

plt.yticks(rotation=15, ha='right')

plt.xlabel('Weight Loss (kg)')
plt.title('Weight Loss Efficiency by Diet Type', fontsize=16)

plt.legend(['Mean Weight Loss'], loc='upper right', fontsize=10, frameon=True, fancybox=True, framealpha=0.5)

plt.tight_layout()

plt.show()