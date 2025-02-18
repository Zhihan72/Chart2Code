import matplotlib.pyplot as plt
import numpy as np

# Years from 1990 to 2020
years = np.arange(1990, 2021)

# Average temperatures (in °C) for each season over the years
spring_temps = [12, 14, 13, 14, 12, 15, 15, 13, 16, 17, 17, 18, 18, 19, 20, 20, 21, 21, 22, 23, 23, 24, 24, 25, 25, 26, 27, 29, 28, 27, 29]
summer_temps = [24, 25, 26, 24, 25, 26, 27, 28, 29, 30, 30, 31, 32, 32, 33, 34, 34, 35, 36, 37, 37, 43, 38, 39, 40, 40, 41, 41, 42, 38, 43]
autumn_temps = [15, 16, 17, 15, 16, 17, 18, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 25, 26, 27, 27, 28, 28, 33, 30, 30, 31, 31, 32, 29, 33]
winter_temps = [5, 6, 7, 5, 6, 7, 8, 9, 9, 10, 10, 11, 11, 12, 13, 13, 14, 14, 15, 16, 16, 21, 17, 18, 19, 19, 20, 20, 22, 17, 22]

fig, ax = plt.subplots(figsize=(12, 5))
fig.suptitle('Average Temperatures Across Seasons in Verdad Valley\n1990-2020', fontsize=18, fontweight='bold', y=0.94)

# Stacked Area Chart
ax.stackplot(years, spring_temps, summer_temps, autumn_temps, winter_temps,
             labels=['Spring', 'Summer', 'Autumn', 'Winter'],
             colors=['#66b3ff', '#99ff99', '#ffcc99', '#ff9999'], alpha=0.85)
ax.set_title('Seasonal Temperature Trends', fontsize=16, pad=10)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Temperature (°C)', fontsize=14)
ax.legend(loc='upper right', title='Seasons', fontsize=10, frameon=False)
ax.grid(axis='x', linestyle=':', alpha=0.5)
ax.set_xticks(years[::2])
ax.set_xticklabels(years[::2], rotation=30, fontsize=12)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()