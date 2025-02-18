import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
avg_upload_speeds = [10, 15, 12, 20, 18, 8, 25]  # Average upload speeds (Mbps)
avg_download_speeds = [50, 48, 52, 55, 53, 60, 58]  # Average download speeds (Mbps)

plt.figure(figsize=(14, 8))

# Plot upload speeds
plt.plot(days, avg_upload_speeds, marker='s', linestyle='--', color='purple', linewidth=3, markersize=10, label='Upload Speed')

# Annotate upload speeds
for i, speed in enumerate(avg_upload_speeds):
    plt.annotate(f'{speed}', (days[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='purple')

# Plot download speeds
plt.plot(days, avg_download_speeds, marker='^', linestyle='-.', color='orange', linewidth=3, markersize=10, label='Download Speed')

# Annotate download speeds
for i, speed in enumerate(avg_download_speeds):
    plt.annotate(f'{speed}', (days[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='orange')

# Title and labels
plt.title('Weekly Network Performance', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Days of the Week', fontsize=14)
plt.ylabel('Speed', fontsize=14)

# Grid and borders
plt.grid(True, linestyle=':', alpha=0.5)
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')

# Customize the y-axis limits
plt.ylim(0, 70)

# Legend placement and style
plt.legend(loc='lower right', fontsize=12, edgecolor='black')

plt.tight_layout()
plt.show()