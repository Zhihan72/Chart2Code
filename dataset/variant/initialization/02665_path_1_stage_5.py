import matplotlib.pyplot as plt
import numpy as np

# Original delivery times data
delivery_times_altered = [5, 6, 4, 7, 5, 3, 6, 3, 2, 8, 1, 3, 7, 
                          6, 2, 5, 2, 1, 4, 5, 3, 8, 4, 9, 8, 2, 20, 
                          7, 6, 6, 5, 1, 2, 3, 2, 3, 4, 5, 5, 
                          3, 8, 7, 1, 4, 3, 2, 1, 6, 4, 5, 9, 8, 7, 
                          6, 10, 4, 3, 5, 11, 7, 12, 7, 10, 9, 6, 10, 12]

# Additional made-up data series
delivery_times_additional = [8, 9, 10, 11, 9, 8, 7, 12, 15, 13, 14, 16, 17, 
                             14, 15, 13, 12, 16, 10, 11, 12, 19, 17, 18, 20, 
                             18, 19, 17, 15, 14, 13, 12, 16, 15, 18, 16, 14]

fig, ax = plt.subplots(figsize=(8, 6))
ax.boxplot([delivery_times_altered, delivery_times_additional], vert=True, patch_artist=False,
           boxprops=dict(color='blue'),
           whiskerprops=dict(color='blue'),
           capprops=dict(color='blue'),
           medianprops=dict(color='orange', linewidth=2),
           flierprops=dict(marker='x', color='cyan', markersize=7))

ax.set_ylabel('Days for Delivery', fontsize=12)
ax.set_xticklabels(['Altered Data', 'Additional Data'])

plt.tight_layout()
plt.show()