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

# Plot stacked bars with altered stylistic elements
bar_width = 0.5
ax.bar(years, solar_energy, label='Solar Energy', color=colors[0], width=bar_width, edgecolor='black', linestyle='-.')
ax.bar(years, wind_energy, bottom=solar_energy, label='Wind Energy', color=colors[1], width=bar_width, edgecolor='grey', linestyle='--')
ax.bar(years, hydro_energy, bottom=np.array(solar_energy) + np.array(wind_energy), label='Hydro Energy', color=colors[2], width=bar_width, edgecolor='brown', linestyle=':')
ax.bar(years, biomass_energy, bottom=np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy), label='Biomass Energy', color=colors[3], width=bar_width, edgecolor='blue', linestyle='-')

# Set title and axis labels
ax.set_title('EcoVille Green Initiative:\nRenewable Energy Generation (2020-2023)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (GWh)', fontsize=12)

# Enable gridlines with altered style
ax.yaxis.grid(True, linestyle=':', color='black', alpha=0.4)

# Add legend with altered position and frame
ax.legend(title="Energy Sources", loc='lower center', bbox_to_anchor=(0.5, -0.3), frameon=True)

# Annotate the total energy generation per year
for i, year in enumerate(years):
    total_energy = solar_energy[i] + wind_energy[i] + hydro_energy[i] + biomass_energy[i]
    ax.text(i, total_energy + 10, f'{total_energy} GWh', ha='center', fontsize=10, fontweight='light')

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()