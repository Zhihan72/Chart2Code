import matplotlib.pyplot as plt
import numpy as np

# Data for energy generation in gigawatt-hours (GWh)
years = ['2020', '2021', '2022', '2023']
solar_energy = [200, 250, 300, 350]
wind_energy = [150, 180, 220, 260]
hydro_energy = [100, 110, 120, 130]
biomass_energy = [80, 85, 90, 95]

# Colors for each energy source
colors = ['#ffd700', '#87ceeb', '#32cd32', '#8b4513']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Width of a single bar
bar_width = 0.2
index = np.arange(len(years))

# Plot grouped bars
ax.bar(index, solar_energy, label='Solar Energy', color=colors[0], width=bar_width, align='center')
ax.bar(index + bar_width, wind_energy, label='Wind Energy', color=colors[1], width=bar_width, align='center')
ax.bar(index + 2 * bar_width, hydro_energy, label='Hydro Energy', color=colors[2], width=bar_width, align='center')
ax.bar(index + 3 * bar_width, biomass_energy, label='Biomass Energy', color=colors[3], width=bar_width, align='center')

# Set the position of the x ticks
ax.set_xticks(index + 1.5 * bar_width)
ax.set_xticklabels(years)

# Set title and axis labels
ax.set_title('EcoVille Green Initiative:\nRenewable Energy Generation (2020-2023)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (GWh)', fontsize=12)

# Enable gridlines for easier readability
ax.yaxis.grid(True, linestyle='--', color='grey', alpha=0.7)

# Add legend
ax.legend(title="Energy Sources", loc='upper left', bbox_to_anchor=(1.0, 1), frameon=False)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()