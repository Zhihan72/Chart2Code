import matplotlib.pyplot as plt
import numpy as np

exoplanet_names = ['LHS 1140b', 'TRAPPIST-1d', 'GJ 667 Cc', 'Proxima Centauri b', 'HD 40307 g', 'Kepler-452b', 'Wolf 1061c', 'Teegarden b', 'Ross 128 b']
potential_habitability = [200, 250, 150, 180, 300, 270, 240, 170, 260]

# New set of colors for the bars
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f','#f7786b','#59a14f']

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(exoplanet_names, potential_habitability, color=colors, edgecolor='w', alpha=0.85)

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