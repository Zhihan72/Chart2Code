import matplotlib.pyplot as plt
import numpy as np

# The topic: The Evolution of Solar and Wind Energy Production in a Growing Renewable Market
# Timeline: Analysis from 2010 to 2020

# Define the years
years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

# Define energy production (in TWh) data for Solar and Wind energy
solar_energy = np.array([10, 20, 35, 55, 85, 130])  # Solar energy production
wind_energy = np.array([40, 55, 75, 95, 120, 150])  # Wind energy production

# Define cost reduction in $ per MWh for Solar and Wind energy
solar_cost_reduction = np.array([200, 160, 130, 100, 75, 50])
wind_cost_reduction = np.array([95, 90, 85, 75, 60, 45])

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot the lines for energy production
ax1.plot(years, solar_energy, label='Solar Energy Production', color='goldenrod', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, wind_energy, label='Wind Energy Production', color='dodgerblue', marker='s', linestyle='--', linewidth=2)

# Adding a title to the plot
ax1.set_title('Growth of Solar and Wind Energy Production\nand Cost Reduction (2010-2020)', fontsize=16, fontweight='bold')

# Adding labels for x and y axes
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14)

# Adding a secondary y-axis to show cost reduction
ax2 = ax1.twinx()
ax2.set_ylabel('Cost Reduction ($/MWh)', fontsize=14, color='tab:red')
ax2.plot(years, solar_cost_reduction, label='Solar Cost Reduction', color='lightcoral', marker='^', linestyle=':', linewidth=2.5)
ax2.plot(years, wind_cost_reduction, label='Wind Cost Reduction', color='tomato', marker='D', linestyle='-.', linewidth=2.5)

# Adding legends
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=12, frameon=True)

# Adding grid for readability
ax1.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to avoid overlapping
plt.tight_layout()

# Display the plot
plt.show()