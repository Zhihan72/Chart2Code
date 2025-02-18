import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
x = np.arange(len(days))

screen_time = [3, 4, 4.5, 5, 6, 7, 5.5]
sleep_quality_index = [70, 65, 60, 55, 50, 45, 55]

fig, ax1 = plt.subplots(figsize=(12, 6))

# Random styles changes
color1 = 'tab:green'
color2 = 'tab:orange'
ax1.set_xlabel('Day of the Week', fontsize=14, fontweight='medium')
ax1.set_ylabel('Screen Time (Hours)', color=color1, fontsize=14, fontweight='medium')
ax1.plot(days, screen_time, color=color1, marker='^', linestyle='-.', linewidth=1.5, label='Screen Time')
ax1.tick_params(axis='y', labelcolor=color1)

# Alter grid style
ax1.grid(which='both', linestyle=':', linewidth=0.8, alpha=0.8)

ax2 = ax1.twinx()
ax2.set_ylabel('Sleep Quality Index', color=color2, fontsize=14, fontweight='medium')
ax2.plot(days, sleep_quality_index, color=color2, marker='x', linestyle='-', linewidth=1.5, label='Sleep Quality Index')
ax2.tick_params(axis='y', labelcolor=color2)

# Randomize title and legend
plt.title('Weekly Screen Time vs Sleep Quality', fontsize=16, fontweight='heavy', pad=20)

fig.tight_layout()

# Randomize legend position
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='lower center', fontsize=10)

plt.show()