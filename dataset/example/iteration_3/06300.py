import matplotlib.pyplot as plt
import numpy as np

# Backstory: We've been tracking the use of sustainable energy by different sectors in "Greenlandia" over the past decade.
# The data represents the adoption of solar, wind, hydro and geothermal energy in industrial, residential, and transportation sectors.

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Create artificial data representing the adoption of different types of sustainable energy in various sectors
industrial_solar = [5, 7, 9, 12, 15, 18, 20, 25, 28, 30, 32]
industrial_wind = [3, 4, 6, 8, 10, 12, 15, 17, 20, 22, 24]
industrial_hydro = [8, 10, 12, 15, 17, 19, 22, 24, 27, 30, 32]
industrial_geothermal = [2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20]

residential_solar = [1, 3, 5, 8, 11, 14, 16, 19, 21, 23, 25]
residential_wind = [0.5, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
residential_hydro = [2, 3, 4, 6, 8, 10, 13, 15, 17, 19, 21]
residential_geothermal = [1, 2, 2, 3, 4, 5, 7, 8, 9, 10, 11]

transportation_solar = [1, 2, 2, 3, 4, 6, 7, 8, 10, 12, 14]
transportation_wind = [0.2, 0.5, 1, 1.5, 2, 3, 4, 5, 6, 7, 8]
transportation_hydro = [0.8, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, 9]
transportation_geothermal = [0.2, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

# Initialize the figure and axis
plt.figure(figsize=(16, 10))

# Create subplot for industrial sectors
plt.subplot(3, 1, 1)
plt.stackplot(years, industrial_solar, industrial_wind, industrial_hydro, industrial_geothermal,
              labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.title('Industrial Sector: Sustainable Energy Adoption in Greenlandia', fontsize=14, fontweight='bold')
plt.ylabel('Energy Use (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Create subplot for residential sectors
plt.subplot(3, 1, 2)
plt.stackplot(years, residential_solar, residential_wind, residential_hydro, residential_geothermal,
              labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.title('Residential Sector: Sustainable Energy Adoption in Greenlandia', fontsize=14, fontweight='bold')
plt.ylabel('Energy Use (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Create subplot for transportation sectors
plt.subplot(3, 1, 3)
plt.stackplot(years, transportation_solar, transportation_wind, transportation_hydro, transportation_geothermal,
              labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=['#FFD700', '#1E90FF', '#00FF7F', '#FF6347'], alpha=0.9)
plt.title('Transportation Sector: Sustainable Energy Adoption in Greenlandia', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Use (GWh)', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Adjust the layout to prevent overlap of visual elements
plt.tight_layout()

# Show the plot
plt.show()