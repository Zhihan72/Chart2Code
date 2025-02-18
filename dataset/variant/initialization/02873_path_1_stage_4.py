import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

solar_energy = 10 + 5 * np.log1p(years - 1999) + 2 * np.sin((years - 2000) / 5)
wind_energy = 15 + 10 * np.sqrt(years - 1999) - 0.5 * (years - 2000)
hydro_energy = np.full(years.shape, 20)
geothermal_energy = 5 + 0.5 * (years - 2000) + 1 * np.sin((years - 2000) / 2)
biomass_energy = 5 + 2 * np.log1p(years - 1999)
tidal_energy = 2 + 0.3 * (years - 2000)

np.random.seed(0)
np.random.shuffle(solar_energy)
np.random.shuffle(wind_energy)
np.random.shuffle(hydro_energy)
np.random.shuffle(geothermal_energy)
np.random.shuffle(biomass_energy)
np.random.shuffle(tidal_energy)

energy_sources = np.row_stack((
    solar_energy, wind_energy, hydro_energy,
    geothermal_energy, biomass_energy, tidal_energy
))

fig, ax = plt.subplots(figsize=(14, 8))
new_colors = ['#FF5733', '#C70039', '#900C3F', '#581845', '#FFC300', '#DAF7A6']

ax.stackplot(years, energy_sources, colors=new_colors, alpha=0.8)

# Randomized line styles for x and y axis grid
ax.set_xticks(np.arange(2000, 2031, 2))
ax.set_yticks(np.arange(0, 151, 10))
ax.yaxis.grid(True, linestyle='-', linewidth=0.75, alpha=0.5)  # Changed line style

# Removed legend for a change
plt.xticks(rotation=30)  # Randomized rotation angle
plt.tight_layout()

# Randomized border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()