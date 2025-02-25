import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
energy_types = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass', 'Tidal', 'Wave']

# Synthetic data for each energy type over the years
solar_energy = [50, 80, 120, 160, 220, 300, 400, 520, 650, 800, 960]
wind_energy = [70, 100, 150, 200, 270, 350, 450, 580, 730, 900, 1080]
hydro_energy = [300, 320, 340, 360, 380, 400, 420, 440, 460, 480, 500]
geothermal_energy = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
biomass_energy = [150, 160, 170, 180, 190, 200, 220, 240, 260, 280, 300]
tidal_energy = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]  
wave_energy = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]  

energy_data = [solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy, tidal_energy, wave_energy]

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.1
y_pos = np.arange(len(years))

for idx, (energy, energy_type) in enumerate(zip(energy_data, energy_types)):
    ax.barh(y_pos + idx * bar_width, energy, bar_width, label=energy_type)

ax.set_ylabel('Year', fontsize=14)
ax.set_xlabel('Consumption (GWh)', fontsize=14)
ax.set_title('Growth in Renewable Energy Consumption (2010 - 2020)', fontsize=16, fontweight='bold')
ax.set_yticks(y_pos + bar_width * (len(energy_types) - 1) / 2)
ax.set_yticklabels(years)
ax.legend(title='Energy Type', fontsize=12)

ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.6)
ax.yaxis.grid(False)

for idx, energy in enumerate(energy_data):
    for pos, val in enumerate(energy):
        ax.text(val + 10, pos + idx * bar_width, f'{val}', va='center', ha='left', fontsize=9)

plt.tight_layout()
plt.show()