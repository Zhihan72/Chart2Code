import matplotlib.pyplot as plt
import numpy as np

delivery_times_altered = [5, 6, 4, 7, 5, 3, 6, 3, 2, 8, 1, 3, 7, 
                          6, 2, 5, 2, 1, 4, 5, 3, 8, 4, 9, 8, 2, 20, 
                          7, 6, 6, 5, 1, 2, 3, 2, 3, 4, 5, 5, 
                          3, 8, 7, 1, 4, 3, 2, 1, 6, 4, 5, 9, 8, 7, 
                          6, 10, 4, 3, 5, 11, 7, 12, 7, 10, 9, 6, 10, 12]

fig, ax = plt.subplots(figsize=(6, 8))
ax.boxplot(delivery_times_altered, vert=True, patch_artist=False,
           boxprops=dict(color='blue'),  # Changed from green to blue
           whiskerprops=dict(color='blue'),  # Changed from green to blue
           capprops=dict(color='blue'),  # Changed from green to blue
           medianprops=dict(color='orange', linewidth=2),  # Changed from purple to orange
           flierprops=dict(marker='x', color='cyan', markersize=7))  # Changed from red to cyan

ax.set_ylabel('Days for Delivery', fontsize=12)

plt.tight_layout()
plt.show()