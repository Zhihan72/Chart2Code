import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

decades = ['2000s', '2010s', '2020s', '2030s', '2040s']
discoveries = [15, 30, 45, 60, 80]
breakthroughs = [
    "Exoplanet Atmosphere",
    "Gravitational Waves",
    "Black Hole Image",
    "Asteroid Mining",
    "Interstellar Object"
]
breakthrough_years = ['2004', '2015', '2019', '2035', '2047']
missions = [10, 20, 35, 55, 75]

fig, ax = plt.subplots(figsize=(14, 8))

# Updated line plot colors
ax.plot(decades, discoveries, marker='o', linestyle='-', color='darkorange', linewidth=2, label='Discoveries', markersize=8)
ax.plot(decades, missions, marker='s', linestyle='--', color='indigo', linewidth=2, label='Missions', markersize=8)

ax.grid(True, linestyle='--', color='gray', alpha=0.5)

for i, txt in enumerate(breakthroughs):
    ax.annotate(
        f'{txt} ({breakthrough_years[i]})',
        xy=(decades[i], discoveries[i]),
        xytext=(0, 10 if i % 2 == 0 else -30),
        textcoords='offset points',
        arrowprops=dict(facecolor='black', arrowstyle='->', lw=0.8),
        fontsize=9,
        ha='center',
        bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='lightyellow', alpha=0.8)
    )

ax.set_xlabel('Decade', fontsize=12, labelpad=10)
ax.set_ylabel('Number of Discoveries / Missions', fontsize=12, labelpad=10)
ax.set_title('Journey to the Stars:\nAstronomical Discoveries and Missions Over the Decades', fontsize=16, pad=20)

ax.legend(loc='upper left', fontsize=10, frameon=True, shadow=True, fancybox=True)
ax.set_facecolor('whitesmoke')
plt.tight_layout()
plt.show()