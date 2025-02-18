import matplotlib.pyplot as plt
import numpy as np

# Define the years of interest with a higher resolution (quarterly)
years = np.arange(2000, 2041, 0.25)

# Artificial data for different energy sources (in gigawatts) with more complexity
solar_energy = np.interp(years, np.arange(2000, 2041), np.linspace(2, 650, 41)) + 10 * np.sin(np.linspace(0, 8 * np.pi, len(years)))
wind_energy = solar_energy + np.interp(years, np.arange(2000, 2041), np.linspace(1, 490, 41)) + 15 * np.cos(np.linspace(0, 6 * np.pi, len(years)))
hydro_energy = wind_energy + np.interp(years, np.arange(2000, 2041), np.linspace(15, 600, 41)) + 20 * np.sin(np.linspace(0, 4 * np.pi, len(years)))
geothermal_energy = hydro_energy + np.interp(years, np.arange(2000, 2041), np.linspace(5, 450, 41))

# Additional energy sources
tidal_energy = geothermal_energy + np.interp(years, np.arange(2000, 2041), np.linspace(2, 300, 41))
biomass_energy = tidal_energy + np.interp(years, np.arange(2000, 2041), np.linspace(3, 200, 41))
nuclear_energy = biomass_energy + np.interp(years, np.arange(2000, 2041), np.linspace(4, 550, 41))

# Plot the stacked area chart
fig, ax = plt.subplots(figsize=(16, 10))

ax.fill_between(years, solar_energy, color='gold', alpha=0.8)
ax.fill_between(years, solar_energy, wind_energy, color='skyblue', alpha=0.8)
ax.fill_between(years, wind_energy, hydro_energy, color='lightgreen', alpha=0.8)
ax.fill_between(years, hydro_energy, geothermal_energy, color='coral', alpha=0.8)
ax.fill_between(years, geothermal_energy, tidal_energy, color='mediumslateblue', alpha=0.8)
ax.fill_between(years, tidal_energy, biomass_energy, color='peru', alpha=0.8)
ax.fill_between(years, biomass_energy, nuclear_energy, color='dimgrey', alpha=0.8)

# Grid for readability
ax.grid(linestyle='--', alpha=0.5)

# Cumulative Total Line Plot
ax.plot(years, nuclear_energy, color='black', linestyle='--', linewidth=2)

# Layout adjustment
plt.tight_layout()

# Display the plot
plt.show()