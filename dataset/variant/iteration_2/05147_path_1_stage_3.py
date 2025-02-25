import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020])

solar_energy = np.array([10, 20, 35, 55, 85, 130])
wind_energy = np.array([40, 55, 75, 95, 120, 150])
hydro_energy = np.array([300, 320, 340, 360, 380, 400])
geothermal_energy = np.array([15, 17, 19, 25, 30, 42])

solar_cost_reduction = np.array([200, 160, 130, 100, 75, 50])
wind_cost_reduction = np.array([95, 90, 85, 75, 60, 45])
hydro_cost_reduction = np.array([60, 58, 55, 53, 50, 48])
geothermal_cost_reduction = np.array([170, 150, 140, 130, 120, 110])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, solar_energy, label='Solar Energy', color='orchid', marker='v', linestyle='-', linewidth=1.5)
ax1.plot(years, wind_energy, label='Wind Energy', color='royalblue', marker='d', linestyle=':', linewidth=2)
ax1.plot(years, hydro_energy, label='Hydro Energy', color='peru', marker='p', linestyle='--', linewidth=2.5)
ax1.plot(years, geothermal_energy, label='Geothermal Energy', color='mediumseagreen', marker='*', linestyle='-.', linewidth=2)

ax1.set_title('Growth of Renewable Energy Production and Cost Reduction (2010-2020)', fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Energy Production (TWh)', fontsize=14)

ax2 = ax1.twinx()
ax2.set_ylabel('Cost Reduction ($/MWh)', fontsize=14, color='tab:red')
ax2.plot(years, solar_cost_reduction, label='Solar Cost', color='darkorange', marker='H', linestyle='--', linewidth=2)
ax2.plot(years, wind_cost_reduction, label='Wind Cost', color='darkcyan', marker='3', linestyle='-.', linewidth=2.5)
ax2.plot(years, hydro_cost_reduction, label='Hydro Cost', color='saddlebrown', marker='x', linestyle='-', linewidth=1.5)
ax2.plot(years, geothermal_cost_reduction, label='Geothermal Cost', color='dodgerblue', marker='8', linestyle='--', linewidth=2.5)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='best', fontsize=10, frameon=False)

ax1.grid(True, linestyle='-', alpha=0.3)

plt.tight_layout()

plt.show()