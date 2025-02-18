import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2023)
traditional_energy = np.array([120, 118, 115, 113, 110, 107, 104, 100, 97, 94, 91, 88, 85, 83, 80, 78, 76, 74, 72, 70, 67, 65, 60])
solar_energy = np.array([0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 50, 55, 60, 65])
wind_energy = np.array([0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 10, 13, 18, 23, 30, 38, 47, 55, 60, 65, 70, 75])
hydro_energy = np.array([10, 10, 11, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 29, 32, 35, 38, 41, 44, 47, 50, 52, 55])

plt.figure(figsize=(14, 8))
plt.plot(years, traditional_energy, color='green', linestyle='-', linewidth=2)
plt.plot(years, solar_energy, color='orange', linestyle='--', linewidth=2)
plt.plot(years, wind_energy, color='blue', linestyle='-.', linewidth=2)
plt.plot(years, hydro_energy, color='purple', linestyle=':', linewidth=2)

plt.title('Energy Use (2000-22)', fontsize=16)
plt.xlabel('Yr', fontsize=12)
plt.ylabel('Energy (GWh)', fontsize=12)

plt.scatter(years, traditional_energy, color='green', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, solar_energy, color='orange', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, wind_energy, color='blue', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, hydro_energy, color='purple', s=50, edgecolors='black', alpha=0.7)

plt.xticks(np.arange(2000, 2023, 2), fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()