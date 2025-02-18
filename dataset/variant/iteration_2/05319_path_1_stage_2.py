import matplotlib.pyplot as plt
import numpy as np

species = ['Parrot', 'Albatross', 'Falcon', 'Eagle', 'Swallow']

wing_spans_tropical = [1.0, 2.5, 1.2, 1.8, 0.3]
wing_spans_temperate = [0.9, 3.2, 1.1, 2.0, 0.35]
wing_spans_arctic = [1.1, 2.8, 1.3, 1.9, 0.4]

flying_speeds_tropical = [24, 60, 55, 50, 30]
flying_speeds_temperate = [20, 65, 53, 47, 33]
flying_speeds_arctic = [22, 63, 56, 52, 28]

colors = ['red', 'blue', 'green', 'purple', 'orange']
markers = ['o', 's', 'D', '^', 'v']

fig, axs = plt.subplots(1, 3, figsize=(21, 7), sharey=True)

axi = axs[0]
for i in range(len(species)):
    axi.scatter(wing_spans_tropical[i], flying_speeds_tropical[i], color=colors[i], s=100, marker=markers[i])

axi.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

axj = axs[1]
for i in range(len(species)):
    axj.scatter(wing_spans_temperate[i], flying_speeds_temperate[i], color=colors[i], s=100, marker=markers[i])

axj.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

axk = axs[2]
for i in range(len(species)):
    axk.scatter(wing_spans_arctic[i], flying_speeds_arctic[i], color=colors[i], s=100, marker=markers[i])

axk.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()