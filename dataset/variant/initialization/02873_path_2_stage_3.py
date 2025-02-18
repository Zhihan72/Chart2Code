import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

# Randomly alter some values in data arrays
solar_energy = 9 + 6 * np.log1p(years - 1999) + 2 * np.sin((years - 2000) / 5)
wind_energy = 14 + 11 * np.sqrt(years - 1999) - 0.5 * (years - 2000)
hydro_energy = np.full(years.shape, 21)
geothermal_energy = 6 + 0.4 * (years - 2000) + 0.9 * np.sin((years - 2000) / 2)
biomass_energy = 6 + 1.5 * np.log1p(years - 1999)
tidal_energy = 3 + 0.25 * (years - 2000)

energy_sources = np.row_stack((solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy, tidal_energy))

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF6347', '#8B4513', '#1E90FF']

ax.stackplot(years, energy_sources, colors=colors, alpha=0.75)

ax.set_xticks(np.arange(2000, 2031, 4))
ax.set_yticks(np.arange(0, 151, 20))
ax.yaxis.grid(True, linestyle=':', linewidth=0.8, alpha=0.6)

for year in {2005, 2028}:
    ax.axvline(x=year, color='black', linestyle='-.', linewidth=1.2)

fig.patch.set_linewidth(1)
fig.patch.set_edgecolor('black')

plt.xticks(rotation=25)

legend_labels = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Tidal']
ax.legend(legend_labels, loc='upper left', framealpha=0.7)

plt.tight_layout()

plt.show()