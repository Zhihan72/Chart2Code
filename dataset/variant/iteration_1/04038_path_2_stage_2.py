import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2030)
solar_usage = [1.2, 1.8, 2.4, 3.0, 3.8, 4.5, 5.2, 6.0, 6.7, 7.5]
wind_usage = [0.8, 1.2, 1.8, 2.3, 3.0, 3.6, 4.1, 4.7, 5.3, 6.0]
hydro_usage = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
geothermal_usage = [0.5, 0.8, 1.0, 1.2, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5]
biomass_usage = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2]

# Adding a new dataset for nuclear usage
nuclear_usage = [2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.3, 3.5, 3.8, 4.0]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_usage, marker='o', linestyle='-', color='orange', linewidth=2, label='Solar')
ax.plot(years, wind_usage, marker='s', linestyle='--', color='green', linewidth=2, label='Wind')
ax.plot(years, hydro_usage, marker='^', linestyle='-.', color='blue', linewidth=2, label='Hydro')
ax.plot(years, geothermal_usage, marker='D', linestyle=':', color='red', linewidth=2, label='Geothermal')
ax.plot(years, biomass_usage, marker='x', linestyle='-', color='purple', linewidth=2, label='Biomass')

# Plotting the new nuclear usage dataset
ax.plot(years, nuclear_usage, marker='*', linestyle='-', color='black', linewidth=2, label='Nuclear')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Usage (TWh)', fontsize=14)
ax.legend()

plt.tight_layout()
plt.show()