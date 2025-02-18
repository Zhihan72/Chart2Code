import matplotlib.pyplot as plt
import numpy as np

# Define years and renewable energy types
years = np.arange(2010, 2021)
energy_types = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']

# Altered synthetic data for each energy type over the years
solar_energy = [220, 960, 50, 300, 120, 650, 160, 520, 800, 80, 400]
wind_energy = [150, 720, 90, 900, 200, 350, 70, 450, 580, 1080, 270]
hydro_energy = [380, 460, 340, 320, 300, 440, 400, 360, 500, 480, 420]
geothermal_energy = [65, 30, 25, 50, 70, 20, 60, 40, 55, 45, 35]
biomass_energy = [160, 280, 300, 220, 180, 190, 240, 170, 260, 150, 200]

energy_data = [solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x_pos = np.arange(len(years))

for idx, (energy, energy_type) in enumerate(zip(energy_data, energy_types)):
    ax.bar(x_pos + idx * bar_width, energy, bar_width, label=energy_type)

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Consumption (GWh)', fontsize=14)
ax.set_title('Growth in Renewable Energy Consumption (2010 - 2020)', fontsize=16, fontweight='bold')
ax.set_xticks(x_pos + bar_width * (len(energy_types) - 1) / 2)
ax.set_xticklabels(years)
ax.legend(title='Energy Type', fontsize=12)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)
ax.xaxis.grid(False)

for idx, energy in enumerate(energy_data):
    for pos, val in enumerate(energy):
        ax.text(pos + idx * bar_width, val + 10, f'{val}', ha='center', va='bottom', fontsize=9, rotation=90)

plt.tight_layout()
plt.show()