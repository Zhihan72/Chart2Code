import matplotlib.pyplot as plt

species = ['Parrot', 'Albatross', 'Falcon', 'Eagle', 'Swallow']

wing_spans_tropical = [1.0, 2.5, 1.2, 1.8, 0.3]
wing_spans_temperate = [0.9, 3.2, 1.1, 2.0, 0.35]
wing_spans_arctic = [1.1, 2.8, 1.3, 1.9, 0.4]

flying_speeds_tropical = [24, 60, 55, 50, 30]
flying_speeds_temperate = [20, 65, 53, 47, 33]
flying_speeds_arctic = [22, 63, 56, 52, 28]

# Manually shuffled color order
colors = ['purple', 'green', 'orange', 'red', 'blue']

markers_temperate = ['^', 'v', '<', '>', 'x']
markers_arctic = ['s', 'p', 'h', 'D', '*']
markers_tropical = ['o', '+', 'd', '|', '_']

fig, axs = plt.subplots(1, 3, figsize=(21, 7), sharey=True)

# Temperate
axj = axs[0]
for i in range(len(species)):
    axj.scatter(wing_spans_temperate[i], flying_speeds_temperate[i], color=colors[i], s=100, marker=markers_temperate[i])

axj.grid(True, linestyle='-', linewidth=0.7, alpha=0.5)

# Arctic
axk = axs[1]
for i in range(len(species)):
    axk.scatter(wing_spans_arctic[i], flying_speeds_arctic[i], color=colors[i], s=100, marker=markers_arctic[i])

axk.grid(True, linestyle=':', linewidth=0.4, alpha=0.9)

# Tropical
axi = axs[2]
for i in range(len(species)):
    axi.scatter(wing_spans_tropical[i], flying_speeds_tropical[i], color=colors[i], s=100, marker=markers_tropical[i])

axi.grid(True, linestyle='-.', linewidth=0.6, alpha=0.6)

for ax in axs:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()