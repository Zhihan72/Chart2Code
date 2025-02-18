import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = np.array([5, 6, 8, 11, 15, 20, 26, 35, 47, 60, 75])
wind_energy = np.array([10, 12, 15, 20, 25, 33, 40, 52, 65, 80, 100])
hydropower_energy = np.array([30, 32, 35, 36, 37, 38, 39, 40, 41, 42, 44])

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, solar_energy, color='gold', edgecolor='black')
ax.bar(years, wind_energy, bottom=solar_energy, color='lightblue', edgecolor='black')
ax.bar(years, hydropower_energy, bottom=solar_energy + wind_energy, color='seagreen', edgecolor='black')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 250, 25))

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()

plt.show()