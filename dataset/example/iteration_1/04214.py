import matplotlib.pyplot as plt
import numpy as np

# Defining the years from 2010 to 2020
years = np.arange(2010, 2021)

# Artificial data for renewable energy production (in Terawatt-hours, TWh)
solar_energy = np.array([5, 8, 13, 18, 25, 35, 50, 70, 95, 125, 160])
wind_energy = np.array([20, 24, 30, 35, 40, 50, 60, 75, 90, 110, 135])
hydro_energy = np.array([60, 62, 65, 68, 70, 73, 77, 80, 84, 87, 90])

# Creating data for future projections
solar_projection = np.array([160, 200, 240, 290, 350])
wind_projection = np.array([135, 150, 165, 180, 200])
hydro_projection = np.array([90, 92, 94, 96, 98])
projection_years = np.arange(2021, 2026)

# Setting up the 1x1 subplot layout
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting historical data with solid lines
ax.plot(years, solar_energy, label='Solar Energy', color='gold', linewidth=2, marker='o')
ax.plot(years, wind_energy, label='Wind Energy', color='skyblue', linewidth=2, marker='s')
ax.plot(years, hydro_energy, label='Hydro Energy', color='lightgreen', linewidth=2, marker='^')

# Plotting future projections with dashed lines
ax.plot(projection_years, solar_projection, label='Solar Projection', color='gold', linestyle='--', linewidth=2)
ax.plot(projection_years, wind_projection, label='Wind Projection', color='skyblue', linestyle='--', linewidth=2)
ax.plot(projection_years, hydro_projection, label='Hydro Projection', color='lightgreen', linestyle='--', linewidth=2)

# Adding a title and labels
ax.set_title('Growth in Renewable Energy Production (2010-2025)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14, fontweight='bold')
ax.set_ylabel('Energy Production (TWh)', fontsize=14, fontweight='bold')

# Customizing the grid
ax.grid(True, linestyle='--', alpha=0.7)

# Customizing the legend
ax.legend(loc='upper left', fontsize=12)

# Setting the ticks and formatting the x-axis
ax.set_xticks(np.concatenate((years, projection_years)))
ax.set_xticklabels([str(year) for year in np.concatenate((years, projection_years))], rotation=45, ha='right')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Display the chart
plt.show()