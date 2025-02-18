import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
average_temperatures = np.array([-10.5, -11.0, -9.8, -10.2, -11.3, -9.7, -10.5, -9.9, -10.1, -9.6])
temperature_std_dev = np.array([0.8, 1.1, 0.6, 0.9, 1.0, 0.7, 0.8, 1.2, 0.7, 0.9])

average_snowfall = np.array([150, 160, 140, 155, 165, 135, 145, 150, 152, 148])
snowfall_std_dev = np.array([10, 15, 12, 8, 20, 18, 11, 14, 9, 13])

average_rainfall = np.array([20, 30, 25, 35, 20, 28, 30, 33, 29, 31])
rainfall_std_dev = np.array([3, 5, 4, 6, 3, 4, 5, 3, 4, 5])

temp_sorted_indices = np.argsort(average_temperatures)
snow_sorted_indices = np.argsort(average_snowfall)
rain_sorted_indices = np.argsort(average_rainfall)

sorted_years_temp = years[temp_sorted_indices]
sorted_temperatures = average_temperatures[temp_sorted_indices]
sorted_temperature_std_dev = temperature_std_dev[temp_sorted_indices]

sorted_years_snow = years[snow_sorted_indices]
sorted_snowfall = average_snowfall[snow_sorted_indices]
sorted_snowfall_std_dev = snowfall_std_dev[snow_sorted_indices]

sorted_years_rain = years[rain_sorted_indices]
sorted_rainfall = average_rainfall[rain_sorted_indices]
sorted_rainfall_std_dev = rainfall_std_dev[rain_sorted_indices]

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(8, 24))

ax[0].bar(sorted_years_temp, sorted_temperatures, yerr=sorted_temperature_std_dev, color='royalblue',
          alpha=0.7, ecolor='lightcoral', capsize=4)
ax[0].set_ylim(min(sorted_temperatures - sorted_temperature_std_dev) - 1, 
               max(sorted_temperatures + sorted_temperature_std_dev) + 1)
ax[0].grid(True, linestyle='--', alpha=0.6)

ax[1].bar(sorted_years_snow, sorted_snowfall, yerr=sorted_snowfall_std_dev, color='cadetblue', 
          alpha=0.7, ecolor='saddlebrown', capsize=4)
ax[1].set_ylim(0, max(sorted_snowfall + sorted_snowfall_std_dev) + 20)
ax[1].grid(True, linestyle='--', alpha=0.6)

ax[2].bar(sorted_years_rain, sorted_rainfall, yerr=sorted_rainfall_std_dev, color='seagreen',
          alpha=0.7, ecolor='darkgreen', capsize=4)
ax[2].set_ylim(0, max(sorted_rainfall + sorted_rainfall_std_dev) + 10)
ax[2].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()