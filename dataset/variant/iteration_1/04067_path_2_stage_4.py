import matplotlib.pyplot as plt
import numpy as np

diets = ['Keto', 'Paleo', 'Vegan', 'Mediterranean', 'Intermittent Fasting']

# Manually shuffled weight loss data for 6 months
weight_loss_data = [
    [3.3, 3.0, 3.2, 2.9, 3.1, 3.4, 3.0, 3.1, 2.9, 3.3, 2.9, 2.8, 3.0, 3.2, 2.8, 3.0],
    [2.8, 2.7, 2.8, 3.0, 2.9, 3.0, 3.0, 3.1, 3.1, 3.0, 3.1, 2.9, 2.9, 3.2, 3.0, 2.8],
    [2.6, 2.4, 2.5, 2.8, 2.5, 2.6, 2.2, 2.4, 2.7, 2.4, 2.7, 2.5, 2.8, 2.3, 2.5, 2.6],
    [3.0, 2.9, 2.9, 3.1, 2.8, 2.9, 2.8, 3.1, 2.8, 2.7, 2.8, 3.0, 3.0, 2.9, 3.0, 2.7],
    [3.7, 3.6, 3.7, 3.6, 3.9, 3.9, 3.7, 3.5, 3.7, 3.8, 3.6, 3.5, 3.8, 3.8, 3.5, 3.7]
]

fig, ax = plt.subplots(figsize=(14, 10))

# Applying a single color consistently across all data groups
box_color = 'lightblue'

ax.boxplot(weight_loss_data, vert=False, notch=True, patch_artist=True,
           boxprops=dict(facecolor=box_color, color='blue', alpha=0.7),
           whiskerprops=dict(color='blue'),
           capprops=dict(color='blue'),
           medianprops=dict(color='darkred', linewidth=2),
           flierprops=dict(marker='o', color='red', markersize=6, alpha=0.5))

means = [np.mean(data) for data in weight_loss_data]

# Applying a single color consistently for mean points
ax.scatter(means, range(1, len(means) + 1), color=box_color, zorder=3)

ax.xaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.yticks(rotation=30, ha='right')

plt.tight_layout()

plt.show()