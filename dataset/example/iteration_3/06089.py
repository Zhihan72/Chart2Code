import matplotlib.pyplot as plt
import numpy as np

# Scenario: "GreenSolutions: Energy Production and Consumption"
# GreenSolutions Co. is focusing on renewable energy sources over a decade. 
# The chart aims to show the data on energy production capacities and consumptions for different energy types.

# Defining energy types and data
energy_types = ["Wind", "Solar", "Hydro", "Biomass", "Geothermal"]
production_capacities = [250, 300, 200, 150, 100]  # in gigawatt-hours (GWh)
energy_consumptions = [230, 290, 180, 140, 90]    # in gigawatt-hours (GWh)
targets = [260, 310, 210, 155, 110]  # planned production targets (GWh)

# Define plotting areas
fig, ax = plt.subplots(figsize=(12, 8))

# Bar width and position
bar_width = 0.25
index = np.arange(len(energy_types))

# Plotting bars for productions, consumptions, and targets
bars1 = ax.bar(index, production_capacities, bar_width, label='Production Capacity', color='teal', alpha=0.7)
bars2 = ax.bar(index + bar_width, energy_consumptions, bar_width, label='Energy Consumption', color='orange', alpha=0.7)
bars3 = ax.bar(index + 2 * bar_width, targets, bar_width, label='Production Target', color='olivedrab', alpha=0.7)

# Adding details and annotations
ax.set_title('GreenSolutions: Energy Production vs. Consumption (2021-2030)', fontsize=14, fontweight='bold')
ax.set_xlabel('Energy Types', fontsize=12)
ax.set_ylabel('Energy (GWh)', fontsize=12)
ax.set_xticks(index + bar_width)
ax.set_xticklabels(energy_types, rotation=45)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.6)

# Annotating bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, color='blue')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()