import matplotlib.pyplot as plt
import numpy as np

continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
capacities = np.array([
    [120, 220, 70, 50],    # Africa
    [310, 480, 210, 90],   # Asia
    [230, 320, 140, 80],   # Europe
    [170, 250, 110, 60],   # North America
    [150, 190, 80, 50],    # South America
    [110, 130, 60, 40],    # Oceania
])

total_capacities = capacities.sum(axis=1)

fig, ax = plt.subplots(figsize=(9, 5))

# New shuffled colors for stylistic changes
colors = ['plum', 'gold', 'lightgreen', 'skyblue', 'coral', 'lightsalmon']

# Randomly chosen different marker styles for demonstration
marker_types = ['o', 's', '^', 'D', 'p', '*']

ax.bar(continents, total_capacities, color=colors, edgecolor='black', linewidth=1.5)

# Including random grid application
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.xaxis.grid(False)

# Random change in border visibility
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add Legend with modified markers
for i, continent in enumerate(continents):
    ax.scatter([], [], color=colors[i], label=continent, marker=marker_types[i])

ax.legend(title="Continents", loc='upper left')

plt.tight_layout()
plt.show()