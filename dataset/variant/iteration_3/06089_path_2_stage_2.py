import matplotlib.pyplot as plt
import numpy as np

energy_types = ["Wind", "Solar", "Hydro", "Biomass", "Geothermal"]
production_capacities = [250, 300, 200, 150, 100]
targets = [260, 310, 210, 155, 110]

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.25
index = np.arange(len(energy_types))

color = 'steelblue'

bars1 = ax.bar(index, production_capacities, bar_width, label='Production Capacity', color=color, alpha=0.7)
bars3 = ax.bar(index + bar_width, targets, bar_width, label='Production Target', color=color, alpha=0.7)

ax.set_title('GreenSolutions: Energy Production (2021-2030)', fontsize=14, fontweight='bold')
ax.set_xlabel('Energy Types', fontsize=12)
ax.set_ylabel('Energy (GWh)', fontsize=12)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(energy_types, rotation=45)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='blue')

add_labels(bars1)
add_labels(bars3)

plt.tight_layout()
plt.show()