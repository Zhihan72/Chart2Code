import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2030)

solar_usage = [1.2, 1.8, 2.4, 3.0, 3.8, 4.5, 5.2, 6.0, 6.7, 7.5]
wind_usage = [0.8, 1.2, 1.8, 2.3, 3.0, 3.6, 4.1, 4.7, 5.3, 6.0]
hydro_usage = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
geothermal_usage = [0.5, 0.8, 1.0, 1.2, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5]
biomass_usage = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_usage, marker='v', linestyle=':', color='darkorange', label='Solar', linewidth=3)
ax.plot(years, wind_usage, marker='d', linestyle='-', color='forestgreen', label='Wind', linewidth=2.5)
ax.plot(years, hydro_usage, marker='*', linestyle='--', color='navy', label='Hydro', linewidth=2.5)
ax.plot(years, geothermal_usage, marker='p', linestyle='-.', color='crimson', label='Geothermal', linewidth=2)
ax.plot(years, biomass_usage, marker='h', linestyle='-', color='indigo', label='Biomass', linewidth=3)

ax.set_title('Renewable Energy Usage Trends\nin EcoLand (2020-2030)', fontsize=18, fontweight='bold')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Usage (TWh)', fontsize=14)

ax.legend(title='Energy Sources', loc='lower right', fontsize=10, shadow=True)

ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

plt.tight_layout()

plt.show()