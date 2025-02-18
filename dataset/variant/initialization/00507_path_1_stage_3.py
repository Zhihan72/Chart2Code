import matplotlib.pyplot as plt
import numpy as np

# Updated data for energy generation in gigawatt-hours (GWh) with additional energy sources
years = ['2020', '2021', '2022', '2023']
solar_energy = [200, 250, 300, 350]
wind_energy = [150, 180, 220, 260]
hydro_energy = [100, 110, 120, 130]
biomass_energy = [80, 85, 90, 95]
geothermal_energy = [50, 60, 70, 80]
nuclear_energy = [30, 40, 50, 60]

# Colors for each energy source
colors = ['#ffd700', '#87ceeb', '#32cd32', '#8b4513', '#ff4500', '#4169e1']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Bar width and position settings
bar_width = 0.12
indices = np.arange(len(years))

# Plot grouped bars
ax.bar(indices - bar_width*2.5, solar_energy, label='Solar Energy', color=colors[0], width=bar_width)
ax.bar(indices - bar_width*1.5, wind_energy, label='Wind Energy', color=colors[1], width=bar_width)
ax.bar(indices - bar_width*0.5, hydro_energy, label='Hydro Energy', color=colors[2], width=bar_width)
ax.bar(indices + bar_width*0.5, biomass_energy, label='Biomass Energy', color=colors[3], width=bar_width)
ax.bar(indices + bar_width*1.5, geothermal_energy, label='Geothermal Energy', color=colors[4], width=bar_width)
ax.bar(indices + bar_width*2.5, nuclear_energy, label='Nuclear Energy', color=colors[5], width=bar_width)

# Set title and axis labels
ax.set_title('EcoVille Green Initiative:\nRenewable Energy Generation (2020-2023)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (GWh)', fontsize=12)

# Set x-ticks and x-tick labels
ax.set_xticks(indices)
ax.set_xticklabels(years)

# Enable gridlines for y-axis
ax.yaxis.grid(True, linestyle=':', color='black', alpha=0.4)

# Add legend
ax.legend(title="Energy Sources", loc='upper left', bbox_to_anchor=(1, 1))

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()