import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)
solar_energy = np.array([5, 10, 18, 30, 50, 75, 100, 130, 165, 200, 240])
wind_energy = np.array([8, 12, 25, 35, 55, 80, 110, 150, 190, 230, 270])
hydro_energy = np.array([15, 15, 15, 18, 22, 30, 40, 55, 70, 85, 100])

total_renewable_energy = solar_energy + wind_energy + hydro_energy
percentage_growth = np.zeros(len(total_renewable_energy))
percentage_growth[1:] = ((total_renewable_energy[1:] - total_renewable_energy[:-1]) / total_renewable_energy[:-1]) * 100

fig, axes = plt.subplots(2, 1, figsize=(14, 12))

axes[0].bar(years, solar_energy, color='#66bb6a', alpha=0.9)
axes[0].bar(years, wind_energy, bottom=solar_energy, color='#ffa726', alpha=0.9)
axes[0].bar(years, hydro_energy, bottom=solar_energy + wind_energy, color='#42a5f5', alpha=0.9)

axes[0].set_xticks(years)
axes[0].set_xticklabels([])
axes[0].set_ylim(0, 620)
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

axes[1].plot(years, total_renewable_energy, color='purple', marker='o', linewidth=2)
axes[1].plot(years, percentage_growth, color='red', linestyle='--', marker='x', linewidth=1)

axes[1].set_xticks(years)
axes[1].set_xticklabels([])
axes[1].set_ylim(0, max(total_renewable_energy) * 1.2)
axes[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()