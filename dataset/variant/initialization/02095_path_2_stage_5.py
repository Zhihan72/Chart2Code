import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

appliance_types = ["Heating &\nCooling", "Electronics", "Laundry\nMachines", "Lighting", "Kitchen\nAppliances", "Other"]
energy_consumption = [250, 400, 150, 200, 100, 50]
variability = [30, 50, 20, 25, 10, 5]
cost_per_kwh = [0.2, 0.15, 0.18, 0.16, 0.22, 0.19]

colors = ['#1f77b4', '#2ca02c', '#8c564b', '#d62728', '#9467bd', '#ff7f0e']

fig, ax = plt.subplots(figsize=(12, 7))
bar_positions = np.arange(len(appliance_types))
bars = ax.bar(bar_positions, energy_consumption, yerr=variability, capsize=7, color=colors, width=0.5,
              path_effects=[patheffects.withStroke(linewidth=3, foreground="yellow")])

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 15, f'{yval} ZWh', ha='center', va='bottom',
            fontsize=10, fontweight='normal', path_effects=[patheffects.withStroke(linewidth=2, foreground="black")])

ax.annotate('Max Activity', xy=(1, 400), xytext=(2.5, 450),
            arrowprops=dict(facecolor='green', shrink=0.05), fontsize=12, color='blue')
ax.axhline(y=200, color='purple', linestyle='-.', linewidth=2, label='Avg. Yardstick')

ax.set_title("Household Appliance\nPower Utilization", fontsize=20, color='darkgreen', pad=25)
ax.set_xlabel("Appliance Category", fontsize=14)
ax.set_ylabel("Power Utilization (ZWh/month)", fontsize=13)
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

ax2.set_title("Monthly Appliance Expenses\n(Derived from Power Utilization)", fontsize=17, color='maroon', pad=25)
ax2.set_xlabel("Appliance Category", fontsize=14)
ax2.set_ylabel("Expense per Month (Galaxy Credits)", fontsize=14)
ax2.set_xticks(bar_positions)
ax2.set_xticklabels(appliance_types, fontsize=11, rotation=30, ha='right', color='darkred')
ax2.set_ylim(0, 90)
ax2.yaxis.grid(True, linestyle='-.', alpha=0.8)

for bar in bars2:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, yval + 2, f'{yval:.2f} GC', ha='center', va='bottom',
             fontsize=10, fontweight='normal', path_effects=[patheffects.withStroke(linewidth=2, foreground="black")])

plt.tight_layout()

plt.show()