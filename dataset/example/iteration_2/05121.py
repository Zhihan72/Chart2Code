import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The Science Museum has been collecting data on visitors' engagement with various exhibits over the last decade.
# This histogram displays the frequency of visitors spending different durations of time at the "Mars Exploration" exhibit.

# Data: The amount of time (in minutes) visitors spent at the "Mars Exploration" exhibit
visitor_times = [
    5, 10, 15, 20, 25, 30, 30, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 15, 20, 25, 30, 30, 35, 40, 40, 45, 50,
    55, 60, 60, 65, 70, 75, 80, 80, 85, 90, 10, 15, 20, 25, 30, 30, 35, 40, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 80, 85,
    90, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120
]

# Creating figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting histogram with descriptive statistics (mean and median lines)
n, bins, patches = ax.hist(visitor_times, bins=12, color='#1f77b4', edgecolor='black', alpha=0.7, label='Time Spent')

# Calculating mean and median
mean_time = np.mean(visitor_times)
median_time = np.median(visitor_times)

# Drawing vertical lines for mean and median
ax.axvline(mean_time, color='red', linestyle='dashed', linewidth=2, label=f'Mean: {mean_time:.1f} mins')
ax.axvline(median_time, color='green', linestyle='dashed', linewidth=2, label=f'Median: {median_time:.1f} mins')

# Adding title and labels
ax.set_title('Time Spent by Visitors at the Mars Exploration Exhibit\nDataset from 2011-2021', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time Spent (Minutes)', fontsize=12)
ax.set_ylabel('Number of Visitors', fontsize=12)

# Grid for easier reading
ax.grid(True, axis='y', linestyle='--', alpha=0.7)

# Adding legend for context
ax.legend(loc='upper right')

# Adding counts on top of each bar for better readability
for patch in patches:
    height = patch.get_height()
    if height > 0:
        ax.text(patch.get_x() + patch.get_width() / 2, height + 1, int(height), ha='center', va='bottom')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()