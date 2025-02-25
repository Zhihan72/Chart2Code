import matplotlib.pyplot as plt
import numpy as np

# Adjusted visitor time data, removed times <= 15
visitor_times = [
    20, 25, 30, 30, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 20, 25, 30, 30, 35, 40, 40, 45, 50,
    55, 60, 60, 65, 70, 75, 80, 80, 85, 90, 25, 30, 30, 35, 40, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 80,
    85, 90, 20, 25, 30, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120
]

fig, ax = plt.subplots(figsize=(14, 8))

n, bins, patches = ax.hist(visitor_times, bins=12, color='#1f77b4', edgecolor='black', alpha=0.7, label='Time')

mean_time = np.mean(visitor_times)
median_time = np.median(visitor_times)

ax.axvline(mean_time, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_time:.1f} min')
ax.axvline(median_time, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_time:.1f} min')

ax.set_title('Time at Mars Exhibit\n2011-2021', fontsize=16, fontweight='bold', pad=20)
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