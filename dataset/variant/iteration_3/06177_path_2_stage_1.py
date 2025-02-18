import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
avg_temps = np.array([5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6])
precipitation = np.array([70, 55, 60, 80, 90, 100, 45, 40, 75, 85, 95, 80])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Use a single color for both data sets
color = 'tab:green'

ax1.plot(months, avg_temps, color=color, marker='o', linestyle='-', linewidth=2, label='Average Temperature (°C)')
ax1.set_title('Seasonal Changes in Coastal Town: Temperature and Precipitation', fontsize=16, pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
ax2.plot(months, precipitation, color=color, marker='s', linestyle='--', linewidth=2, label='Precipitation (mm)')
ax2.set_ylabel('Precipitation (mm)', fontsize=12, color=color)
ax2.tick_params(axis='y', labelcolor=color)

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(True, linestyle='--', alpha=0.5)

ax1.annotate('Peak Summer Heat', xy=('Jul', 28), xytext=('May', 30),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax2.annotate('Heavy Rain Season', xy=('Jun', 100), xytext=('Mar', 110),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()