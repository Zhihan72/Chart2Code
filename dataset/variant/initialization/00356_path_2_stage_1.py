import matplotlib.pyplot as plt
import numpy as np

# Simulated average annual temperature data (in °C) over a decade
years = np.arange(2010, 2020)
average_temperatures = np.array([-10.5, -11.0, -9.8, -10.2, -11.3, -9.7, -10.5, -9.9, -10.1, -9.6])
temperature_std_dev = np.array([0.8, 1.1, 0.6, 0.9, 1.0, 0.7, 0.8, 1.2, 0.7, 0.9])

# Simulated average annual snowfall (in cm) over the same decade
average_snowfall = np.array([150, 160, 140, 155, 165, 135, 145, 150, 152, 148])
snowfall_std_dev = np.array([10, 15, 12, 8, 20, 18, 11, 14, 9, 13])

# Sorting data
temp_indices = np.argsort(average_temperatures) # Ascending sort for temperatures
sorted_years_temp = years[temp_indices]
sorted_temperatures = average_temperatures[temp_indices]
sorted_temp_std_dev = temperature_std_dev[temp_indices]

snow_indices = np.argsort(average_snowfall)[::-1] # Descending sort for snowfall
sorted_years_snow = years[snow_indices]
sorted_snowfall = average_snowfall[snow_indices]
sorted_snowfall_std_dev = snowfall_std_dev[snow_indices]

# Set up the subplots
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plot 1: Sorted Average Annual Temperature as Bar Chart
ax[0].bar(sorted_years_temp, sorted_temperatures, yerr=sorted_temp_std_dev, color='royalblue',
          ecolor='lightcoral', capsize=4, alpha=0.7, label='Avg Temperature ± Std Dev')
ax[0].set_title('Temperature Variability\nin the Arctic Region', fontsize=14, fontweight='bold')
ax[0].set_xlabel('Year', fontsize=12)
ax[0].set_ylabel('Avg Annual Temperature (°C)', fontsize=12)
ax[0].set_ylim(min(sorted_temperatures - sorted_temp_std_dev) - 1, 
               max(sorted_temperatures + sorted_temp_std_dev) + 1)
ax[0].legend(loc='upper right', fontsize=10)
ax[0].grid(True, linestyle='--', alpha=0.6)

# Plot 2: Sorted Average Annual Snowfall as Bar Chart
ax[1].bar(sorted_years_snow, sorted_snowfall, yerr=sorted_snowfall_std_dev, color='cadetblue', 
          alpha=0.7, ecolor='saddlebrown', capsize=4, label='Avg Snowfall ± Std Dev')
ax[1].set_title('Snowfall Trends in the Arctic Region', fontsize=14, fontweight='bold')
ax[1].set_xlabel('Year', fontsize=12)
ax[1].set_ylabel('Avg Annual Snowfall (cm)', fontsize=12)
ax[1].set_ylim(0, max(sorted_snowfall + sorted_snowfall_std_dev) + 20)
ax[1].legend(loc='upper right', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.6)

# Overall title for the entire figure
plt.suptitle('Climate Trends: Analyzing Arctic Temperature and Snowfall Over a Decade', fontsize=16, fontweight='bold', y=1.02)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()