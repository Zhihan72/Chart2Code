import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019])
solar_output = np.array([220, 245, 260, 280, 310])
wind_output = np.array([180, 210, 230, 270, 290])
hydro_output = np.array([260, 255, 265, 270, 275])
geothermal_output = np.array([90, 95, 100, 105, 110])

fig, ax = plt.subplots(figsize=(10, 6))

# Apply the same color 'green' for all data groups
ax.plot(years, solar_output, label='SunPower Yield', color='green', marker='x', linewidth=1.5, linestyle='-.')
ax.plot(years, wind_output, label='Breeze Energy', color='green', marker='s', linewidth=2.5, linestyle='-')
ax.plot(years, hydro_output, label='WaterFlow Energy', color='green', marker='^', linewidth=2, linestyle=':')
ax.plot(years, geothermal_output, label='EarthHeat Energy', color='green', marker='o', linewidth=3, linestyle='--')

ax.set_xlabel('Yearly Recordings', fontsize=11)
ax.set_ylabel('Output (Thousand MWh)', fontsize=11)
ax.set_title('Yearly Renewable Power Generation\nSources (2015-2019)', fontsize=15)

ax.grid(True, linestyle='-', alpha=0.8)

ax.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.show()