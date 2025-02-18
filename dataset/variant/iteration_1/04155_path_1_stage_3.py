import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1990, 2021)
solar_energy = np.array([0.2, 0.3, 0.4, 0.6, 0.8, 1, 1.2, 1.5, 2.0, 2.5, 3.0, 3.8, 4.4, 5.0, 6, 7, 10, 15, 22, 30, 35, 50, 65, 80, 100, 120, 150, 180, 210, 240, 280])
wind_energy = np.array([0.1, 0.15, 0.2, 0.4, 0.6, 0.9, 1.3, 1.7, 2.3, 3, 4, 5, 7, 8, 10, 12, 14, 16, 20, 25, 30, 35, 40, 50, 65, 80, 95, 120, 140, 160, 180])
hydro_energy = np.array([25, 25.3, 25.6, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30, 31, 31.5, 32, 32.5, 33, 33.6, 34, 34.5, 35, 35.4, 35.8, 36, 36.5, 37, 37.2, 37.5, 37.8, 38, 38.3])
geothermal_energy = np.array([1.2, 1.3, 1.4, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5, 2.8, 3.1, 3.4, 3.6, 4, 4.3, 4.7, 5, 5.5, 6, 6.4, 6.8, 7.2, 7.5, 8, 8.5, 9, 10, 10.5, 11, 12, 13])
biomass_energy = np.array([5, 5.2, 5.5, 5.8, 6, 6.3, 6.6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.6, 11.2, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 24, 26, 28, 30, 32])

plt.figure(figsize=(14, 8))

plt.plot(years, solar_energy, color='purple', linestyle='-', linewidth=2, marker='o', label='Sun Power')
plt.plot(years, wind_energy, color='brown', linestyle='-', linewidth=2, marker='s', label='Breeze Energy')
plt.plot(years, hydro_energy, color='grey', linestyle='-', linewidth=2, marker='^', label='Water Force')
plt.plot(years, geothermal_energy, color='pink', linestyle='-', linewidth=2, marker='d', label='Earth Heat')
plt.plot(years, biomass_energy, color='orange', linestyle='-', linewidth=2, marker='x', label='Green Mass')

plt.title('Evolution of Sustainable Energy: 1990 – 2020', fontsize=16, weight='bold', pad=20)
plt.xlabel('Calendar Year', fontsize=12)
plt.ylabel('Power Consumption (TWh)', fontsize=12)

plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(years[::2], rotation=45)
plt.yticks(np.arange(0, 305, 20))

plt.legend(title='Eco Energy Sources', loc='upper left', fontsize=10)

plt.annotate('Sun surpasses Breeze', xy=(2015, 50), xytext=(2010, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

plt.annotate('Earth hits 10 TWh', xy=(2000, 9), xytext=(1995, 12),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

plt.tight_layout()

plt.show()