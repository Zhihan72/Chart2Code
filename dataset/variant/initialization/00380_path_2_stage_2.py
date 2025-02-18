import matplotlib.pyplot as plt
import numpy as np

exoplanet_names = ['Kepler-452b', 'Proxima Centauri b', 'TRAPPIST-1d', 'LHS 1140b', 'GJ 667 Cc', 'HD 40307 g']
potential_habitability = [200, 250, 150, 180, 300, 270]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(exoplanet_names, potential_habitability, color='lightgreen', edgecolor='w', alpha=0.85)

ax.set_title("Exoplanet Habitability Scores", fontsize=14, fontstyle='italic')
ax.set_xlabel("Habitability Index", fontsize=13)

line_styles = ['--', '-.', ':', '-', '--', '-.']
marker_types = ['o', 'v', '^', '<', '>', 's']
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