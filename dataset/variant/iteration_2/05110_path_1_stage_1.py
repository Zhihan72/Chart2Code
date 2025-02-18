import matplotlib.pyplot as plt
import numpy as np

# Define the years from 2000 to 2050 in 10-year intervals
years = np.arange(2000, 2060, 10)

# Capacity of different renewable energy sources (fictional data in GW)
solar_capacity = [18, 33, 100, 500, 1000, 2000]
wind_capacity = [10, 20, 85, 300, 700, 1500]
hydro_capacity = [750, 800, 840, 880, 920, 960]
biomass_capacity = [25, 50, 80, 120, 160, 200]

# Setup the plotting area
fig, ax = plt.subplots(figsize=(14, 8))

# Plot lines for each type of renewable energy
ax.plot(years, solar_capacity, marker='o', linestyle='-', color='orange', linewidth=2)
ax.plot(years, wind_capacity, marker='s', linestyle='--', color='blue', linewidth=2)
ax.plot(years, hydro_capacity, marker='^', linestyle='-.', color='green', linewidth=2)
ax.plot(years, biomass_capacity, marker='d', linestyle=':', color='brown', linewidth=2)

# Set Title and Labels
ax.set_title('The Evolution and Forecast of Renewable Energy Capacity (2000-2050)', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Installed Capacity (GW)', fontsize=14)

# Limit the x and y axes ranges
ax.set_xlim(2000, 2050)
ax.set_ylim(0, 2200)

# Show the plot
plt.show()