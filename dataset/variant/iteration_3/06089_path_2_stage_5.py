import matplotlib.pyplot as plt
import numpy as np

energy_types = ["Wind", "Solar", "Hydro", "Bio", "Geo"]
production_capacities = [250, 300, 200, 150, 100]
targets = [260, 310, 210, 155, 110]

fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 0.25
index = np.arange(len(energy_types))

color_capacity = 'powderblue'
color_target = 'lightcoral'

bars1 = ax.barh(index, production_capacities, bar_height, label='Capacity', color=color_capacity, alpha=0.8, edgecolor='gray', hatch='//')
bars3 = ax.barh(index + bar_height, targets, bar_height, label='Target', color=color_target, alpha=0.8, edgecolor='gray', hatch='\\')

ax.set_title('GreenSolutions: Energy Output Analysis', fontsize=16, fontweight='bold', style='italic')
ax.set_ylabel('Energy Type', fontsize=13, color='darkgreen')
ax.set_xlabel('Energy (GWh)', fontsize=13, color='darkgreen')
ax.set_yticks(index + bar_height / 2)
ax.set_yticklabels(energy_types, fontsize=11, fontstyle='italic')
ax.legend(loc='lower right', fontsize=10, frameon=False)
ax.grid(axis='x', linestyle='-', linewidth=0.7, color='black', alpha=0.3)

def add_labels(bars, label_color):
    for bar in bars:
        width = bar.get_width()
        ax.annotate(f'{width}',
                    xy=(width, bar.get_y() + bar.get_height() / 2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left', va='center', fontsize=9, color=label_color, fontweight='normal')

add_labels(bars1, 'darkblue')
add_labels(bars3, 'darkred')

plt.tight_layout()
plt.show()