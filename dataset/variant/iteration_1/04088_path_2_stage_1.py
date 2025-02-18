import matplotlib.pyplot as plt
import numpy as np

# Years from 2005 to 2025
years = np.arange(2005, 2026)

# Data: Energy consumption (in gigawatt hours) of different renewable energy sources
solar_energy = np.array([
    5, 7, 12, 18, 20, 25, 30, 35, 45, 50, 
    60, 70, 75, 85, 95, 110, 130, 145, 160, 180, 
    200
])
wind_energy = np.array([
    20, 25, 30, 40, 45, 50, 60, 70, 85, 100,
    110, 120, 135, 150, 165, 180, 195, 210, 230, 250,
    270
])
hydro_energy = np.array([
    30, 35, 40, 50, 55, 60, 70, 80, 90, 100,
    110, 120, 130, 140, 150, 165, 180, 200, 220, 240,
    260
])
biomass_energy = np.array([
    10, 15, 20, 25, 30, 35, 45, 50, 60, 70,
    75, 85, 95, 105, 115, 130, 145, 160, 175, 190,
    210
])

# Generate the figure and axis
fig, ax = plt.subplots(figsize=(14, 7))

# Create a stacked area plot
ax.stackplot(years, solar_energy, wind_energy, hydro_energy, biomass_energy, 
             colors=['#FFD700', '#87CEEB', '#00FF7F', '#FF6347'], alpha=0.7)

# Customize plot appearance without textual elements
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 900)

# Set x-ticks to show every 2 years
ax.set_xticks(years[::2])
plt.xticks(rotation=45)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the chart
plt.show()