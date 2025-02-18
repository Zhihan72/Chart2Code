import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Solar', 'Wind']
carbon_emissions = [820, 490, 16, 24, 43, 10]
cost = [65, 50, 112, 30, 50, 40]
capacity = [1000, 800, 400, 500, 300, 450]

sorted_indices = np.argsort(carbon_emissions)[::-1]

energy_sources = [energy_sources[i] for i in sorted_indices]
carbon_emissions = [carbon_emissions[i] for i in sorted_indices]
cost = [cost[i] for i in sorted_indices]
capacity = [capacity[i] for i in sorted_indices]

fig, ax1 = plt.subplots(figsize=(14, 8))

color1 = 'darkred'  # Changed from 'tab:purple'
ax1.set_xlabel('Energy Source', fontsize=12, fontstyle='italic')
ax1.set_ylabel('Carbon Emissions (gCO2/kWh)', color=color1, fontsize=12, fontweight='bold')
bars1 = ax1.bar(energy_sources, carbon_emissions, color=color1, alpha=0.8, hatch='/', label='Carbon Emissions')
ax1.tick_params(axis='y', labelcolor=color1, width=2)

ax2 = ax1.twinx()
color2 = 'mediumseagreen'  # Changed from 'tab:cyan'
ax2.set_ylabel('Cost ($/MWh)', color=color2, fontsize=12, fontweight='bold')
bars2 = ax2.bar(energy_sources, cost, color=color2, alpha=0.8, label='Cost', width=0.3, align='edge', hatch='\\')
ax2.tick_params(axis='y', labelcolor=color2, width=2)

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 70))
color3 = 'gold'  # Changed from 'tab:orange'
ax3.set_ylabel('Capacity (MW)', color=color3, fontsize=12, fontweight='bold')
bars3 = ax3.bar(energy_sources, capacity, color=color3, alpha=0.8, label='Capacity', width=0.3, align='center', hatch='o')
ax3.tick_params(axis='y', labelcolor=color3, width=2)

plt.title('Comparative Footprint of Various Energy Sources', fontsize=18, pad=20)
fig.tight_layout()

fig.legend(loc='lower right', bbox_to_anchor=(0.9, 0.1))
ax1.grid(True, which='both', linestyle='--', linewidth=0.5, color='grey')

plt.show()