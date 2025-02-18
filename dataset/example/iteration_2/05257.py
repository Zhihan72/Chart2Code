import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Growth of Renewable Energy Consumption by Type Over a Decade
# This chart shows the consumption of different types of renewable energy sources 
# in gigawatt-hours (GWh) in a fictional country from 2010 to 2020.

# Define years and renewable energy types
years = np.arange(2010, 2021)
energy_types = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']

# Construct synthetic data for each energy type over the years
solar_energy = [50, 80, 120, 160, 220, 300, 400, 520, 650, 800, 960]
wind_energy = [70, 100, 150, 200, 270, 350, 450, 580, 730, 900, 1080]
hydro_energy = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]
geothermal_energy = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
biomass_energy = [150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300]

# Create list of the energy data
energy_data = [solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy]

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar width and positions
bar_width = 0.15
x_pos = np.arange(len(years))

# Plot each energy type
for idx, (energy, energy_type) in enumerate(zip(energy_data, energy_types)):
    ax.bar(x_pos + idx * bar_width, energy, bar_width, label=energy_type)

# Adding labels, title, and legend
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Consumption (GWh)', fontsize=14)
ax.set_title('Growth in Renewable Energy Consumption (2010 - 2020)', fontsize=16, fontweight='bold')
ax.set_xticks(x_pos + bar_width * (len(energy_types) - 1) / 2)
ax.set_xticklabels(years)
ax.legend(title='Energy Type', fontsize=12)

# Adding grid lines for ease of reading data
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)
ax.xaxis.grid(False)

# Annotate bars with values
for idx, energy in enumerate(energy_data):
    for pos, val in enumerate(energy):
        ax.text(pos + idx * bar_width, val + 10, f'{val}', ha='center', va='bottom', fontsize=9, rotation=90)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()