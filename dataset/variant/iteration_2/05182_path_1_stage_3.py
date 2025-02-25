import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_celsius = np.array([-5, -2, 4, 10, 16, 21, 25, 24, 19, 12, 5, -1])
precipitation_mm = np.array([60, 45, 50, 40, 70, 85, 90, 82, 75, 70, 65, 50])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Altered style: Changed marker, line style, and color for temperature
ax1.plot(months, temperature_celsius, color='darkorange', marker='s', linestyle='--', linewidth=2, markersize=8, label='Temp (°C)')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14, color='darkorange')
ax1.tick_params(axis='y', labelcolor='darkorange')
ax1.set_ylim(-10, 30)

ax2 = ax1.twinx()
# Altered style: Changed bar color and alpha for precipitation
ax2.bar(months, precipitation_mm, color='cornflowerblue', alpha=0.7, label='Precipitation (mm)')
ax2.set_ylabel('Precipitation (mm)', fontsize=14, color='cornflowerblue')
ax2.tick_params(axis='y', labelcolor='cornflowerblue')
ax2.set_ylim(0, 100)

plt.title('WeatherVille Annual Weather', fontsize=16, fontweight='bold')

# Changed legend location
lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, loc='upper right')

# Altered grid style
ax1.grid(True, linestyle=':', alpha=0.8)
plt.tight_layout()
plt.show()