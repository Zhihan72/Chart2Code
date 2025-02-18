import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2026)

solar_energy = np.array([
    5, 7, 12, 18, 20, 25, 30, 35, 45, 50, 
    60, 70, 75, 85, 95, 110, 130, 145, 160, 180, 
    200
])
wind_energy = np.array([
    20, 25, 30, 40, 45, 50, 60, 70, 85, 100,
    110, 120, 135, 150, 165, 180, 195, 210, 230, 250,
    270
])
hydro_energy = np.array([
    30, 35, 40, 50, 55, 60, 70, 80, 90, 100,
    110, 120, 130, 140, 150, 165, 180, 200, 220, 240,
    260
])
biomass_energy = np.array([
    10, 15, 20, 25, 30, 35, 45, 50, 60, 70,
    75, 85, 95, 105, 115, 130, 145, 160, 175, 190,
    210
])

fig, ax = plt.subplots(figsize=(14, 7))

# New set of colors: deep pink, royal blue, forest green, orange
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy, 
             colors=['#FF1493', '#4169E1', '#228B22', '#FFA500'], alpha=0.7)

ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 900)

ax.set_xticks(years[::2])
plt.xticks(rotation=45)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()