import matplotlib.pyplot as plt
import numpy as np

visitor_times_group_1 = [20, 25, 30, 30, 35, 40, 45, 50, 55, 60, 60, 65]
visitor_times_group_2 = [70, 75, 80, 85, 90, 20, 25, 30, 30, 35, 40, 40]
visitor_times_group_3 = [45, 50, 55, 60, 60, 65, 70, 75, 80, 80, 85, 90]
visitor_times_group_4 = [25, 30, 30, 35, 40, 40, 45, 50, 55, 60, 60, 65]
visitor_times_group_5 = [70, 75, 80, 85, 90, 20, 25, 30, 35, 40, 45, 50]
visitor_times_group_6 = [55, 60, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120]

visitor_times = [visitor_times_group_1, visitor_times_group_2, visitor_times_group_3,
                 visitor_times_group_4, visitor_times_group_5, visitor_times_group_6]

fig, ax = plt.subplots(figsize=(14, 8))

n, bins, patches = ax.hist(visitor_times, bins=12, stacked=True, edgecolor='black', alpha=0.7)

# New colors for the bars
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A8', '#33FFF6', '#FF9233']

# Apply new colors to each group of bars
for patch, color in zip(patches, colors):
    for rectangle in patch:
        rectangle.set_facecolor(color)

ax.set_title('Stacked Histogram of Time at Mars Exhibit\n2011-2021', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time (min)', fontsize=12)
ax.set_ylabel('Visitors', fontsize=12)

ax.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()