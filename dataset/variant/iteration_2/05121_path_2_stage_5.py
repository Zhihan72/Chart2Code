import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

visitor_times = [
    5, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 15, 20, 25, 35, 40, 40, 45, 50,
    55, 60, 60, 65, 70, 75, 80, 80, 85, 90, 10, 15, 20, 25, 35, 40, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 80, 85,
    90, 10, 15, 20, 25, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120
]

# Count the occurrences of each duration time
time_counts = Counter(visitor_times)

# Sort the time intervals and their counts
sorted_times = sorted(time_counts.items(), key=lambda x: x[0])  # Sort by time (ascending)

times, counts = zip(*sorted_times)  # Unpack the sorted pairs

fig, ax = plt.subplots(figsize=(14, 8))

ax.bar(times, counts, color='green', edgecolor='purple', alpha=0.8, label='Visitor Duration')

mean_time = np.mean(visitor_times)
median_time = np.median(visitor_times)

ax.axvline(mean_time, color='grey', linestyle='solid', linewidth=3, label=f'Mean: {mean_time:.1f} mins')
ax.axvline(median_time, color='red', linestyle='dotted', linewidth=2, label=f'Median: {median_time:.1f} mins')

ax.set_title('Exhibit Stay Time', fontsize=14, fontweight='light', pad=15)
ax.set_xlabel('Time (minutes)', fontsize=12)
ax.set_ylabel('Visitor Count', fontsize=12)
ax.grid(False)
ax.legend(loc='upper left')

# Added annotations for each bar
for x, y in zip(times, counts):
    ax.text(x, y + 1, str(y), ha='center', va='bottom')

plt.tight_layout()
plt.show()