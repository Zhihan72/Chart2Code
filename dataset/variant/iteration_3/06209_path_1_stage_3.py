import matplotlib.pyplot as plt
import numpy as np

# Days
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
x = np.arange(len(days))

# Data: Screen time and sleep quality index
screen_time = [3, 4, 4.5, 5, 6, 7, 5.5]
sleep_quality_index = [70, 65, 60, 55, 50, 45, 55]

fig, ax1 = plt.subplots(figsize=(12, 6))

# Consistent color for both data groups
color = 'blue'

# Screen time
ax1.set_xlabel('Day', fontsize=12, fontweight='bold')
ax1.set_ylabel('Screen Time (hrs)', color=color, fontsize=12, fontweight='bold')
ax1.plot(days, screen_time, color=color, marker='D', linestyle=':', linewidth=3, label='Screen Time')
ax1.tick_params(axis='y', labelcolor=color)

# Sleep quality index
ax2 = ax1.twinx()
ax2.set_ylabel('Sleep Quality', color=color, fontsize=12, fontweight='bold')
ax2.plot(days, sleep_quality_index, color=color, marker='x', linestyle='-', linewidth=2, label='Sleep Quality')
ax2.tick_params(axis='y', labelcolor=color)

# Title
plt.title('Screen Time vs Sleep in Teens', fontsize=16, fontweight='bold', pad=10)

# Legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper right', fontsize=9, frameon=False)

# Border
for spine in ax1.spines.values():
    spine.set_linewidth(1.5)
for spine in ax2.spines.values():
    spine.set_linewidth(1.5)

# Display
plt.show()