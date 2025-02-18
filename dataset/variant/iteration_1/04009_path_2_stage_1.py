import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_energy = [5, 6, 8, 10, 13, 16, 20, 25, 30, 35, 40]
wind_energy = [10, 12, 15, 18, 22, 27, 33, 39, 46, 53, 60]
hydro_energy = [20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
geothermal_energy = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

total_energy_usage = (np.array(solar_energy) +
                      np.array(wind_energy) +
                      np.array(hydro_energy) +
                      np.array(geothermal_energy))

# Create a figure with two subplots, arranged vertically
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Stacked Bar Chart for Renewable Energy Usage
ax1.bar(years, solar_energy, label='Solar', color='#FFC300')
ax1.bar(years, wind_energy, bottom=solar_energy, label='Wind', color='#2E86C1')
ax1.bar(years, hydro_energy, bottom=np.array(solar_energy) + np.array(wind_energy), label='Hydro', color='#28B463')
ax1.bar(years, geothermal_energy, bottom=np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy), label='Geothermal', color='#CB4335')

ax1.set_title("Renewable Energy Usage Trends (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Usage (TWh)", fontsize=12)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(title='Energy Source', loc='upper left', bbox_to_anchor=(1, 1))
ax1.grid(True, axis='y', linestyle='--', alpha=0.7)

# Line Plot for Total Energy Usage
ax2.plot(years, total_energy_usage, marker='o', linestyle='-', color='purple', label='Total Energy Usage')
ax2.set_title("Total Renewable Energy Usage Per Year", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Energy Usage (TWh)", fontsize=12)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.legend(loc='upper right')
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()