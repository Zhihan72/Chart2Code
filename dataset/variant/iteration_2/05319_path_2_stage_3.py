import matplotlib.pyplot as plt
import numpy as np

species = ['Swallow', 'Eagle', 'Parrot', 'Falcon', 'Albatross']

# Bird data from different regions
wing_spans_tropical = [1.0, 2.5, 1.2, 1.8, 0.3]
wing_spans_temperate = [0.9, 3.2, 1.1, 2.0, 0.35]
flying_speeds_tropical = [24, 60, 55, 50, 30]
flying_speeds_temperate = [20, 65, 53, 47, 33]

# Stylistic elements randomly altered
colors = ['green', 'orange', 'blue', 'purple', 'red']
markers = ['o', 's', 'D', 'v', '^']

fig, axs = plt.subplots(1, 2, figsize=(14, 7), sharey=True)

axj = axs[0]
for i, sp in enumerate(species):
    axj.scatter(wing_spans_temperate[i], flying_speeds_temperate[i], 
                color=colors[i], label=f'{sp} in Cool', s=100, marker=markers[i])

axj.set_title('Temperate Avifauna: Speed/Span', fontsize=14, fontweight='bold')
axj.set_xlabel('WSpan (m)', fontsize=12)
axj.legend(title='Kinds', loc='upper left', fontsize=10, frameon=True)
axj.grid(False)

axi = axs[1]
for i, sp in enumerate(species):
    axi.scatter(wing_spans_tropical[i], flying_speeds_tropical[i], 
                color=colors[i], label=f'{sp} in Hot', s=100, marker=markers[i])

axi.set_title('Tropical Birds: Speed/Wing', fontsize=14, fontweight='bold')
axi.set_xlabel('Span (m)', fontsize=12)
axi.set_ylabel('Speed (km/h)', fontsize=12)
axi.legend(title='Birds', loc='upper center', fontsize=10, frameon=True)
axi.grid(True, linestyle='-', linewidth=1, alpha=0.5)

plt.tight_layout()
plt.show()