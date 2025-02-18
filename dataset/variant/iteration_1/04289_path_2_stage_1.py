import matplotlib.pyplot as plt
import numpy as np

# Define the months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Monthly rainfall data (in mm)
rainfall = [60, 50, 70, 100, 120, 150, 180, 160, 140, 110, 80, 70]

# Monthly average temperature data (in Celsius)
avg_temperature = [5, 7, 10, 15, 20, 25, 28, 27, 22, 17, 12, 7]

# Plotting the data
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting rainfall on primary y-axis
color_rainfall = 'forestgreen'
ax1.set_xlabel('Month')
ax1.set_ylabel('Rainfall (mm)', color=color_rainfall)
ax1.plot(months, rainfall, marker='o', linestyle='-', color=color_rainfall, linewidth=2, label='Monthly Rainfall')
ax1.tick_params(axis='y', labelcolor=color_rainfall)
ax1.legend(loc='upper left', fontsize=10)
ax1.set_title("Monthly Rainfall and Average Temperature Trends in RiverTown, 2021", fontsize=16, fontweight='bold', pad=20)

# Adding a secondary y-axis for temperature
ax2 = ax1.twinx()
color_temperature = 'darkorange'
ax2.set_ylabel('Average Temperature (°C)', color=color_temperature)
ax2.plot(months, avg_temperature, marker='s', linestyle='--', color=color_temperature, linewidth=2, label='Average Temperature (°C)')
ax2.tick_params(axis='y', labelcolor=color_temperature)
ax2.legend(loc='upper right', fontsize=10)

# Adding grid only on primary y-axis
ax1.grid(True, linestyle='--', alpha=0.7)

# Annotating significant points
peak_rainfall_month = 'Jul'
peak_rainfall = rainfall[months.index(peak_rainfall_month)]
ax1.annotate('Peak Rainfall\n180 mm in July', xy=(peak_rainfall_month, peak_rainfall), xytext=(peak_rainfall_month, peak_rainfall+30),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color=color_rainfall)

lowest_temp_month = 'Jan'
lowest_temp = avg_temperature[months.index(lowest_temp_month)]
ax2.annotate('Lowest Temp\n5°C in January', xy=(lowest_temp_month, lowest_temp), xytext=('Feb', lowest_temp-10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10, ha='center', color=color_temperature)

# Adjust layout to prevent clipping
fig.tight_layout()

# Display the chart
plt.show()