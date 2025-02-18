import matplotlib.pyplot as plt
import numpy as np

# Shuffled data within the sedans list while preserving structure
sedans = [8.5, 9.2, 9.5, 7.4, 5.7, 6.8, 8.0, 7.6, 5.3, 9.0, 6.3, 6.1, 8.9, 7.8, 5.0, 8.3, 7.0, 6.5, 7.2, 5.5, 5.9]

fig, ax = plt.subplots(figsize=(7, 9))

single_color = 'lightblue'
box = ax.boxplot(sedans, vert=True, patch_artist=True, notch=True,
                 boxprops=dict(facecolor=single_color, color='navy'),
                 whiskerprops=dict(color='navy'),
                 capprops=dict(color='navy'),
                 medianprops=dict(color='darkorange', linewidth=2),
                 flierprops=dict(markerfacecolor='red', marker='o', markersize=8, linestyle='none'))

mean = np.mean(sedans)
ax.scatter(1, mean, color='blue', marker='D')

# Removed title and all textual elements including labels and annotations
ax.set_xticks(ticks=[1])
ax.set_xticklabels([''])  # Set empty string to remove labels
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()