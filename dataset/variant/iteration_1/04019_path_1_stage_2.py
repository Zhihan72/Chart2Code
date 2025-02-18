import matplotlib.pyplot as plt
import numpy as np

continents = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Australia']
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']

na_flavors = [35, 25, 15, 12, 13]
eu_flavors = [28, 30, 10, 20, 12]
asia_flavors = [20, 35, 25, 10, 10]
sa_flavors = [25, 20, 30, 10, 15]
africa_flavors = [15, 20, 10, 25, 30]
australia_flavors = [30, 25, 15, 10, 20]

flavor_data = np.array([na_flavors, eu_flavors, asia_flavors, sa_flavors, africa_flavors, australia_flavors])

baseline = 25 
flavor_data_pos = np.where(flavor_data > baseline, flavor_data - baseline, 0)
flavor_data_neg = np.where(flavor_data <= baseline, flavor_data - baseline, 0)

# Random changes to represent altering styles
colors = ['#8b4513', '#f3e5ab', '#fc5a8d', '#c0c0c0', '#98ff98']  # Shuffle colors
markers = ['s', '^']  # Different markers for sub-plot
linestyles = ['-.', (0, (3, 1, 1, 1))]  # Different line styles

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

for idx, flavor in enumerate(flavors):
    ax1.bar(continents, flavor_data_pos[:, idx], label=flavor, color=colors[idx], edgecolor='gray', alpha=0.7)
    ax1.bar(continents, flavor_data_neg[:, idx], color=colors[idx], edgecolor='gray', hatch='/', alpha=0.7)

for cont_idx, cont_data in enumerate(flavor_data):
    for flavor_idx, value in enumerate(cont_data):
        ax1.text(cont_idx, value - baseline / 1.8, f'{value}%', va='center', ha='center', color='black' if flavor_data_pos[cont_idx, flavor_idx] > 0 else 'white', fontweight='bold')

ax1.set_title("Global Ice Cream Flavor Popularity by Continent (2023)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Continent", fontsize=12)
ax1.set_ylabel("Difference from 25% Popularity", fontsize=12)
ax1.axhline(0, color='black', linewidth=0.9)
ax1.legend(title='Ice Cream Flavors', loc='lower left')

ax1.yaxis.grid(True, linestyle=':', linewidth=0.8, alpha=0.8)  # Changed grid style

years = np.arange(2013, 2024)
vanilla_growth = [20, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34]

ax2.plot(years, vanilla_growth, marker=markers[0], linestyle=linestyles[0], color=colors[1], linewidth=2, markersize=8, label='Vanilla')

for i, growth in enumerate(vanilla_growth):
    ax2.text(years[i], growth + 0.5, f'{growth}%', ha='center', fontsize=10)

ax2.set_title("Vanilla Flavor Growth (2013-2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Popularity (%)", fontsize=12)
ax2.legend(loc='lower right')
ax2.yaxis.grid(True, linestyle='-', linewidth=0.8, alpha=0.9)

fig.tight_layout()

plt.show()