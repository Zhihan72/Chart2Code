import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Randomly altered content within the speed data groups
avg_upload_speeds = [12, 18, 15, 25, 10, 20, 8]
avg_download_speeds = [55, 50, 60, 52, 48, 58, 53]

plt.figure(figsize=(14, 8))

# Plot upload speeds
plt.plot(days, avg_upload_speeds, marker='s', linestyle='--', color='orange', linewidth=3, markersize=10, label='Upload Speed')

# Annotate upload speeds
for i, speed in enumerate(avg_upload_speeds):
    plt.annotate(f'{speed}', (days[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='orange')

# Plot download speeds
plt.plot(days, avg_download_speeds, marker='^', linestyle='-.', color='purple', linewidth=3, markersize=10, label='Download Speed')

# Annotate download speeds
for i, speed in enumerate(avg_download_speeds):
    plt.annotate(f'{speed}', (days[i], speed), textcoords="offset points", xytext=(-10, 10), ha='center', color='purple')

plt.title('Weekly Network Performance', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Days of the Week', fontsize=14)
plt.ylabel('Speed', fontsize=14)
plt.grid(True, linestyle=':', alpha=0.5)
plt.gca().spines['top'].set_color('none')
plt.gca().spines['right'].set_color('none')
plt.ylim(0, 70)
plt.legend(loc='lower right', fontsize=12, edgecolor='black')

plt.tight_layout()
plt.show()