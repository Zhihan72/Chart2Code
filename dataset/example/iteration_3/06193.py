import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Imagine a tech company monitoring its network's data traffic load throughout a week.
# The company has data on the average upload and download speeds (Mbps) to track network performance.

# Data Preparation
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_upload_speeds = [10, 15, 12, 20, 18, 8, 25]  # Average upload speeds (Mbps)
avg_download_speeds = [50, 48, 52, 55, 53, 60, 58]  # Average download speeds (Mbps)

# Set up the figure and plot the line chart
plt.figure(figsize=(14, 8))

# Plot upload speeds
plt.plot(days, avg_upload_speeds, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8, label='Avg Upload Speed (Mbps)')

# Annotate upload speeds
for i, speed in enumerate(avg_upload_speeds):
    plt.annotate(f'{speed} Mbps', (days[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='blue')

# Plot download speeds
plt.plot(days, avg_download_speeds, marker='o', linestyle='-', color='green', linewidth=2, markersize=8, label='Avg Download Speed (Mbps)')

# Annotate download speeds
for i, speed in enumerate(avg_download_speeds):
    plt.annotate(f'{speed} Mbps', (days[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='green')

# Title and labels
plt.title('Weekly Network Performance Analysis\nAverage Upload and Download Speeds', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Days of the Week', fontsize=14)
plt.ylabel('Speed (Mbps)', fontsize=14)

# Applying Grid
plt.grid(True, linestyle='--', alpha=0.7)

# Customize the y-axis limits
plt.ylim(0, 70)

# Add legend to the plot
plt.legend(loc='upper left', fontsize=12)

# Improve layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()