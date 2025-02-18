import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021])

# Manually permuted temperature values
spring_temps = np.array([16.3, 15.8, 18.1, 17.6, 15.2, 16.9, 17.2])
summer_temps = np.array([24.5, 23.4, 26.2, 25.0, 25.3, 24.1, 25.9])
autumn_temps = np.array([18.2, 19.0, 17.8, 20.0, 18.7, 19.2, 19.6])
winter_temps = np.array([7.5, 6.5, 5.3, 7.2, 5.7, 6.8, 6.1])

colors = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3']

plt.figure(figsize=(14, 8))

plt.plot(years, spring_temps, color=colors[0], marker='o', linestyle='-', linewidth=2, markersize=6, label='Spr')
plt.plot(years, summer_temps, color=colors[1], marker='o', linestyle='-', linewidth=2, markersize=6, label='Sum')
plt.plot(years, autumn_temps, color=colors[2], marker='o', linestyle='-', linewidth=2, markersize=6, label='Aut')
plt.plot(years, winter_temps, color=colors[3], marker='o', linestyle='-', linewidth=2, markersize=6, label='Win')

plt.title('GreenValley: Avg Seasonal Temps (2015-2021)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Yr', fontsize=14)
plt.ylabel('Avg Temp (°C)', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(loc='upper left', title="Ssn", fontsize=12)

plt.xticks(years)

plt.tight_layout()

plt.show()