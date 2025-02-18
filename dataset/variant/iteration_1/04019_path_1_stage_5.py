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

# Changed the order of colors to shuffle them
colors = ['#98ff98', '#fc5a8d', '#f3e5ab', '#8b4513', '#c0c0c0']
markers = ['s', '^']
linestyles = ['-.', (0, (3, 1, 1, 1))]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

years = np.arange(2013, 2024)
vanilla_growth = [20, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34]

ax1.plot(years, vanilla_growth, marker=markers[0], linestyle=linestyles[0], color=colors[2], linewidth=2, markersize=8, label='Vanilla Pleasures')

for i, growth in enumerate(vanilla_growth):
    ax1.text(years[i], growth + 0.5, f'{growth}%', ha='center', fontsize=10)

ax1.set_title("Vanilla Craze Over Years", fontsize=14, fontweight='bold')
ax1.set_xlabel("Timeline", fontsize=12)
ax1.set_ylabel("Preference (%)", fontsize=12)
ax1.legend(loc='lower right')
ax1.yaxis.grid(True, linestyle='-', linewidth=0.8, alpha=0.9)

for idx, flavor in enumerate(flavors):
    ax2.bar(continents, flavor_data_pos[:, idx], label=f'Savory {flavor}', color=colors[idx], edgecolor='gray', alpha=0.7)
    ax2.bar(continents, flavor_data_neg[:, idx], color=colors[idx], edgecolor='gray', hatch='/', alpha=0.7)

for cont_idx, cont_data in enumerate(flavor_data):
    for flavor_idx, value in enumerate(cont_data):
        ax2.text(cont_idx, value - baseline / 1.8, f'{value}%', va='center', ha='center', color='black' if flavor_data_pos[cont_idx, flavor_idx] > 0 else 'white', fontweight='bold')

ax2.set_title("Flavor Dynamics by Region", fontsize=16, fontweight='bold')
ax2.set_xlabel("Regions", fontsize=12)
ax2.set_ylabel("Offset from 25% Benchmark", fontsize=12)
ax2.axhline(0, color='black', linewidth=0.9)
ax2.legend(title='Tasty Treats', loc='lower left')
ax2.yaxis.grid(True, linestyle=':', linewidth=0.8, alpha=0.8)

fig.tight_layout()

plt.show()