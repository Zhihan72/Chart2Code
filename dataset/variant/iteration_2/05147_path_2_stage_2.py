import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])
solar_energy = np.array([10, 20, 35, 55, 85, 130])
solar_cost_reduction = np.array([200, 160, 130, 100, 75, 50])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, solar_energy, label='Solar Energy', color='darkorange', marker='x', linestyle='-.', linewidth=2.5)

ax1.set_title('Solar Energy Insights: 2010-2020', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14, color='navy')

ax2 = ax1.twinx()
ax2.set_ylabel('Cost Reduction ($/MWh)', fontsize=14, color='indigo')
ax2.plot(years, solar_cost_reduction, label='Solar Cost Cut', color='magenta', marker='p', linestyle='--', linewidth=3)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower right', fontsize=10, frameon=False)

ax1.grid(True, linestyle=':', alpha=0.5)

plt.tight_layout()

plt.show()