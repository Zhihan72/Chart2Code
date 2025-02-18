import matplotlib.pyplot as plt
import numpy as np

# Define delivery times for different zones
zone_a_times = [2, 3, 5, 2, 3, 4, 5, 2, 3, 6, 2, 3, 4]
zone_b_times = [4, 3, 5, 6, 4, 7, 3, 6, 4, 5, 7, 6, 8, 20]
zone_c_times = [1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2,
                3, 5, 4, 6, 5, 3, 4, 5, 6, 4, 5, 7, 3, 4,
                6, 8, 7, 9, 8, 10, 7, 6, 7, 11, 12, 10]

# Create a list of delivery times for each zone
delivery_times = [zone_a_times, zone_b_times, zone_c_times]

fig, ax = plt.subplots(figsize=(8, 6))
bplot = ax.boxplot(delivery_times, vert=True, patch_artist=True, 
                   notch=False, labels=['Zone A', 'Zone B', 'Zone C'],
                   boxprops=dict(facecolor='lightgray', color='gray'),
                   whiskerprops=dict(color='darkgray'),
                   capprops=dict(color='lightgreen'),
                   medianprops=dict(color='purple', linewidth=2),
                   flierprops=dict(marker='x', color='orange', markersize=5))

ax.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.9)
ax.set_title('Delivery Times Distribution Across Zones', fontsize=14, fontweight='semibold')
ax.set_ylabel('Delivery Time (Days)', fontsize=11)

plt.tight_layout()
plt.show()