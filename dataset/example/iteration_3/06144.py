import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Charting the rise of renewable energy sources in a fictional country "Greensland"
# from 2010-2030 to monitor their progression while identifying key events and trends.

# Defining the years for the data set
years = np.arange(2010, 2031)

# Data for different renewable energy sources (in TWh) in Greensland
solar_energy = np.array([1, 2, 4, 6, 10, 16, 24, 34, 46, 60, 76, 94, 114, 136, 160, 186, 214, 244, 276, 310, 346])
wind_energy = np.array([3, 5, 9, 14, 20, 27, 35, 44, 54, 66, 79, 93, 108, 124, 141, 159, 178, 198, 219, 241, 264])
hydro_energy = np.array([10, 12, 15, 19, 24, 30, 37, 45, 54, 64, 75, 87, 100, 114, 129, 145, 162, 180, 199, 219, 240])
bio_energy = np.array([2, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93, 107, 122, 138, 155, 173, 192, 212])
geothermal_energy = np.array([1, 1, 2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95, 109, 124, 140, 157])

# Calculate cumulative renewable energy production
total_renewable_energy = solar_energy + wind_energy + hydro_energy + bio_energy + geothermal_energy

# Create a stacked area plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, bio_energy, geothermal_energy,
             labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'],
             colors=['#ffd700', '#87ceeb', '#32cd32', '#8b4513', '#ff4500'], alpha=0.8)

# Setting the title and labels
ax.set_title("Renewable Energy Sources in Greensland: Evolution from 2010 to 2030", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Energy Production (TWh)", fontsize=14)

# Adding a legend
ax.legend(loc='upper left', fontsize=12, frameon=False, title="Energy Sources")

# Adding gridlines for better readability
ax.grid(True, linestyle='--', alpha=0.5)

# Adding key events annotations
ax.annotate('Major Solar Farm Introduced', xy=(2014, 10), xytext=(2016, 50),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

ax.annotate('Wind Turbine Expansion', xy=(2020, 96), xytext=(2021, 150),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, color='black')

# Rotate x-axis labels for clarity
ax.tick_params(axis='x', rotation=45)

# Automatically adjust layout to prevent clipping
plt.tight_layout()

# Show the plot
plt.show()