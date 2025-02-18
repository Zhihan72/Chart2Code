import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

solar_energy = 10 + 5 * np.log1p(years - 1999) + 2 * np.sin((years - 2000) / 5)
wind_energy = 15 + 10 * np.sqrt(years - 1999) - 0.5 * (years - 2000)
hydro_energy = np.full(years.shape, 20)
geothermal_energy = 5 + 0.5 * (years - 2000) + 1 * np.sin((years - 2000) / 2)
biomass_energy = 5 + 2 * np.log1p(years - 1999)
tidal_energy = 2 + 0.3 * (years - 2000)

energy_sources = np.row_stack((solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy, tidal_energy))

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#FFD700', '#87CEEB', '#32CD32', '#FF6347', '#8B4513', '#1E90FF']

ax.stackplot(years, energy_sources, colors=colors, alpha=0.75)

# Altered grid style and position of x-ticks and y-ticks
ax.set_xticks(np.arange(2000, 2031, 3)) # Randomly change interval
ax.set_yticks(np.arange(0, 151, 15)) # Randomly change interval
ax.yaxis.grid(True, linestyle=':', linewidth=0.8, alpha=0.6) # Different grid style

# Alter vertical line styles and positions
for year in {2010, 2025}:
    ax.axvline(x=year, color='black', linestyle='-.', linewidth=1.2)

# Add border with a different color and style
fig.patch.set_linewidth(1)
fig.patch.set_edgecolor('black')

plt.xticks(rotation=30) # Slightly alter rotation for variation

# Legend alterations
legend_labels = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Tidal']
ax.legend(legend_labels, loc='upper left', framealpha=0.7)

plt.tight_layout()

plt.show()