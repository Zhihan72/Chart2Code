import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

solar_energy = np.array([10, 20, 35, 55, 85, 130])
wind_energy = np.array([40, 55, 75, 95, 120, 150])
hydro_energy = np.array([300, 320, 340, 360, 380, 400])  # New data for hydro energy
geothermal_energy = np.array([15, 17, 19, 25, 30, 42])   # New data for geothermal energy

solar_cost_reduction = np.array([200, 160, 130, 100, 75, 50])
wind_cost_reduction = np.array([95, 90, 85, 75, 60, 45])
hydro_cost_reduction = np.array([60, 58, 55, 53, 50, 48])  # New data for hydro cost reduction
geothermal_cost_reduction = np.array([170, 150, 140, 130, 120, 110])  # New data for geothermal cost reduction

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, solar_energy, label='Solar Energy Production', color='mediumseagreen', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, wind_energy, label='Wind Energy Production', color='orchid', marker='s', linestyle='--', linewidth=2)
ax1.plot(years, hydro_energy, label='Hydro Energy Production', color='royalblue', marker='x', linestyle='-.', linewidth=2)  # Plot for hydro energy
ax1.plot(years, geothermal_energy, label='Geothermal Energy Production', color='peru', marker='8', linestyle=':', linewidth=2)  # Plot for geothermal energy

ax1.set_title('Growth of Renewable Energy Production\nand Cost Reduction (2010-2020)', fontsize=16, fontweight='bold')

ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14)

ax2 = ax1.twinx()
ax2.set_ylabel('Cost Reduction ($/MWh)', fontsize=14, color='tab:red')
ax2.plot(years, solar_cost_reduction, label='Solar Cost Reduction', color='darkcyan', marker='^', linestyle=':', linewidth=2.5)
ax2.plot(years, wind_cost_reduction, label='Wind Cost Reduction', color='darkorange', marker='D', linestyle='-.', linewidth=2.5)
ax2.plot(years, hydro_cost_reduction, label='Hydro Cost Reduction', color='dodgerblue', marker='*', linestyle='-', linewidth=2.5)  # Plot for hydro cost reduction
ax2.plot(years, geothermal_cost_reduction, label='Geothermal Cost Reduction', color='saddlebrown', marker='h', linestyle='--', linewidth=2.5)  # Plot for geothermal cost reduction

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=12, frameon=True)

ax1.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.show()