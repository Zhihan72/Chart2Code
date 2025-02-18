import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023']
solar_energy = [200, 250, 300, 350]
wind_energy = [150, 180, 220, 260]
hydro_energy = [100, 110, 120, 130]
biomass_energy = [80, 85, 90, 95]
geothermal_energy = [50, 60, 70, 80]
nuclear_energy = [30, 40, 50, 60]

uniform_color = '#4169e1'

fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.12
indices = np.arange(len(years))

ax.bar(indices - bar_width*2.5, solar_energy, color=uniform_color, width=bar_width)
ax.bar(indices - bar_width*1.5, wind_energy, color=uniform_color, width=bar_width)
ax.bar(indices - bar_width*0.5, hydro_energy, color=uniform_color, width=bar_width)
ax.bar(indices + bar_width*0.5, biomass_energy, color=uniform_color, width=bar_width)
ax.bar(indices + bar_width*1.5, geothermal_energy, color=uniform_color, width=bar_width)
ax.bar(indices + bar_width*2.5, nuclear_energy, color=uniform_color, width=bar_width)

ax.set_xticks(indices)

ax.yaxis.grid(True, linestyle=':', color='black', alpha=0.4)

plt.tight_layout()

plt.show()