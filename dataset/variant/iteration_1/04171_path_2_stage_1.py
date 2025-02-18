import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2031)

# Altered data while preserving the original dimensional structure
solar_energy = np.array([12, 10, 20, 15, 25, 36, 30, 43, 51, 60, 81, 70, 106, 93, 120, 151, 135, 168, 186, 205, 225])
wind_energy = np.array([23, 20, 35, 28, 52, 43, 62, 85, 73, 98, 127, 112, 143, 178, 160, 217, 197, 238, 260, 283, 307])
hydro_energy = np.array([101, 100, 103, 102, 108, 105, 117, 112, 123, 138, 130, 147, 168, 157, 180, 207, 193, 222, 238, 255, 273])
geothermal_energy = np.array([6, 5, 9, 7, 16, 12, 27, 21, 34, 51, 42, 61, 72, 97, 84, 126, 111, 142, 159, 177, 196])
biomass_energy = np.array([17, 15, 22, 19, 31, 26, 44, 37, 52, 71, 61, 82, 107, 94, 121, 152, 136, 169, 187, 206, 226])

energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy])

colors = ['#ffbb78', '#98df8a', '#aec7e8', '#ff9896', '#c5b0d5']

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'], colors=colors, alpha=0.8)

ax.set_title("Global Renewable Energy Production Growth (2010-2030)", fontsize=16, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

ax.legend(loc='upper left', fontsize=10, title='Energy Sources')
ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

ax.annotate('2015: Solar energy production ramps up', xy=(2015, solar_energy[5] / 2), xytext=(2013, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkslategray')
ax.annotate('2020: Wind energy overtakes hydro', xy=(2020, wind_energy[10] + hydro_energy[10] / 2), xytext=(2017, 250),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkslategray')
ax.annotate('2025: Geothermal energy sees rapid growth', xy=(2025, geothermal_energy[15] + biomass_energy[15] / 2), xytext=(2022, 60),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkslategray')

plt.tight_layout()
plt.show()