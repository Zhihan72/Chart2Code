import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([5, 10, 15, 20, 30, 40, 55, 70, 80, 90, 100])
wind_energy = np.array([12, 18, 25, 30, 35, 45, 58, 75, 85, 95, 110])
hydro_energy = np.array([20, 22, 25, 27, 30, 33, 36, 38, 41, 43, 45])
total_energy = solar_energy + wind_energy + hydro_energy

plt.figure(figsize=(12, 7))
common_color = 'purple'
plt.plot(years, solar_energy, color=common_color, linestyle='--', marker='o', linewidth=2)
plt.plot(years, wind_energy, color=common_color, linestyle='-.', marker='s', linewidth=2)
plt.plot(years, hydro_energy, color=common_color, linestyle=':', marker='^', linewidth=2)
plt.plot(years, total_energy, color=common_color, linestyle='-', marker='d', linewidth=2)

plt.title('Energy Expansion in Sunland (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Output (Megawatts)', fontsize=12)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 201, 20))

plt.tight_layout()
plt.show()