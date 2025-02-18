import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2026)

# Randomly altered data values within each group while maintaining structure
solar_energy = np.array([
    5, 10, 14, 20, 25, 22, 33, 28, 48, 52,
    62, 65, 85, 82, 93, 105, 125, 135, 155, 175,
    195
])
wind_energy = np.array([
    18, 30, 28, 35, 50, 55, 65, 68, 80, 95,
    115, 125, 130, 155, 160, 175, 190, 205, 220, 240,
    265
])
hydro_energy = np.array([
    28, 32, 42, 46, 52, 65, 75, 78, 95, 98,
    108, 115, 125, 145, 153, 160, 172, 198, 215, 235,
    255
])
biomass_energy = np.array([
    12, 18, 24, 22, 32, 40, 50, 48, 58, 68,
    72, 82, 100, 102, 118, 125, 140, 155, 170, 185,
    206
])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy, 
             colors=['#FF1493', '#4169E1', '#228B22', '#FFA500'], alpha=0.7)

ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 900)

ax.set_xticks(years[::2])
plt.xticks(rotation=45)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()