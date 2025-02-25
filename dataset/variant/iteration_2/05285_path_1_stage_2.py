import matplotlib.pyplot as plt
import numpy as np

# Define hours in a typical workday
hours = np.array([8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

# Manually constructed usage data (percentage used)
cpu_usage = np.array([40, 45, 55, 70, 60, 65, 75, 70, 60, 50, 45])
ram_usage = np.array([30, 35, 40, 50, 45, 50, 55, 53, 48, 44, 40])
disk_usage = np.array([50, 55, 60, 65, 70, 75, 70, 65, 60, 55, 50])
network_usage = np.array([20, 25, 30, 35, 40, 45, 40, 35, 30, 25, 20])

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data with new colors
ax.plot(hours, cpu_usage, label='CPU Usage', color='coral', marker='o', linestyle='-', linewidth=2.5)
ax.plot(hours, ram_usage, label='RAM Usage', color='lime', marker='s', linestyle='--', linewidth=2.5)
ax.plot(hours, disk_usage, label='Disk Usage', color='navy', marker='^', linestyle='-.', linewidth=2.5)
ax.plot(hours, network_usage, label='Network Usage', color='orchid', marker='d', linestyle=':', linewidth=2.5)

# Adding grid, title, and labels
ax.set_title("IT System Performance Monitoring\nCPU, RAM, Disk, and Network Usage Over a Workday", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Hour of the Day", fontsize=14)
ax.set_ylabel("Usage (%)", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.6)

# Add legend
ax.legend(loc='upper right', fontsize=12)

# Annotate peak usages with new colors
for usage, label, color in zip(
    [cpu_usage, ram_usage, disk_usage, network_usage],
    ['CPU', 'RAM', 'Disk', 'Network'],
    ['coral', 'lime', 'navy', 'orchid']
):
    peak_hour = hours[np.argmax(usage)]
    peak_value = np.max(usage)
    ax.annotate(f'Peak: {peak_value}%', xy=(peak_hour, peak_value), xytext=(peak_hour, peak_value+5),
                arrowprops=dict(facecolor=color, shrink=0.05), fontsize=12, color=color, ha='center')

    low_hour = hours[np.argmin(usage)]
    low_value = np.min(usage)
    ax.annotate(f'Lowest: {low_value}%', xy=(low_hour, low_value), xytext=(low_hour, low_value-10),
                arrowprops=dict(facecolor=color, shrink=0.05), fontsize=12, color=color, ha='center')

# Make the layout tight
plt.tight_layout()

# Display the plot
plt.show()