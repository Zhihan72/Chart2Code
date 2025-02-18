import matplotlib.pyplot as plt
import numpy as np

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

pm25_concentrations = np.array([55, 60, 52, 45, 50, 65, 70])
pm25_variability = np.array([5, 7, 4, 6, 5, 8, 7])
avg_temperatures = np.array([22, 21, 24, 23, 22, 26, 25])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Swap the colors: Set PM2.5 line to orange and error bars to blue
ax1.errorbar(days, pm25_concentrations, yerr=pm25_variability, fmt='-o',
             ecolor='blue', capsize=5, capthick=2, color='orange', alpha=0.8, label='PM2.5 Levels')

ax1.set_title("Air Quality & Weather Overview:\nPM2.5 Concentration and Temperature Trends", fontsize=14)
ax1.set_xlabel("Day of the Week", fontsize=12)
ax1.set_ylabel("PM2.5 Concentration (µg/m³)", fontsize=12, color='orange')  # Update label color
ax1.set_ylim(35, 80)
ax1.set_yticks(np.arange(35, 85, 5))
ax1.tick_params(axis='y', labelcolor='orange')
ax1.grid(True, linestyle='--', alpha=0.6)

ax2 = ax1.twinx()

# Change the bar color to red
ax2.bar(days, avg_temperatures, color='red', alpha=0.5, width=0.4, label='Average Temperature')
ax2.set_ylabel("Average Temperature (°C)", fontsize=12, color='red')  # Update label color
ax2.set_ylim(20, 30)
ax2.tick_params(axis='y', labelcolor='red')

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()