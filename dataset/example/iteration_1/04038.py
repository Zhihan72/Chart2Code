import matplotlib.pyplot as plt
import numpy as np

# Imagine we are tracking the usage of renewable energy sources over a decade in a fictional country named EcoLand
years = np.arange(2020, 2030)

# Data: Monthly usage in Terawatt-hours (TWh) for different renewable sources
# Solar, Wind, Hydro, Geothermal, Biomass
solar_usage = [1.2, 1.8, 2.4, 3.0, 3.8, 4.5, 5.2, 6.0, 6.7, 7.5]
wind_usage = [0.8, 1.2, 1.8, 2.3, 3.0, 3.6, 4.1, 4.7, 5.3, 6.0]
hydro_usage = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
geothermal_usage = [0.5, 0.8, 1.0, 1.2, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5]
biomass_usage = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2]

# Creating the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each renewable energy source with different style lines
ax.plot(years, solar_usage, marker='o', linestyle='-', color='orange', label='Solar', linewidth=2)
ax.plot(years, wind_usage, marker='s', linestyle='--', color='green', label='Wind', linewidth=2)
ax.plot(years, hydro_usage, marker='^', linestyle='-.', color='blue', label='Hydro', linewidth=2)
ax.plot(years, geothermal_usage, marker='D', linestyle=':', color='red', label='Geothermal', linewidth=2)
ax.plot(years, biomass_usage, marker='x', linestyle='-', color='purple', label='Biomass', linewidth=2)

# Title and Labels
ax.set_title('Renewable Energy Usage Trends\nin EcoLand (2020-2030)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Usage (TWh)', fontsize=14)

# Add a legend with a title
ax.legend(title='Energy Sources', loc='upper left', fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Enhancing layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()