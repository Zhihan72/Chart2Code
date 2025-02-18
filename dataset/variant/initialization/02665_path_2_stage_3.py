import matplotlib.pyplot as plt
import numpy as np

# Combine all delivery times into a single list
delivery_times = [
    2, 3, 5, 2, 3, 4, 5, 2, 3, 6, 2, 3, 4,
    4, 3, 5, 6, 4, 7, 3, 6, 4, 5, 7, 6, 8, 20,
    1, 2, 2, 1, 3, 2, 1, 2, 3, 1, 1, 2,
    3, 5, 4, 6, 5, 3, 4, 5, 6, 4, 5, 7, 3, 4,
    6, 8, 7, 9, 8, 10, 7, 6, 7, 11, 12, 10
]

fig, ax = plt.subplots(figsize=(6, 8))
bplot = ax.boxplot(delivery_times, vert=True, patch_artist=True, 
                   notch=False,
                   boxprops=dict(facecolor='lightgray', color='gray'),
                   whiskerprops=dict(color='darkgray'),
                   capprops=dict(color='lightgreen'),
                   medianprops=dict(color='purple', linewidth=2),
                   flierprops=dict(marker='x', color='orange', markersize=5))

ax.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.9)
ax.set_title('Overall Delivery Times Distribution', fontsize=14, fontweight='semibold')
ax.set_ylabel('Delivery Time (Days)', fontsize=11)

plt.tight_layout()
plt.show()