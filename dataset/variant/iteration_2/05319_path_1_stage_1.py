import matplotlib.pyplot as plt
import numpy as np

# Define bird species data
species = ['Parrot', 'Albatross', 'Falcon', 'Eagle', 'Swallow']
regions = ['Tropical', 'Temperate', 'Arctic']  # Added new region

# Bird data for three regions
wing_spans_tropical = [1.0, 2.5, 1.2, 1.8, 0.3]
wing_spans_temperate = [0.9, 3.2, 1.1, 2.0, 0.35]
wing_spans_arctic = [1.1, 2.8, 1.3, 1.9, 0.4]  # New data for Arctic region

flying_speeds_tropical = [24, 60, 55, 50, 30]
flying_speeds_temperate = [20, 65, 53, 47, 33]
flying_speeds_arctic = [22, 63, 56, 52, 28]  # New data for Arctic region

# Define colors and markers for species
colors = ['red', 'blue', 'green', 'purple', 'orange']
markers = ['o', 's', 'D', '^', 'v']

# Create the figure and multiple subplots
fig, axs = plt.subplots(1, 3, figsize=(21, 7), sharey=True)  # Added a new subplot

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

# Scatter plot for Arctic region
axk = axs[2]
for i, sp in enumerate(species):
    axk.scatter(wing_spans_arctic[i], flying_speeds_arctic[i], 
                color=colors[i], label=f'{sp} (Arctic)', s=100, marker=markers[i])

axk.set_title('Bird Species in Arctic Regions:\nWingspan vs. Average Flying Speed', fontsize=14, fontweight='bold')
axk.set_xlabel('Wingspan (m)', fontsize=12)
axk.legend(title='Species', loc='lower right', fontsize=10, frameon=False)
axk.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show plots
plt.show()