import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023']
solar_energy = [200, 250, 300, 350]
wind_energy = [150, 180, 220, 260]
hydro_energy = [100, 110, 120, 130]
biomass_energy = [80, 85, 90, 95]

colors = ['#ffd700', '#87ceeb', '#32cd32', '#8b4513']
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = np.arange(len(years))

ax.bar(index, solar_energy, color=colors[0], width=bar_width, align='center')
ax.bar(index + bar_width, wind_energy, color=colors[1], width=bar_width, align='center')
ax.bar(index + 2 * bar_width, hydro_energy, color=colors[2], width=bar_width, align='center')
ax.bar(index + 3 * bar_width, biomass_energy, color=colors[3], width=bar_width, align='center')

ax.set_xticks(index + 1.5 * bar_width)
ax.set_xticklabels(years)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Generation (GWh)', fontsize=12)

plt.tight_layout()
plt.show()