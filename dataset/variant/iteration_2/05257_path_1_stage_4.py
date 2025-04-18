import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
energy_types = ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass']

solar_energy = [220, 960, 50, 300, 120, 650, 160, 520, 800, 80, 400]
wind_energy = [150, 720, 90, 900, 200, 350, 70, 450, 580, 1080, 270]
hydro_energy = [380, 460, 340, 320, 300, 440, 400, 360, 500, 480, 420]
geothermal_energy = [65, 30, 25, 50, 70, 20, 60, 40, 55, 45, 35]
biomass_energy = [160, 280, 300, 220, 180, 190, 240, 170, 260, 150, 200]

energy_data = [solar_energy, wind_energy, hydro_energy, geothermal_energy, biomass_energy]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
x_pos = np.arange(len(years))

bar_colors = ['#66B3FF', '#FFCC99', '#CCCCFF', '#FF9999', '#99FF99']
hatch_styles = ['/', '\\', '|', '-', '+']

for idx, (energy, color, hatch) in enumerate(zip(energy_data, bar_colors, hatch_styles)):
    ax.bar(x_pos + idx * bar_width, energy, bar_width, color=color, hatch=hatch, edgecolor='black')

ax.set_xticks(x_pos + bar_width * (len(energy_types) - 1) / 2)
ax.set_xticklabels(years, rotation=45)

ax.yaxis.grid(True, linestyle='-.', linewidth=0.5, alpha=0.8)
ax.xaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.3)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)
ax.spines['right'].set_color('grey')

plt.tight_layout()
plt.show()