import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

appliance_types = ["Kitchen\nAppliances", "Heating &\nCooling", "Lighting", "Laundry\nMachines", "Electronics", "Other"]
energy_consumption = [250, 400, 150, 100, 200, 50]
variability = [30, 50, 20, 10, 25, 5]

benchmark = 200

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(12, 7))

bar_positions = np.arange(len(appliance_types))
bars = ax.bar(bar_positions, energy_consumption, yerr=variability, capsize=8, color=colors, width=0.5,
              path_effects=[patheffects.withStroke(linewidth=2, foreground="gray")])

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 10, f'{yval} kWh', ha='center', va='bottom',
            fontsize=10, fontweight='bold', path_effects=[patheffects.withStroke(linewidth=2, foreground="gray")])

ax.annotate('Peak Usage', xy=(1, 400), xytext=(3, 420),
            arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=11, color='darkred')

ax.axhline(y=benchmark, color='black', linestyle='-.', linewidth=2, label='Benchmark')

ax.set_title("Energy Consumption by Appliance\nType in an Average Home", fontsize=17, color='purple', pad=15)
ax.set_xlabel("Appliance Type", fontsize=13)
ax.set_ylabel("Energy Consumption (kWh)", fontsize=13)
ax.set_xticks(bar_positions)
ax.set_xticklabels(appliance_types, fontsize=11, rotation=30, ha='right', color='teal')
ax.set_ylim(0, 500)

ax.yaxis.grid(True, linestyle=':', alpha=0.8)
ax.legend(loc='upper left', frameon=False)

plt.tight_layout()

cost_per_kwh = [0.14, 0.16, 0.20, 0.18, 0.15, 0.17]
monthly_costs = np.array(energy_consumption) * np.array(cost_per_kwh)

fig, ax2 = plt.subplots(figsize=(12, 5))

bars2 = ax2.bar(bar_positions, monthly_costs, color=colors, width=0.5,
                path_effects=[patheffects.withStroke(linewidth=2, foreground="gray")])

ax2.set_title("Monthly Cost per Appliance\n(Based on Consumption)", fontsize=15, color='purple', pad=15)
ax2.set_xlabel("Appliance Type", fontsize=13)
ax2.set_ylabel("Cost (Currency Units)", fontsize=13)
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(appliance_types, fontsize=11, rotation=30, ha='right', color='teal')
ax2.set_ylim(0, 80)
ax2.yaxis.grid(True, linestyle=':', alpha=0.8)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{yval:.2f} CU', ha='center', va='bottom',
             fontsize=10, fontweight='bold', path_effects=[patheffects.withStroke(linewidth=2, foreground="gray")])

plt.tight_layout()
plt.show()