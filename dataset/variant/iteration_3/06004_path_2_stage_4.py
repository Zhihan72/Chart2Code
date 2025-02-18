import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 
    'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

water_levels = np.array([1.5, 1.7, 1.8, 2.0, 2.1, 2.2, 2.5, 2.3, 2.1, 1.9, 1.6, 1.4])
temperatures = np.array([2, 3, 8, 15, 20, 25, 28, 27, 22, 16, 9, 4])
rainfall = np.array([78, 56, 92, 110, 150, 180, 210, 205, 190, 130, 90, 70])
humidity = np.array([85, 80, 75, 70, 65, 60, 55, 50, 55, 65, 75, 85])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, water_levels, color='blue', marker='x', linestyle='--', linewidth=2, markersize=10, label='Water (m)')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Water (m)', fontsize=12, color='blue')
ax1.tick_params(axis='y', colors='blue')
ax1.set_ylim(0, 3)
ax1.grid(axis='x', linestyle=':', alpha=0.7)

ax2 = ax1.twinx()
ax2.plot(months, temperatures, color='red', marker='d', linestyle='-.', linewidth=2, markersize=10, label='Temp (°C)')
ax2.set_ylabel('Temp (°C)', fontsize=12, color='red')
ax2.tick_params(axis='y', colors='red')
ax2.set_ylim(0, 30)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(months, rainfall, color='green', marker='o', linestyle='-', linewidth=2, markersize=8, label='Rainfall (mm)')
ax3.set_ylabel('Rainfall (mm)', fontsize=12, color='green')
ax3.tick_params(axis='y', colors='green')
ax3.set_ylim(0, 250)

ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
ax4.plot(months, humidity, color='purple', marker='s', linestyle='--', linewidth=2, markersize=8, label='Humidity (%)')
ax4.set_ylabel('Humidity (%)', fontsize=12, color='purple')
ax4.tick_params(axis='y', colors='purple')
ax4.set_ylim(0, 100)

plt.title('Lake Observation: Monthly Metrics', fontsize=16, fontweight='bold')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
lines4, labels4 = ax4.get_legend_handles_labels()
ax1.legend(lines + lines2 + lines3 + lines4, labels + labels2 + labels3 + labels4, loc='lower right', fontsize=10)

for spine in ax1.spines.values():
    spine.set_edgecolor('purple')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()