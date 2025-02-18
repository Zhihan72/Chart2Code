import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Seasonal Changes in Temperature and Precipitation Over a Year
# Context: The data represents a year's cycle of temperature and precipitation in a fictional town called 'WeatherVille'.

# Data: Months of the year and corresponding temperature (Celsius) and precipitation (mm).
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_celsius = np.array([-5, -2, 4, 10, 16, 21, 25, 24, 19, 12, 5, -1])
precipitation_mm = np.array([60, 45, 50, 40, 70, 85, 90, 82, 75, 70, 65, 50])

# Create a figure with two y-axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the temperature data
ax1.plot(months, temperature_celsius, color='tab:red', marker='o', linestyle='-', linewidth=2, markersize=6, label='Temperature (°C)')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Temperature (°C)', fontsize=14, color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')
ax1.set_ylim(-10, 30)

# Creating a second y-axis for precipitation
ax2 = ax1.twinx()
ax2.bar(months, precipitation_mm, color='tab:blue', alpha=0.5, label='Precipitation (mm)')
ax2.set_ylabel('Precipitation (mm)', fontsize=14, color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set_ylim(0, 100)

# Adding the title
plt.title('Seasonal Changes in Temperature and Precipitation in WeatherVille\nA Yearly Cycle Overview', fontsize=16, fontweight='bold')

# Adding legends
lines, labels = ax1.get_legend_handles_labels()
bars, bar_labels = ax2.get_legend_handles_labels()
ax1.legend(lines + bars, labels + bar_labels, loc='upper left')

# Adding grid to the plot for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Adjust layout for better fit
plt.tight_layout()

# Display the plot
plt.show()