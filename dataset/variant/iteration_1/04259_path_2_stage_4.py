import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
spring_temps = np.array([15.2, 15.8, 16.3, 16.9, 17.2, 17.6, 18.1, 18.4, 18.7])
summer_temps = np.array([23.4, 24.1, 24.5, 25.0, 25.3, 25.9, 26.2, 26.5, 26.8])
autumn_temps = np.array([17.8, 18.2, 18.7, 19.0, 19.2, 19.6, 20.0, 20.3, 20.5])
winter_temps = np.array([5.3, 5.7, 6.1, 6.5, 6.8, 7.2, 7.5, 7.9, 8.2])

single_color = '#66c2a5'  # Consistent color for all data groups

plt.figure(figsize=(14, 8))

plt.plot(years, spring_temps, color=single_color, marker='o', linestyle='-', linewidth=2, markersize=6)
plt.plot(years, summer_temps, color=single_color, marker='o', linestyle='-', linewidth=2, markersize=6)
plt.plot(years, autumn_temps, color=single_color, marker='o', linestyle='-', linewidth=2, markersize=6)
plt.plot(years, winter_temps, color=single_color, marker='o', linestyle='-', linewidth=2, markersize=6)

plt.title('Atmospheric Evolutions:\nYearly Season Temps (2015-2023)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Timeline', fontsize=14)
plt.ylabel('Mean Temp (°C)', fontsize=14)

plt.xticks(years)
plt.tight_layout()

plt.show()