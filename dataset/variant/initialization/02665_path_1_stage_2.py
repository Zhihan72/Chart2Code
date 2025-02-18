import matplotlib.pyplot as plt
import numpy as np

# Altered set of delivery times
delivery_times_altered = [5, 6, 4, 7, 5, 3, 6, 3, 2, 8, 1, 3, 7, 
                          6, 2, 5, 2, 1, 4, 5, 3, 8, 4, 9, 8, 2, 20, 
                          7, 6, 6, 5, 1, 2, 3, 2, 3, 4, 5, 5, 
                          3, 8, 7, 1, 4, 3, 2, 1, 6, 4, 5, 9, 8, 7, 
                          6, 10, 4, 3, 5, 11, 7, 12, 7, 10, 9, 6, 10, 12]

fig, ax = plt.subplots(figsize=(6, 8))
bplot = ax.boxplot(delivery_times_altered, vert=True, patch_artist=True, 
                   boxprops=dict(facecolor='lightgreen', color='green'),
                   whiskerprops=dict(color='green'),
                   capprops=dict(color='green'),
                   medianprops=dict(color='purple', linewidth=2),
                   flierprops=dict(marker='x', color='red', markersize=7))

# Altered labels and title
ax.set_title('E-commerce Order Times\nVariation', fontsize=16, fontweight='bold')
ax.set_ylabel('Days for Delivery', fontsize=12)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)
plt.tight_layout()
plt.show()