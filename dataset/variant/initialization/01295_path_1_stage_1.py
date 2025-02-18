import matplotlib.pyplot as plt
import numpy as np

# Combine data from all cities into a single dataset
combined_data = [1.2, 1.5, 1.3, 1.4, 1.6, 1.5, 1.7, 1.8, 1.6, 1.7,
                 2.1, 2.3, 2.5, 2.2, 2.4, 2.6, 2.5, 2.7, 2.8, 2.6,
                 1.7, 1.6, 1.9, 1.8, 2.0, 1.9, 2.1, 2.2, 1.8, 2.0,
                 0.8, 1.0, 1.1, 1.2, 1.3, 1.1, 1.0, 1.2, 1.4, 1.3,
                 3.2, 3.0, 3.3, 3.5, 3.6, 3.4, 3.5, 3.6, 3.7, 3.8]

fig, ax = plt.subplots(figsize=(8, 6))

# Box plot settings for a single vertical box
ax.boxplot(combined_data, vert=True, patch_artist=True,
           boxprops=dict(facecolor='#A3E4D7', color='green'),
           whiskerprops=dict(color='green'),
           capprops=dict(color='green'),
           flierprops=dict(marker='o', color='red', markersize=8, alpha=0.5),
           medianprops=dict(color='orange', linewidth=2))

# Title and labels
ax.set_title('Park Size Distribution Across Urban Areas', fontsize=14, fontweight='bold', pad=20)
ax.set_ylabel('Park Size (Square Kilometers)', fontsize=12, fontweight='bold')
ax.set_xticks([])  # Remove x-ticks as there's only one boxplot
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()