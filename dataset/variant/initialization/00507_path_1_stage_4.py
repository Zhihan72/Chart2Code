import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023']
solar_energy = [200, 250, 300, 350]
wind_energy = [150, 180, 220, 260]
hydro_energy = [100, 110, 120, 130]
biomass_energy = [80, 85, 90, 95]
geothermal_energy = [50, 60, 70, 80]
nuclear_energy = [30, 40, 50, 60]

# Unified color for all energy sources
uniform_color = '#4169e1'

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.12
indices = np.arange(len(years))

ax.bar(indices - bar_width*2.5, solar_energy, label='Solar Energy', color=uniform_color, width=bar_width)
ax.bar(indices - bar_width*1.5, wind_energy, label='Wind Energy', color=uniform_color, width=bar_width)
ax.bar(indices - bar_width*0.5, hydro_energy, label='Hydro Energy', color=uniform_color, width=bar_width)
ax.bar(indices + bar_width*0.5, biomass_energy, label='Biomass Energy', color=uniform_color, width=bar_width)
ax.bar(indices + bar_width*1.5, geothermal_energy, label='Geothermal Energy', color=uniform_color, width=bar_width)
ax.bar(indices + bar_width*2.5, nuclear_energy, label='Nuclear Energy', color=uniform_color, width=bar_width)

ax.set_title('EcoVille Green Initiative:\nRenewable Energy Generation (2020-2023)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (GWh)', fontsize=12)

ax.set_xticks(indices)
ax.set_xticklabels(years)

ax.yaxis.grid(True, linestyle=':', color='black', alpha=0.4)

ax.legend(title="Energy Sources", loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()

plt.show()