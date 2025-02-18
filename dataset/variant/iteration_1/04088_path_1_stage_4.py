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
geothermal_energy = np.array([
    2, 4, 6, 8, 10, 12, 14, 18, 22, 28, 
    33, 38, 44, 50, 58, 65, 75, 85, 95, 110,
    125
])

fig, ax = plt.subplots(figsize=(14, 7))

ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy,
             colors=['#FF6347', '#00FF7F', '#FFD700', '#87CEEB', '#8A2BE2'], alpha=0.7)

ax.set_title("Increment in Clean Energy Usage\n(2005-2025)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeline', fontsize=14)
ax.set_ylabel('Consumption in GWh', fontsize=14)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 1000)
ax.set_xticks(years[::2])
plt.xticks(rotation=45)

ax.annotate('Solar Surge', xy=(2015, 45), xytext=(2012, 400),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')
ax.annotate('Wind Innovation Spike', xy=(2020, 150), xytext=(2017, 600),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkgreen')

plt.tight_layout()
plt.show()