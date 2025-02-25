import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2030)

solar_usage = [1.2, 1.8, 2.4, 3.0, 3.8, 4.5, 5.2, 6.0, 6.7, 7.5]
wind_usage = [0.8, 1.2, 1.8, 2.3, 3.0, 3.6, 4.1, 4.7, 5.3, 6.0]
hydro_usage = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]
geothermal_usage = [0.5, 0.8, 1.0, 1.2, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5]
biomass_usage = [0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9, 2.2]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_usage, marker='v', linestyle=':', color='darkorange', label='Sunshine Energy', linewidth=3)
ax.plot(years, wind_usage, marker='d', linestyle='-', color='forestgreen', label='Breeze Power', linewidth=2.5)
ax.plot(years, hydro_usage, marker='*', linestyle='--', color='navy', label='Water Force', linewidth=2.5)
ax.plot(years, geothermal_usage, marker='p', linestyle='-.', color='crimson', label='Earth Heat', linewidth=2)
ax.plot(years, biomass_usage, marker='h', linestyle='-', color='indigo', label='Eco Biomatter', linewidth=3)

ax.set_title('EcoTrends in Renewable Power\n(2020-2030)', fontsize=18, fontweight='bold')
ax.set_xlabel('Timeline - Years', fontsize=14)
ax.set_ylabel('Consumption (TWh)', fontsize=14)

ax.legend(title='Power Types', loc='lower right', fontsize=10, shadow=True)

ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

plt.tight_layout()

plt.show()