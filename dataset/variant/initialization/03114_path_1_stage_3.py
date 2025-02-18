import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2041, 0.25)

solar_energy = np.interp(years, np.arange(2000, 2041), np.linspace(2, 650, 41)) + 10 * np.sin(np.linspace(0, 8 * np.pi, len(years)))
wind_energy = solar_energy + np.interp(years, np.arange(2000, 2041), np.linspace(1, 490, 41)) + 15 * np.cos(np.linspace(0, 6 * np.pi, len(years)))
hydro_energy = wind_energy + np.interp(years, np.arange(2000, 2041), np.linspace(15, 600, 41)) + 20 * np.sin(np.linspace(0, 4 * np.pi, len(years)))
geothermal_energy = hydro_energy + np.interp(years, np.arange(2000, 2041), np.linspace(5, 450, 41))
tidal_energy = geothermal_energy + np.interp(years, np.arange(2000, 2041), np.linspace(2, 300, 41))
biomass_energy = tidal_energy + np.interp(years, np.arange(2000, 2041), np.linspace(3, 200, 41))
nuclear_energy = biomass_energy + np.interp(years, np.arange(2000, 2041), np.linspace(4, 550, 41))

# Adding made-up energy sources
fusion_energy = nuclear_energy + np.interp(years, np.arange(2000, 2041), np.linspace(1, 400, 41)) + 5 * np.cos(np.linspace(0, 2 * np.pi, len(years)))
space_solar_energy = fusion_energy + np.interp(years, np.arange(2000, 2041), np.linspace(2, 500, 41)) + 5 * np.sin(np.linspace(0, 2 * np.pi, len(years)))

fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(years, solar_energy, color='coral', alpha=0.8, label='Solar Energy')
ax.fill_between(years, solar_energy, wind_energy, color='dimgrey', alpha=0.8, label='Wind Energy')
ax.fill_between(years, wind_energy, hydro_energy, color='peru', alpha=0.8, label='Hydro Energy')
ax.fill_between(years, hydro_energy, geothermal_energy, color='mediumslateblue', alpha=0.8, label='Geothermal Energy')
ax.fill_between(years, geothermal_energy, tidal_energy, color='skyblue', alpha=0.8, label='Tidal Energy')
ax.fill_between(years, tidal_energy, biomass_energy, color='lightgreen', alpha=0.8, label='Biomass Energy')
ax.fill_between(years, biomass_energy, nuclear_energy, color='gold', alpha=0.8, label='Nuclear Energy')
ax.fill_between(years, nuclear_energy, fusion_energy, color='orange', alpha=0.8, label='Fusion Energy')
ax.fill_between(years, fusion_energy, space_solar_energy, color='violet', alpha=0.8, label='Space Solar Energy')

ax.grid(linestyle='--', alpha=0.5)
ax.plot(years, space_solar_energy, color='black', linestyle='--', linewidth=2)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

plt.tight_layout()
plt.show()