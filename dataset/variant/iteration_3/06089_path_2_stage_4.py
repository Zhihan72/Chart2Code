import matplotlib.pyplot as plt
import numpy as np

energy_types = ["Wind", "Solar", "Hydro", "Bio", "Geo"]
production_capacities = [250, 300, 200, 150, 100]
targets = [260, 310, 210, 155, 110]

fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 0.25
index = np.arange(len(energy_types))

color = 'steelblue'

bars1 = ax.barh(index, production_capacities, bar_height, label='Capacity', color=color, alpha=0.7)
bars3 = ax.barh(index + bar_height, targets, bar_height, label='Target', color=color, alpha=0.7)

ax.set_title('GreenSolutions: Energy Output', fontsize=14, fontweight='bold')
ax.set_ylabel('Type', fontsize=12)
ax.set_xlabel('Energy (GWh)', fontsize=12)
ax.set_yticks(index + bar_height / 2)
ax.set_yticklabels(energy_types)
ax.legend()
ax.grid(axis='x', linestyle='--', alpha=0.6)

def add_labels(bars):
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(3, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=10, color='blue')

add_labels(bars1)
add_labels(bars3)

plt.tight_layout()
plt.show()