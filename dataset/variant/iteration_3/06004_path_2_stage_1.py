import matplotlib.pyplot as plt
import numpy as np

months = np.array([
    'January', 'February', 'March', 'April', 'May', 'June', 'July', 
    'August', 'September', 'October', 'November', 'December'])

water_levels = np.array([1.5, 1.7, 1.8, 2.0, 2.1, 2.2, 2.5, 2.3, 2.1, 1.9, 1.6, 1.4])
temperatures = np.array([2, 3, 8, 15, 20, 25, 28, 27, 22, 16, 9, 4])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, water_levels, color='green', marker='o', linestyle='-', linewidth=2, markersize=8, label='Water Level (meters)')
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Water Level (meters)', fontsize=12)
ax1.tick_params(axis='y', colors='green')
ax1.set_ylim(0, 3)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(months, temperatures, color='green', marker='s', linestyle='-', linewidth=2, markersize=8, label='Temperature (°C)')
ax2.set_ylabel('Temperature (°C)', fontsize=12)
ax2.tick_params(axis='y', colors='green')
ax2.set_ylim(0, 30)

plt.title('Lake Observation: Monthly Water Level and Temperature Changes', fontsize=16, fontweight='bold')

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines + lines2, labels + labels2, loc='upper left', fontsize=10)

max_level_month = months[np.argmax(water_levels)]
max_level_value = water_levels.max()
min_level_month = months[np.argmin(water_levels)]
min_level_value = water_levels.min()

max_temp_month = months[np.argmax(temperatures)]
max_temp_value = temperatures.max()
min_temp_month = months[np.argmin(temperatures)]
min_temp_value = temperatures.min()

ax1.annotate(f'Highest Water Level ({max_level_value}m)', xy=(max_level_month, max_level_value), xytext=(max_level_month, max_level_value+0.5),
             arrowprops=dict(facecolor='green', shrink=0.1), fontsize=10, color='green', ha='center')
ax1.annotate(f'Lowest Water Level ({min_level_value}m)', xy=(min_level_month, min_level_value), xytext=(min_level_month, min_level_value-0.5),
             arrowprops=dict(facecolor='green', shrink=0.1), fontsize=10, color='green', ha='center')

ax2.annotate(f'Highest Temperature ({max_temp_value}°C)', xy=(max_temp_month, max_temp_value), xytext=(max_temp_month, max_temp_value+5),
             arrowprops=dict(facecolor='green', shrink=0.1), fontsize=10, color='green', ha='center')
ax2.annotate(f'Lowest Temperature ({min_temp_value}°C)', xy=(min_temp_month, min_temp_value), xytext=(min_temp_month, min_temp_value-5),
             arrowprops=dict(facecolor='green', shrink=0.1), fontsize=10, color='green', ha='center')

plt.tight_layout()
plt.show()