import matplotlib.pyplot as plt
import numpy as np

# Defining energy types and data
energy_types = ["Wind", "Solar", "Hydro", "Biomass", "Geothermal"]
production_capacities = [250, 300, 200, 150, 100]
energy_consumptions = [230, 290, 180, 140, 90]
targets = [260, 310, 210, 155, 110]

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.25
index = np.arange(len(energy_types))

# Altering marker types, line styles, and colors
bars1 = ax.bar(index, production_capacities, bar_width, label='Production Capacity', color='purple', alpha=0.9, edgecolor='black', hatch='/')
bars2 = ax.bar(index + bar_width, energy_consumptions, bar_width, label='Energy Consumption', color='gold', alpha=0.9, edgecolor='red', hatch='x')
bars3 = ax.bar(index + 2 * bar_width, targets, bar_width, label='Production Target', color='lightgreen', alpha=0.9, edgecolor='blue', hatch='\\')

# Adding details and annotations with altered style
ax.set_title('GreenSolutions: Energy Production vs. Consumption\n(2021-2030)', fontsize=16, fontweight='heavy')
ax.set_xlabel('Energy Types', fontsize=12)
ax.set_ylabel('Energy (GWh)', fontsize=12)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(energy_types, rotation=45)
ax.legend(loc='upper left', fontsize=10)
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
add_labels(bars2)
add_labels(bars3)

plt.tight_layout()
plt.show()