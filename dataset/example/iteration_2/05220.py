import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the renewable energy production across different sources over a decade
# This script tracks solar, wind, and hydro energy production from 2010 to 2020

# Data for years
years = np.arange(2010, 2021)

# Data for each energy source (in gigawatt-hours)
solar_energy = np.array([10, 15, 25, 35, 50, 70, 100, 150, 210, 280, 350])
wind_energy = np.array([30, 35, 45, 60, 85, 120, 160, 210, 260, 320, 390])
hydro_energy = np.array([200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300])

# Plotting setup
fig, ax = plt.subplots(figsize=(14, 8))

# Stacked area plot
ax.stackplot(years, solar_energy, wind_energy, hydro_energy,
             labels=['Solar', 'Wind', 'Hydro'],
             colors=['#FFD700', '#1E90FF', '#32CD32'], alpha=0.7)

# Customizing plot appearance
ax.set_title("Renewable Energy Production\nby Source (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (GWh)', fontsize=14)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 1000)

# Set x-ticks to show every year
ax.set_xticks(years)

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend
ax.legend(loc='upper left', bbox_to_anchor=(1.05, 1), title="Energy Source", fontsize=12)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the chart
plt.show()