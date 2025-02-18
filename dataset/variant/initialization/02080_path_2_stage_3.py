import matplotlib.pyplot as plt
import numpy as np

continents = ['Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania']
decades = ['2000s', '2010s', '2020s']

asia = [[30, 20, 50], [150, 100, 70], [300, 250, 120]]
europe = [[40, 60, 30], [200, 300, 50], [350, 500, 80]]
north_america = [[20, 40, 60], [180, 150, 100], [300, 320, 130]]
south_america = [[10, 10, 80], [50, 70, 90], [100, 150, 140]]
africa = [[5, 5, 20], [25, 30, 40], [80, 110, 60]]
oceania = [[15, 10, 5], [40, 50, 30], [60, 80, 40]]

data = [asia, europe, north_america, south_america, africa, oceania]

colors = ['#ff5733', '#33ff57', '#3357ff']
sources = ['Solar', 'Wind', 'Hydroelectric']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
x_positions = np.arange(len(decades))

for i, continent_data in enumerate(data):
    solar, wind, hydro = np.array(continent_data).T
    
    x_offset = i * bar_width * len(sources)

    ax.bar(x_positions + x_offset, solar, color=colors[0], label=sources[0] if i == 0 else "", width=bar_width)
    ax.bar(x_positions + x_offset + bar_width, wind, color=colors[1], label=sources[1] if i == 0 else "", width=bar_width)
    ax.bar(x_positions + x_offset + 2 * bar_width, hydro, color=colors[2], label=sources[2] if i == 0 else "", width=bar_width)

ax.set_title('Renewable Energy Adoption Across Continents:\nA Decadal Analysis (2000-2020)', 
             fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Adoption (Gigawatts)', fontsize=12)
ax.set_ylim(0, 600)
ax.set_xticks(x_positions + bar_width * len(sources) * (len(continents) - 1) / 2)
ax.set_xticklabels(decades)

ax.grid(axis='y', linestyle='--', alpha=0.7)

ax.legend(loc='upper left', fontsize=10, frameon=False, title='Energy Source', title_fontsize='13')

plt.tight_layout()
plt.show()