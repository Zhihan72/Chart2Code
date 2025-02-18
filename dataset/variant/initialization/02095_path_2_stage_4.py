import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

appliance_types = ["Kitchen\nAppliances", "Heating &\nCooling", "Lighting", "Laundry\nMachines", "Electronics", "Other"]
energy_consumption = [100, 250, 200, 150, 400, 50]
variability = [10, 30, 25, 20, 50, 5]
cost_per_kwh = [0.22, 0.2, 0.16, 0.18, 0.15, 0.19]

sorted_indices = np.argsort(energy_consumption)[::-1]
appliance_types = [appliance_types[i] for i in sorted_indices]
energy_consumption = [energy_consumption[i] for i in sorted_indices]
variability = [variability[i] for i in sorted_indices]
cost_per_kwh = [cost_per_kwh[i] for i in sorted_indices]

benchmark = 200

# Shuffled colors
colors = ['#9467bd', '#1f77b4', '#d62728', '#8c564b', '#2ca02c', '#ff7f0e']

fig, ax = plt.subplots(figsize=(12, 7))
bar_positions = np.arange(len(appliance_types))
bars = ax.bar(bar_positions, energy_consumption, yerr=variability, capsize=7, color=colors, width=0.5,
              path_effects=[patheffects.withStroke(linewidth=3, foreground="yellow")])

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 15, f'{yval} kWh', ha='center', va='bottom',
            fontsize=10, fontweight='normal', path_effects=[patheffects.withStroke(linewidth=2, foreground="black")])

ax.annotate('Peak Usage', xy=(0, 400), xytext=(1, 450),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=12, color='blue')
ax.axhline(y=benchmark, color='purple', linestyle='-.', linewidth=2, label='Avg. Benchmark')

ax.set_title("Appliance Energy Use\nin Homes", fontsize=20, color='olive', pad=25)
ax.set_xlabel("Type of Appliance", fontsize=14)
ax.set_ylabel("Energy Consumption (kWh/month)", fontsize=13)
ax.set_xticks(bar_positions)
ax.set_xticklabels(appliance_types, fontsize=11, rotation=30, ha='right', color='navy')
ax.set_ylim(0, 500)
ax.yaxis.grid(True, linestyle=':', alpha=0.7)

ax.legend(loc='upper center')

plt.tight_layout()

monthly_costs = np.array(energy_consumption) * np.array(cost_per_kwh)
fig, ax2 = plt.subplots(figsize=(12, 5))
bars2 = ax2.bar(bar_positions, monthly_costs, color=colors, width=0.4,
                path_effects=[patheffects.withStroke(linewidth=2, foreground="pink")])

ax2.set_title("Monthly Appliance Costs\n(Based on Energy Use)", fontsize=17, color='maroon', pad=25)
ax2.set_xlabel("Type of Appliance", fontsize=14)
ax2.set_ylabel("Cost per Month (Currency Units)", fontsize=14)
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(appliance_types, fontsize=11, rotation=30, ha='right', color='darkred')
ax2.set_ylim(0, 90)
ax2.yaxis.grid(True, linestyle='-.', alpha=0.8)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval:.2f} CU', ha='center', va='bottom',
             fontsize=10, fontweight='normal', path_effects=[patheffects.withStroke(linewidth=2, foreground="black")])

plt.tight_layout()

plt.show()