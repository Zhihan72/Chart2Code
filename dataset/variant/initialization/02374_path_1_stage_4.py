import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_power = [5, 6, 8, 12, 15, 19, 25, 30, 40, 45, 50]
wind_energy = [10, 12, 15, 17, 21, 24, 28, 32, 37, 39, 42]
hydroelectric_power = [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]
biomass_energy = [3, 4, 5, 6, 7, 8, 10, 12, 14, 15, 16]  # New data series added

plt.figure(figsize=(12, 8))

new_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

plt.plot(years, solar_power, marker='o', linestyle='-', color=new_colors[0], linewidth=2)
plt.plot(years, wind_energy, marker='^', linestyle='--', color=new_colors[1], linewidth=2)
plt.plot(years, hydroelectric_power, marker='s', linestyle='-.', color=new_colors[2], linewidth=2)
plt.plot(years, biomass_energy, marker='d', linestyle=':', color=new_colors[3], linewidth=2)  # Plot new data series

plt.title('Renewable Energy (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Contribution (%)', fontsize=12)

plt.xticks(years, rotation=45)
plt.legend(['Solar Power', 'Wind Energy', 'Hydroelectric Power', 'Biomass Energy'], loc='upper left')

plt.tight_layout()
plt.show()