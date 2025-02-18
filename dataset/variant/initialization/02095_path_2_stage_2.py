import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

# Data for energy consumption by appliance type (in kWh)
appliance_types = ["Kitchen\nAppliances", "Heating &\nCooling", "Lighting", "Laundry\nMachines", "Electronics", "Other"]
energy_consumption = [100, 250, 200, 150, 400, 50]
variability = [10, 30, 25, 20, 50, 5]
cost_per_kwh = [0.22, 0.2, 0.16, 0.18, 0.15, 0.19]

# Sort data based on energy consumption (descending)
sorted_indices = np.argsort(energy_consumption)[::-1]
appliance_types = [appliance_types[i] for i in sorted_indices]
energy_consumption = [energy_consumption[i] for i in sorted_indices]
variability = [variability[i] for i in sorted_indices]
cost_per_kwh = [cost_per_kwh[i] for i in sorted_indices]

benchmark = 200
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(12, 7))
bar_positions = np.arange(len(appliance_types))
bars = ax.bar(bar_positions, energy_consumption, yerr=variability, capsize=5, color=colors, width=0.6,
              path_effects=[patheffects.withStroke(linewidth=3, foreground="w")])

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 20, f'{yval} kWh', ha='center', va='bottom',
            fontsize=11, fontweight='bold', path_effects=[patheffects.withStroke(linewidth=3, foreground="white")])

ax.annotate('Highest consumption', xy=(0, 400), xytext=(1, 450),
            arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12, color='darkred')
ax.axhline(y=benchmark, color='gray', linestyle='--', linewidth=1.5, label='Average Benchmark')

ax.set_title("Energy Consumption by Appliance Type\nin an Average Home", fontsize=18, color='darkblue', pad=20)
ax.set_xlabel("Appliance Type", fontsize=14)
ax.set_ylabel("Monthly Energy Consumption (kWh)", fontsize=14)
ax.set_xticks(bar_positions)
ax.set_xticklabels(appliance_types, fontsize=12, rotation=45, ha='right', color='darkgreen')
ax.set_ylim(0, 500)
ax.yaxis.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()

monthly_costs = np.array(energy_consumption) * np.array(cost_per_kwh)
fig, ax2 = plt.subplots(figsize=(12, 5))
bars2 = ax2.bar(bar_positions, monthly_costs, color=colors, width=0.6,
                path_effects=[patheffects.withStroke(linewidth=3, foreground="w")])

ax2.set_title("Monthly Cost per Appliance Type\n(Based on Energy Consumption)", fontsize=16, color='darkblue', pad=20)
ax2.set_xlabel("Appliance Type", fontsize=14)
ax2.set_ylabel("Monthly Cost (Currency Units)", fontsize=14)
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(appliance_types, fontsize=12, rotation=45, ha='right', color='darkgreen')
ax2.set_ylim(0, 90)
ax2.yaxis.grid(True, linestyle='--', alpha=0.6)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval:.2f} CU', ha='center', va='bottom',
             fontsize=11, fontweight='bold', path_effects=[patheffects.withStroke(linewidth=3, foreground="white")])

plt.tight_layout()

plt.show()