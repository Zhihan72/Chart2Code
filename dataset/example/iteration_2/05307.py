import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart depicts the evolution of Renewable Energy Consumption over a decade (2010-2020) in a fictional region,
# highlighting the adoption of Solar, Wind, Hydro, Biomass, and Geothermal energy sources.

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Data: Renewable energy consumption in terawatt-hours (TWh)
# Created to reflect a gradual increase in renewable energy adoption over the decade
solar_energy = [4, 5, 7, 10, 14, 18, 23, 29, 36, 44, 53]
wind_energy = [3, 4, 6, 9, 13, 17, 22, 28, 35, 43, 52]
hydro_energy = [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
biomass_energy = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
geothermal_energy = [1, 1.5, 2, 3, 4, 6, 8, 10, 13, 15, 18]

# Combine energy consumption data
energy_consumption = np.vstack([solar_energy, wind_energy, hydro_energy, biomass_energy, geothermal_energy])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, energy_consumption, labels=[
    'Solar Energy', 'Wind Energy', 'Hydro Energy', 'Biomass Energy', 'Geothermal Energy'
], colors=['#ffcc00', '#66c2a5', '#8da0cb', '#fc8d62', '#e78ac3'], alpha=0.85)

# Title and labels
ax.set_title('Renewable Energy Consumption Over a Decade\n(2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Consumption (TWh)', fontsize=14)

# Legend positioned outside the plot
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), title='Energy Sources', fontsize=12)

# Customizing the x-ticks
ax.set_xticks(np.arange(2010, 2021, 1))
ax.set_xticklabels([f"{year}" for year in np.arange(2010, 2021, 1)], rotation=45)

# Adding a secondary plot overlay: Total energy consumption as a line plot
total_energy_consumption = np.sum(energy_consumption, axis=0)
ax.plot(years, total_energy_consumption, color='black', linewidth=2, label='Total Renewable Energy')
ax.text(2020, total_energy_consumption[-1], f'{total_energy_consumption[-1]:.1f}', fontsize=10, color='black', ha='right')

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()