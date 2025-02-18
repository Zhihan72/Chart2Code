import matplotlib.pyplot as plt
import numpy as np

# Data: Annual average temperatures in GreenValley for each season from 2015 to 2023
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
spring_temps = np.array([15.2, 15.8, 16.3, 16.9, 17.2, 17.6, 18.1, 18.4, 18.7])
summer_temps = np.array([23.4, 24.1, 24.5, 25.0, 25.3, 25.9, 26.2, 26.5, 26.8])
autumn_temps = np.array([17.8, 18.2, 18.7, 19.0, 19.2, 19.6, 20.0, 20.3, 20.5])
winter_temps = np.array([5.3, 5.7, 6.1, 6.5, 6.8, 7.2, 7.5, 7.9, 8.2])

colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

plt.figure(figsize=(14, 8))

plt.plot(years, spring_temps, color=colors[0], marker='o', linestyle='-', linewidth=2, markersize=6, label='Spring')
plt.plot(years, summer_temps, color=colors[1], marker='o', linestyle='-', linewidth=2, markersize=6, label='Summer')
plt.plot(years, autumn_temps, color=colors[2], marker='o', linestyle='-', linewidth=2, markersize=6, label='Autumn')
plt.plot(years, winter_temps, color=colors[3], marker='o', linestyle='-', linewidth=2, markersize=6, label='Winter')

plt.title('Climate Trends in GreenValley:\nAverage Seasonal Temperatures (2015-2023)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Temperature (°C)', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left', title="Seasons", fontsize=12)
plt.xticks(years)
plt.tight_layout()

plt.show()