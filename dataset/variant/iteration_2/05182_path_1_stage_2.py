import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_celsius = np.array([-5, -2, 4, 10, 16, 21, 25, 24, 19, 12, 5, -1])
precipitation_mm = np.array([60, 45, 50, 40, 70, 85, 90, 82, 75, 70, 65, 50])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(months, temperature_celsius, color='forestgreen', marker='o', linestyle='-', linewidth=2, markersize=6, label='Temp (°C)')
ax1.set_xlabel('Mon', fontsize=14)
ax1.set_ylabel('Temp (°C)', fontsize=14, color='forestgreen')
ax1.tick_params(axis='y', labelcolor='forestgreen')
ax1.set_ylim(-10, 30)

ax2 = ax1.twinx()
ax2.bar(months, precipitation_mm, color='mediumslateblue', alpha=0.5, label='Precip (mm)')
ax2.set_ylabel('Precip (mm)', fontsize=14, color='mediumslateblue')
ax2.tick_params(axis='y', labelcolor='mediumslateblue')
ax2.set_ylim(0, 100)

plt.title('WeatherVille Annual Weather', fontsize=16, fontweight='bold')

lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, loc='upper left')

ax1.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()