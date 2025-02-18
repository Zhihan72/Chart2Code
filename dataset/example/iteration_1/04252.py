import matplotlib.pyplot as plt
import numpy as np

# Backstory: Comparative Footprint of Various Energy Sources
# This chart will highlight the carbon emission, cost, and capacity of different energy sources.

energy_sources = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Solar', 'Wind']
carbon_emissions = [820, 490, 16, 24, 43, 10]  # gCO2/kWh
cost = [65, 50, 112, 30, 50, 40]  # $/MWh
capacity = [1000, 800, 400, 500, 300, 450]  # MW

# Create the figure and the bar axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Set up the primary y-axis for carbon emissions
color1 = 'tab:red'
ax1.set_xlabel('Energy Source')
ax1.set_ylabel('Carbon Emissions (gCO2/kWh)', color=color1)
bars1 = ax1.bar(energy_sources, carbon_emissions, color=color1, alpha=0.6, label='Carbon Emissions')
ax1.tick_params(axis='y', labelcolor=color1)

# Set up the secondary y-axis for cost
ax2 = ax1.twinx()
color2 = 'tab:blue'
ax2.set_ylabel('Cost ($/MWh)', color=color2)
bars2 = ax2.bar(energy_sources, cost, color=color2, alpha=0.6, label='Cost', width=0.4, align='edge')
ax2.tick_params(axis='y', labelcolor=color2)

# Create a third y-axis for capacity
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Offset the third axis
color3 = 'tab:green'
ax3.set_ylabel('Capacity (MW)', color=color3)
bars3 = ax3.bar(energy_sources, capacity, color=color3, alpha=0.6, label='Capacity', width=0.4, align='center')
ax3.tick_params(axis='y', labelcolor=color3)

# Title and layout adjustments
plt.title('Comparative Footprint of Various Energy Sources', fontsize=16, fontweight='bold', pad=20)
fig.tight_layout()

# Legend
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.9))

# Display the plot
plt.show()