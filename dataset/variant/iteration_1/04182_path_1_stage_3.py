import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = np.array([45, 60, 75, 85, 30, 95, 110, 130, 150, 160, 170])
wind_energy = np.array([40, 30, 40, 50, 65, 80, 95, 110, 25, 140, 155])
hydro_energy = np.array([25, 20, 25, 30, 35, 40, 40, 45, 50, 55, 60])

fig, ax = plt.subplots(figsize=(14, 8))

# Modified plot style with random alternatives
ax.plot(years, solar_energy, label="Solar", color='orange', marker='x', linestyle='-', linewidth=1.5)
ax.plot(years, wind_energy, label="Wind", color='navy', marker='*', linestyle='--', linewidth=1.5)
ax.plot(years, hydro_energy, label="Hydro", color='purple', marker='d', linestyle='-.', linewidth=1.5)

ax.set_title("Renewable Energy Production (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (MW)', fontsize=14)

plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 201, 20))

# Changed legend style
ax.legend(loc='upper left', shadow=True, fontsize=10)

# Enhanced grid
ax.grid(True, color='gray', linestyle=':', linewidth=0.5, alpha=0.9)

plt.tight_layout()
plt.show()