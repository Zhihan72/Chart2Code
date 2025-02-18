import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
solar_energy = np.array([10, 20, 35, 55, 85, 130])
wind_energy = np.array([40, 55, 75, 95, 120, 150])
solar_cost_reduction = np.array([200, 160, 130, 100, 75, 50])
wind_cost_reduction = np.array([95, 90, 85, 75, 60, 45])

fig, ax1 = plt.subplots(figsize=(14, 8))

# Altering marker, line style, and color
ax1.plot(years, solar_energy, label='Solar Energy', color='darkorange', marker='x', linestyle='-.', linewidth=2.5)
ax1.plot(years, wind_energy, label='Wind Energy', color='mediumseagreen', marker='v', linestyle=':', linewidth=2.5)

ax1.set_title('Renewable Energy Insights: 2010-2020', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14, color='navy')

# Random alteration for the secondary y-axis line styles and colors
ax2 = ax1.twinx()
ax2.set_ylabel('Cost Reduction ($/MWh)', fontsize=14, color='indigo')
ax2.plot(years, solar_cost_reduction, label='Solar Cost Cut', color='magenta', marker='p', linestyle='--', linewidth=3)
ax2.plot(years, wind_cost_reduction, label='Wind Cost Cut', color='darkred', marker='1', linestyle='-', linewidth=3)

# Legend positioned at lower right with a different style
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower right', fontsize=10, frameon=False)

# Changing grid style
ax1.grid(True, linestyle=':', alpha=0.5)

# A tighter layout
plt.tight_layout()

plt.show()