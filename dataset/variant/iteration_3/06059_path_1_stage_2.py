import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Average temperatures (in °C) for each season over the years
spring_temps = [12, 14, 13, 14, 12, 15, 15, 13, 16, 17, 17, 18, 18, 19, 20, 20, 21, 21, 22, 23, 23, 24, 24, 25, 25, 26, 27, 29, 28, 27, 29]
summer_temps = [24, 25, 26, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 37, 43, 38, 39, 40, 40, 41, 41, 42, 38, 43]
autumn_temps = [15, 16, 17, 15, 16, 17, 18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25, 26, 27, 27, 28, 28, 33, 30, 30, 31, 31, 32, 29, 33]
winter_temps = [5, 6, 7, 5, 6, 7, 8, 9, 9, 10, 10, 11, 11, 12, 13, 13, 14, 14, 15, 16, 16, 21, 17, 18, 19, 19, 20, 20, 22, 17, 22]

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
fig.suptitle('Average Temperatures Across Seasons in Verdad Valley\n1990-2020', fontsize=18, fontweight='bold', y=0.94)

# Stacked Area Chart
axs[0].stackplot(years, spring_temps, summer_temps, autumn_temps, winter_temps,
                labels=['Spring', 'Summer', 'Autumn', 'Winter'],
                colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9999'], alpha=0.85)
axs[0].set_title('Seasonal Temperature Trends', fontsize=16, pad=10)
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Temperature (°C)', fontsize=14)
axs[0].legend(loc='upper right', title='Seasons', fontsize=10, frameon=False)
axs[0].grid(axis='x', linestyle=':', alpha=0.5)
axs[0].set_xticks(years[::2])
axs[0].set_xticklabels(years[::2], rotation=30, fontsize=12)

# Subplot for Yearly Temperature Averages Comparison
average_temps = (np.array(spring_temps) + np.array(summer_temps) + np.array(autumn_temps) + np.array(winter_temps)) / 4
axs[1].plot(years, average_temps, linestyle='-.', marker='s', color='g', label='Average Yearly Temperature')
axs[1].fill_between(years, average_temps, color='lightgreen', alpha=0.6)
axs[1].set_title('Yearly Average Temperature in Verdad Valley', fontsize=16, pad=10)
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Temperature (°C)', fontsize=14)
axs[1].legend(loc='lower right', fontsize=10, frameon=False)
axs[1].grid(axis='y', linestyle='-.', alpha=0.8)
axs[1].set_xticks(years[::2])
axs[1].set_xticklabels(years[::2], rotation=45, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()