import matplotlib.pyplot as plt
import numpy as np

energy_types = ["Wind", "Solar", "Hydro", "Biomass", "Geo"]
production_capacities = [200, 250, 300, 100, 150]
energy_consumptions = [180, 230, 140, 290, 90]
targets = [155, 210, 310, 110, 260]

# Sorting by production_capacities in descending order
sorted_indices = np.argsort(production_capacities)[::-1]
energy_types = [energy_types[i] for i in sorted_indices]
production_capacities = [production_capacities[i] for i in sorted_indices]
energy_consumptions = [energy_consumptions[i] for i in sorted_indices]
targets = [targets[i] for i in sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.25
index = np.arange(len(energy_types))

# Only showing the bars for production capacities along with their order
bars1 = ax.bar(index, production_capacities, bar_width, label='Prod Cap.', color='gold', alpha=0.9, edgecolor='black', hatch='/')

ax.set_title('Energy Prod. Capacities (Sorted)\n(2021-2030)', fontsize=16, fontweight='heavy')
ax.set_xlabel('Types', fontsize=12)
ax.set_ylabel('Energy (GWh)', fontsize=12)

ax.set_xticks(index)
ax.set_xticklabels(energy_types, rotation=45)
ax.legend(loc='upper right', fontsize=10)
ax.grid(axis='y', linestyle='-.', alpha=0.8)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, color='darkred')

add_labels(bars1)

plt.tight_layout()
plt.show()