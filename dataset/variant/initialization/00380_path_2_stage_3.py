import matplotlib.pyplot as plt
import numpy as np

# Shuffle exoplanet names for randomized group labels
exoplanet_names = ['LHS 1140b', 'TRAPPIST-1d', 'GJ 667 Cc', 'Proxima Centauri b', 'HD 40307 g', 'Kepler-452b']
potential_habitability = [200, 250, 150, 180, 300, 270]

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(exoplanet_names, potential_habitability, color='lightblue', edgecolor='w', alpha=0.85)

# Change the title to something different
ax.set_title("Habitability of Alien Worlds", fontsize=14, fontstyle='italic')
# Alter the x-axis label
ax.set_xlabel("Habitability Score Index", fontsize=13)

# Annotate text without randomization in style for simplicity
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