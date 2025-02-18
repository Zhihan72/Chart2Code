import matplotlib.pyplot as plt
import numpy as np

# Define bird species data
species = ['Swallow', 'Eagle', 'Parrot', 'Falcon', 'Albatross']
regions = ['Temperate', 'Tropical']

# Bird data manually created
wing_spans_tropical = [1.0, 2.5, 1.2, 1.8, 0.3]
wing_spans_temperate = [0.9, 3.2, 1.1, 2.0, 0.35]
flying_speeds_tropical = [24, 60, 55, 50, 30]
flying_speeds_temperate = [20, 65, 53, 47, 33]

# Define colors and markers for species
colors = ['purple', 'green', 'orange', 'red', 'blue']
markers = ['D', '^', 'v', 'o', 's']

# Create the figure and multiple subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7), sharey=True)

# Scatter plot for Tropical region
axi = axs[0]
for i, sp in enumerate(species):
    axi.scatter(wing_spans_tropical[i], flying_speeds_tropical[i], 
                color=colors[i], label=f'{sp} in Hot', s=100, marker=markers[i])

axi.set_title('Tropical Birds: Speed vs. Wing', fontsize=14, fontweight='bold')
axi.set_xlabel('Span (m)', fontsize=12)
axi.set_ylabel('Speed (km/h)', fontsize=12)
axi.legend(title='Birds', loc='lower right', fontsize=10, frameon=False)
axi.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Scatter plot for Temperate region
axj = axs[1]
for i, sp in enumerate(species):
    axj.scatter(wing_spans_temperate[i], flying_speeds_temperate[i], 
                color=colors[i], label=f'{sp} in Cool', s=100, marker=markers[i])

axj.set_title('Temperate Avifauna: Speed vs. Span', fontsize=14, fontweight='bold')
axj.set_xlabel('WSpan (m)', fontsize=12)
axj.legend(title='Kinds', loc='lower right', fontsize=10, frameon=False)
axj.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()