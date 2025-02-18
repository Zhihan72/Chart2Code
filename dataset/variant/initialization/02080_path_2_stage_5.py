import matplotlib.pyplot as plt
import numpy as np

asia = [[30, 20, 50], [150, 100, 70], [300, 250, 120]]
europe = [[40, 60, 30], [200, 300, 50], [350, 500, 80]]
north_america = [[20, 40, 60], [180, 150, 100], [300, 320, 130]]
south_america = [[10, 10, 80], [50, 70, 90], [100, 150, 140]]
africa = [[5, 5, 20], [25, 30, 40], [80, 110, 60]]
oceania = [[15, 10, 5], [40, 50, 30], [60, 80, 40]]
data = [asia, europe, north_america, south_america, africa, oceania]

# shuffled colors (previously: #ff5733, #33ff57, #3357ff)
colors = ['#3357ff', '#ff5733', '#33ff57']

# Mixing the sources order (previously: Solar, Wind, Hydroelectric)
sources = ['Wind', 'Solar', 'Hydroelectric']

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
x_positions = np.arange(3)

for i, continent_data in enumerate(data):
    wind, solar, hydro = np.array(continent_data).T

    x_offset = i * bar_width * len(sources)

    # The order of sources is changed (Wind, Solar, Hydroelectric)
    ax.bar(x_positions + x_offset, wind, color=colors[0], label=sources[0] if i == 0 else "", width=bar_width, edgecolor='black', hatch='/')
    ax.bar(x_positions + x_offset + bar_width, solar, color=colors[1], label=sources[1] if i == 0 else "", width=bar_width, edgecolor='black', hatch='\\')
    ax.bar(x_positions + x_offset + 2 * bar_width, hydro, color=colors[2], label=sources[2] if i == 0 else "", width=bar_width, edgecolor='black', hatch='-')

ax.set_ylim(0, 600)
ax.set_xticks([])  # No x-axis ticks
ax.grid(axis='x', linestyle=':', alpha=0.5)  # Updating grid style and axis

# Changing legend position and frame style
ax.legend(loc='upper right', fontsize=9, frameon=True, title='Energy', title_fontsize='12', facecolor='lightgrey')

plt.tight_layout()
plt.show()