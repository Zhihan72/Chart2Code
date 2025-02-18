import matplotlib.pyplot as plt
import numpy as np

# Days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
x = np.arange(len(days))

# Data: Average screen time in hours and sleep quality index (higher is better)
screen_time = [3, 4, 4.5, 5, 6, 7, 5.5]  # in hours
sleep_quality_index = [70, 65, 60, 55, 50, 45, 55]  # index from 0 to 100

# Initialize the plot
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting screen time as a primary Y-axis
color = 'tab:blue'  # Changed color
ax1.set_xlabel('Day of the Week', fontsize=12, fontweight='bold')
ax1.set_ylabel('Screen Time (Hours)', color=color, fontsize=12, fontweight='bold')
ax1.plot(days, screen_time, color=color, marker='o', linestyle='-', linewidth=2, label='Screen Time')
ax1.tick_params(axis='y', labelcolor=color)

# Setting up grid
ax1.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.6)

# Creating a secondary Y-axis for sleep quality index
color = 'tab:red'  # Changed color
ax2 = ax1.twinx()
ax2.set_ylabel('Sleep Quality Index', color=color, fontsize=12, fontweight='bold')
ax2.plot(days, sleep_quality_index, color=color, marker='s', linestyle='--', linewidth=2, label='Sleep Quality Index')
ax2.tick_params(axis='y', labelcolor=color)

# Title and legend
plt.title('Effect of Daily Screen Time on Sleep Quality Among Teenagers', fontsize=14, fontweight='bold', pad=20)

# Customize layout to prevent overlap and ensure better appearance
fig.tight_layout()

# Adding legends for both lines
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

# Display the plot
plt.show()