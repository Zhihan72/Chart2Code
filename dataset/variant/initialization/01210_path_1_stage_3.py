import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Randomly altered energy values within the same structure
solar_energy = np.array([6, 8, 5, 35, 20, 11, 47, 15, 60, 75, 26])
wind_energy = np.array([12, 15, 20, 80, 25, 52, 40, 33, 65, 100, 10])
hydropower_energy = np.array([42, 41, 35, 36, 32, 38, 40, 39, 44, 30, 37])

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(years, solar_energy, color='gold', edgecolor='black')
ax.bar(years, wind_energy, bottom=solar_energy, color='lightblue', edgecolor='black')
ax.bar(years, hydropower_energy, bottom=solar_energy + wind_energy, color='seagreen', edgecolor='black')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 250, 25))

plt.tight_layout()

plt.show()