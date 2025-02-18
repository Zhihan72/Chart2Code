import matplotlib.pyplot as plt
import numpy as np

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Modified monthly rainfall data (in mm)
rainfall = [65, 45, 75, 95, 125, 155, 175, 155, 145, 105, 85, 65]

# Modified monthly average temperature data (in Celsius)
avg_temperature = [4, 8, 11, 14, 21, 24, 29, 26, 23, 16, 13, 6]

fig, ax1 = plt.subplots(figsize=(14, 8))

color_rainfall = 'forestgreen'
ax1.set_xlabel('Month')
ax1.set_ylabel('Rainfall (mm)', color=color_rainfall)
ax1.plot(months, rainfall, marker='o', linestyle='-', color=color_rainfall, linewidth=2, label='Monthly Rainfall')
ax1.tick_params(axis='y', labelcolor=color_rainfall)
ax1.legend(loc='upper left', fontsize=10)
ax1.set_title("Monthly Rainfall and Average Temperature Trends in RiverTown, 2021", fontsize=16, fontweight='bold', pad=20)

ax2 = ax1.twinx()
color_temperature = 'darkorange'
ax2.set_ylabel('Average Temperature (°C)', color=color_temperature)
ax2.plot(months, avg_temperature, marker='s', linestyle='--', color=color_temperature, linewidth=2, label='Average Temperature (°C)')
ax2.tick_params(axis='y', labelcolor=color_temperature)
ax2.legend(loc='upper right', fontsize=10)

ax1.grid(True, linestyle='--', alpha=0.7)

peak_rainfall_month = 'Jul'
peak_rainfall = rainfall[months.index(peak_rainfall_month)]
ax1.annotate('Peak Rainfall\n175 mm in July', xy=(peak_rainfall_month, peak_rainfall), xytext=(peak_rainfall_month, peak_rainfall+30),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color=color_rainfall)

lowest_temp_month = 'Jan'
lowest_temp = avg_temperature[months.index(lowest_temp_month)]
ax2.annotate('Lowest Temp\n4°C in January', xy=(lowest_temp_month, lowest_temp), xytext=('Feb', lowest_temp-10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color=color_temperature)

fig.tight_layout()
plt.show()