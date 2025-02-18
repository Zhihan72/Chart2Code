import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = [5, 6, 8, 10, 13, 16, 20, 25, 30, 35, 40]
wind_energy = [10, 12, 15, 18, 22, 27, 33, 39, 46, 53, 60]
hydro_energy = [20, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
geothermal_energy = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Total energy usage remains unchanged because we use it in the second subplot
total_energy_usage = np.array(solar_energy) + np.array(wind_energy) + np.array(hydro_energy) + np.array(geothermal_energy)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), gridspec_kw={'width_ratios': [2, 1]})

# Parameters for grouped bar plotting; using 4 sets equally spaced
bar_width = 0.2  
x_indices = np.arange(len(years))

ax1.bar(x_indices, solar_energy, width=bar_width, label='Solar')
ax1.bar(x_indices + bar_width, wind_energy, width=bar_width, label='Wind')
ax1.bar(x_indices + 2*bar_width, hydro_energy, width=bar_width, label='Hydro')
ax1.bar(x_indices + 3*bar_width, geothermal_energy, width=bar_width, label='Geothermal')

ax1.set_xticks(x_indices + 1.5*bar_width)
ax1.set_xticklabels(years, rotation=45)
ax1.grid(True, axis='y', linestyle='--', alpha=0.7)
ax1.legend()

# Line Plot of Total Energy Usage
ax2.plot(years, total_energy_usage, marker='o', linestyle='-', color='#1f77b4')
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()