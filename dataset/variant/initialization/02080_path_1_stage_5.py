import matplotlib.pyplot as plt
import numpy as np

continents = ['Asia', 'Europe', 'NA', 'SA', 'Africa', 'Oceania']
decades = ['00s', '10s', '20s']

asia = [[30, 20, 50], [150, 100, 70], [300, 250, 120]]
europe = [[40, 60, 30], [200, 300, 50], [350, 500, 80]]
north_america = [[20, 40, 60], [180, 150, 100], [300, 320, 130]]
south_america = [[10, 10, 80], [50, 70, 90], [100, 150, 140]]
africa = [[5, 5, 20], [25, 30, 40], [80, 110, 60]]
oceania = [[15, 25, 10], [80, 60, 30], [120, 100, 40]]

data = [asia, europe, north_america, south_america, africa, oceania]

single_color = '#76c7c0'

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
n_sources = 3
n_continents = len(continents)
x_positions = np.arange(len(decades))

for i, continent_data in enumerate(data):
    solar, wind, hydro = np.array(continent_data).T
    for j, energy_data in enumerate([solar, wind, hydro]):
        ax.bar(x_positions + i * n_sources * bar_width + j * bar_width, energy_data, color=single_color, width=bar_width)

ax.set_title('Renewable Energy: Continent & Decade', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('GW', fontsize=12)
ax.set_ylim(0, 600)
ax.set_xticks(x_positions + (n_continents * n_sources - 1) * bar_width / 2)
ax.set_xticklabels(decades)

plt.tight_layout()
plt.show()