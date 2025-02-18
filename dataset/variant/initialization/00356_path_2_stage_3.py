import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
average_temperatures = np.array([-10.5, -11.0, -9.8, -10.2, -11.3, -9.7, -10.5, -9.9, -10.1, -9.6])
temperature_std_dev = np.array([0.8, 1.1, 0.6, 0.9, 1.0, 0.7, 0.8, 1.2, 0.7, 0.9])

average_snowfall = np.array([150, 160, 140, 155, 165, 135, 145, 150, 152, 148])
snowfall_std_dev = np.array([10, 15, 12, 8, 20, 18, 11, 14, 9, 13])

temp_indices = np.argsort(average_temperatures)
sorted_years_temp = years[temp_indices]
sorted_temperatures = average_temperatures[temp_indices]
sorted_temp_std_dev = temperature_std_dev[temp_indices]

snow_indices = np.argsort(average_snowfall)[::-1]
sorted_years_snow = years[snow_indices]
sorted_snowfall = average_snowfall[snow_indices]
sorted_snowfall_std_dev = snowfall_std_dev[snow_indices]

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))

# Plot 1: Sorted Average Annual Temperature as Bar Chart
ax[0].bar(sorted_years_temp, sorted_temperatures, yerr=sorted_temp_std_dev, color='firebrick',
          ecolor='orangered', capsize=5, alpha=0.8)
ax[0].set_ylim(min(sorted_temperatures - sorted_temp_std_dev) - 1, 
               max(sorted_temperatures + sorted_temp_std_dev) + 1)
ax[0].grid(False)  # Disabled grid
ax[0].spines['top'].set_visible(False)  # Removed top border

# Plot 2: Sorted Average Annual Snowfall as Bar Chart
ax[1].bar(sorted_years_snow, sorted_snowfall, yerr=sorted_snowfall_std_dev, color='seagreen', 
          alpha=0.7, ecolor='darkgreen', capsize=3, hatch='/')
ax[1].set_ylim(0, max(sorted_snowfall + sorted_snowfall_std_dev) + 20)
ax[1].grid(True, linestyle=':', alpha=0.8)  # Changed grid line style
ax[1].spines['right'].set_visible(False)  # Removed right border

plt.tight_layout()
plt.show()