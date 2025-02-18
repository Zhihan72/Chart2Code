import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# We're studying the distribution of bird species in different regions and their respective average 
# flying speeds versus wingspan. The conservationist group is particularly interested in 
# two regions: Tropical and Temperate climates.

# Define bird species data
species = ['Parrot', 'Albatross', 'Falcon', 'Eagle', 'Swallow']
regions = ['Tropical', 'Temperate']

# Bird data manually created
wing_spans_tropical = [1.0, 2.5, 1.2, 1.8, 0.3]  # in meters
wing_spans_temperate = [0.9, 3.2, 1.1, 2.0, 0.35]  # in meters
flying_speeds_tropical = [24, 60, 55, 50, 30]  # in km/h
flying_speeds_temperate = [20, 65, 53, 47, 33]  # in km/h

# Define colors and markers for species
colors = ['red', 'blue', 'green', 'purple', 'orange']
markers = ['o', 's', 'D', '^', 'v']

# Create the figure and multiple subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7), sharey=True)

# Scatter plot for Tropical region
axi = axs[0]
for i, sp in enumerate(species):
    axi.scatter(wing_spans_tropical[i], flying_speeds_tropical[i], 
                color=colors[i], label=f'{sp} (Tropical)', s=100, marker=markers[i])

axi.set_title('Bird Species in Tropical Regions:\nWingspan vs. Average Flying Speed', fontsize=14, fontweight='bold')
axi.set_xlabel('Wingspan (m)', fontsize=12)
axi.set_ylabel('Average Flying Speed (km/h)', fontsize=12)
axi.legend(title='Species', loc='lower right', fontsize=10, frameon=False)
axi.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Scatter plot for Temperate region
axj = axs[1]
for i, sp in enumerate(species):
    axj.scatter(wing_spans_temperate[i], flying_speeds_temperate[i], 
                color=colors[i], label=f'{sp} (Temperate)', s=100, marker=markers[i])

axj.set_title('Bird Species in Temperate Regions:\nWingspan vs. Average Flying Speed', fontsize=14, fontweight='bold')
axj.set_xlabel('Wingspan (m)', fontsize=12)
axj.legend(title='Species', loc='lower right', fontsize=10, frameon=False)
axj.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()