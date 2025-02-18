import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
sources = ['Sol', 'Wnd', 'Hyd', 'Bio']

energy_production = np.array([
    [90, 65, 50, 100, 80],   # Solar
    [95, 80, 110, 70, 85],   # Wind
    [115, 110, 100, 120, 105],  # Hydropower
    [45, 50, 35, 30, 40]     # Biomass
])

positions = np.arange(len(years))
bar_width = 0.2

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#1E90FF', '#8B4513', '#FFD700', '#32CD32']

for i, source in enumerate(sources):
    ax.bar(positions + i*bar_width, energy_production[i], bar_width, color=colors[i], label=source)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Production (TWh)', fontsize=12)
ax.set_title('Renewable Energy in EU (2018-22)', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width*1.5)
ax.set_xticklabels(years, fontsize=10)

ax.legend()
plt.tight_layout()
plt.show()