import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
avg_temps = np.array([5, 7, 10, 15, 20, 25, 28, 27, 22, 16, 10, 6])
precipitation = np.array([70, 55, 60, 80, 90, 100, 45, 40, 75, 85, 95, 80])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Use different colors and styles for each data set
color_temp = 'tab:blue'
color_precip = 'tab:orange'

ax1.plot(months, avg_temps, color=color_temp, marker='^', linestyle='-.', linewidth=2, label='Average Temperature (°C)')
ax1.set_title('Seasonal Changes in Coastal Town: Temperature and Precipitation', fontsize=16, pad=20)
ax1.set_xlabel('Month', fontsize=12)
ax1.set_ylabel('Temperature (°C)', fontsize=12, color=color_temp)
ax1.tick_params(axis='y', labelcolor=color_temp)

ax2 = ax1.twinx()
ax2.plot(months, precipitation, color=color_precip, marker='d', linestyle=':', linewidth=2, label='Precipitation (mm)')
ax2.set_ylabel('Precipitation (mm)', fontsize=12, color=color_precip)
ax2.tick_params(axis='y', labelcolor=color_precip)

ax1.legend(loc='lower left')
ax2.legend(loc='lower right')
ax1.grid(True, linestyle='-', color='gray', alpha=0.3)

ax1.annotate('Peak Summer Heat', xy=('Jul', 28), xytext=('Sep', 30),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10)
ax2.annotate('Heavy Rain Season', xy=('Jun', 100), xytext=('Aug', 110),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()