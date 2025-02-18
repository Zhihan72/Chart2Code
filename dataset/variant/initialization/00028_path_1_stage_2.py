import matplotlib.pyplot as plt
import numpy as np

years = np.array([2015, 2016, 2017, 2018, 2019])
solar_output = np.array([220, 245, 260, 280, 310])
wind_output = np.array([180, 210, 230, 270, 290])
hydro_output = np.array([260, 255, 265, 270, 275])
geothermal_output = np.array([50, 55, 60, 65, 70])    # Added data for Geothermal Energy
biomass_output = np.array([40, 45, 50, 52, 54])       # Added data for Biomass Energy

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, solar_output, color='gold', marker='o', linewidth=2, linestyle='-')
ax.plot(years, wind_output, color='skyblue', marker='^', linewidth=2, linestyle='--')
ax.plot(years, hydro_output, color='blue', marker='s', linewidth=2, linestyle='-.')
ax.plot(years, geothermal_output, color='orange', marker='v', linewidth=2, linestyle=':')  # Plot for Geothermal
ax.plot(years, biomass_output, color='green', marker='P', linewidth=2, linestyle=':')      # Plot for Biomass

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Output (TWh)', fontsize=12)
ax.set_title('Annual Renewable Energy Output\nby Source (2015-2019)', fontsize=14)

plt.tight_layout()
plt.show()