import matplotlib.pyplot as plt
import numpy as np

species = ['Swallow', 'Eagle', 'Parrot', 'Falcon', 'Albatross']

# Shuffled data within the groups while preserving the structure
wing_spans_tropical = [1.2, 1.0, 0.3, 1.8, 2.5]  # shuffled
wing_spans_temperate = [1.1, 3.2, 0.35, 2.0, 0.9]  # shuffled
flying_speeds_tropical = [55, 24, 30, 50, 60]  # shuffled
flying_speeds_temperate = [53, 65, 33, 47, 20]  # shuffled

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