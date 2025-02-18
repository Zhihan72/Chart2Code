import matplotlib.pyplot as plt
import numpy as np

# Exoplanet names and additional made-up data for habitability scores
exoplanet_names = ['LHS 1140b', 'TRAPPIST-1d', 'GJ 667 Cc', 'Proxima Centauri b', 'HD 40307 g', 'Kepler-452b', 'Wolf 1061c', 'Teegarden b', 'Ross 128 b']
potential_habitability = [200, 250, 150, 180, 300, 270, 240, 170, 260]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(exoplanet_names, potential_habitability, color='lightblue', edgecolor='w', alpha=0.85)

ax.set_title("Habitability of Alien Worlds", fontsize=14, fontstyle='italic')
ax.set_xlabel("Habitability Score Index", fontsize=13)

for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.annotate(f'{width}',
                xy=(width, bar.get_y() + bar.get_height() / 2),
                xytext=(3, 0),
                textcoords="offset points",
                va='center', ha='left', fontsize=8,
                color='black', style='italic')

ax.grid(True, which='both', linestyle=':', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.tight_layout()
plt.show()