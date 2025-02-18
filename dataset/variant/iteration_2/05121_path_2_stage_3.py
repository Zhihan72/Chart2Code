import matplotlib.pyplot as plt
import numpy as np

visitor_times = [
    5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 15, 20, 25, 35, 40, 40, 45, 50,
    55, 60, 60, 65, 70, 75, 80, 80, 85, 90, 10, 15, 20, 25, 35, 40, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 80, 85,
    90, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120
]

fig, ax = plt.subplots(figsize=(14, 8))

n, bins, patches = ax.hist(visitor_times, bins=12, color='blue', edgecolor='black', alpha=0.7, label='Time Spent')

mean_time = np.mean(visitor_times)
median_time = np.median(visitor_times)

ax.axvline(mean_time, color='blue', linestyle='dashed', linewidth=2, label=f'Mean: {mean_time:.1f} mins')
ax.axvline(median_time, color='blue', linestyle='dashed', linewidth=2, label=f'Median: {median_time:.1f} mins')

ax.set_title('Visitor Time at Mars Exhibit', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (min)', fontsize=12)
ax.set_ylabel('Visitors', fontsize=12)

ax.grid(True, axis='y', linestyle='--', alpha=0.7)

ax.legend(loc='upper right')

for patch in patches:
    height = patch.get_height()
    if height > 0:
        ax.text(patch.get_x() + patch.get_width() / 2, height + 1, int(height), ha='center', va='bottom')

plt.tight_layout()
plt.show()