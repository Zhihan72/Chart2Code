import matplotlib.pyplot as plt
import numpy as np

# Define the years
years = np.arange(2010, 2031)

# Artificial data for renewable energy production in terawatt-hours (TWh)
solar_energy = np.array([10, 12, 15, 20, 25, 30, 36, 43, 51, 60, 70, 81, 93, 106, 120, 135, 151, 168, 186, 205, 225])
wind_energy = np.array([20, 23, 28, 35, 43, 52, 62, 73, 85, 98, 112, 127, 143, 160, 178, 197, 217, 238, 260, 283, 307])
hydro_energy = np.array([100, 101, 102, 103, 105, 108, 112, 117, 123, 130, 138, 147, 157, 168, 180, 193, 207, 222, 238, 255, 273])
geothermal_energy = np.array([5, 6, 7, 9, 12, 16, 21, 27, 34, 42, 51, 61, 72, 84, 97, 111, 126, 142, 159, 177, 196])
biomass_energy = np.array([15, 17, 19, 22, 26, 31, 37, 44, 52, 61, 71, 82, 94, 107, 121, 136, 152, 169, 187, 206, 226])

# Stack the data for area chart
energy_data = np.vstack([solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy])

colors = ['#ffbb78', '#98df8a', '#aec7e8', '#ff9896', '#c5b0d5']

# Plotting the area chart
fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, energy_data, colors=colors, alpha=0.8)

# Add title and labels
ax.set_title("Global Renewable Energy Production Growth (2010-2030)", fontsize=16, weight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Production (TWh)", fontsize=12)

# Removing stylistic elements: legend, grid, and annotations

# Adjusting the layout
plt.tight_layout()

# Display the plot
plt.show()