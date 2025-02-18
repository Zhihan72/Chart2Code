import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2031)

# Generate synthetic data for multiple energy sources
solar_energy = 10 + 5 * np.log1p(years - 1999) + 2 * np.sin((years - 2000) / 5)
wind_energy = 15 + 10 * np.sqrt(years - 1999) - 0.5 * (years - 2000)
hydro_energy = np.full(years.shape, 20)
geothermal_energy = 5 + 0.5 * (years - 2000) + 1 * np.sin((years - 2000) / 2)
biomass_energy = 5 + 2 * np.log1p(years - 1999)
tidal_energy = 2 + 0.3 * (years - 2000)

# Shuffle data for randomness while preserving structure
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

ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Tidal'], colors=new_colors, alpha=0.8)

ax.set_title('Trends in Renewable Energy Adoption (2000-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Percentage Contribution of Energy Sources (%)', fontsize=12)

ax.set_xticks(np.arange(2000, 2031, 2))
ax.set_yticks(np.arange(0, 151, 10))
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))

highlight_years = {2015: "Paris Agreement", 2020: "Renewables Push", 2030: "Sustainability Goal"}
for year, event in highlight_years.items():
    ax.axvline(x=year, color='grey', linestyle='--', linewidth=0.8)
    ax.text(year, 5, event, rotation=90, verticalalignment='bottom', horizontalalignment='right', color='grey', fontsize=9)

plt.xticks(rotation=45)
plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()