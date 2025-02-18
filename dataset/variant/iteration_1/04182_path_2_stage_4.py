import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Randomly altered energy data while preserving dimensions
solar_energy = np.array([30, 90, 70, 65, 95, 60, 110, 120, 160, 170, 105])
wind_energy = np.array([25, 50, 60, 45, 55, 85, 100, 130, 110, 150, 140])
hydro_energy = np.array([20, 30, 20, 35, 35, 50, 45, 40, 55, 60, 50])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_energy, label="Solar Energy", color='magenta', marker='D', linestyle='solid', linewidth=2)
ax.plot(years, wind_energy, label="Wind Energy", color='limegreen', marker='x', linestyle='dashdot', linewidth=2)
ax.plot(years, hydro_energy, label="Hydro Energy", color='navy', marker='v', linestyle='dotted', linewidth=2)

ax.set_title("Greenvilla Energy (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Production (MW)', fontsize=14)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 201, 20))

ax.legend(title='Energy Source', fontsize=12, loc='upper left', frameon=False)
ax.grid(True, linestyle=':', linewidth=1.0, alpha=0.5)

plt.tight_layout()
plt.show()