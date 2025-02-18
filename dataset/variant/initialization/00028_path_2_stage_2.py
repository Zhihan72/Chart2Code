import matplotlib.pyplot as plt
import numpy as np

# Years of observation
years = np.array([2015, 2016, 2017, 2018, 2019])

# Energy output data in TWh for each year
solar_output = np.array([220, 245, 260, 280, 310])
wind_output = np.array([180, 210, 230, 270, 290])
hydro_output = np.array([260, 255, 265, 270, 275])
geothermal_output = np.array([90, 95, 100, 105, 110])

# Create the line plot
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, solar_output, label='Solar Energy', color='gold', marker='x', linewidth=1.5, linestyle='-.')
ax.plot(years, wind_output, label='Wind Energy', color='skyblue', marker='s', linewidth=2.5, linestyle='-')
ax.plot(years, hydro_output, label='Hydro Energy', color='blue', marker='^', linewidth=2, linestyle=':')
ax.plot(years, geothermal_output, label='Geothermal Energy', color='darkorange', marker='o', linewidth=3, linestyle='--')

ax.set_xlabel('Year', fontsize=11)
ax.set_ylabel('Energy Output (TWh)', fontsize=11)
ax.set_title('Annual Renewable Energy Output\nby Source (2015-2019)', fontsize=15)

ax.grid(True, linestyle='-', alpha=0.8)

ax.legend(loc='lower right', fontsize=11)

plt.tight_layout()
plt.show()