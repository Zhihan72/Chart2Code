import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2030)

solar_usage = [1.8, 3.0, 2.4, 1.2, 6.7, 4.5, 3.8, 6.0, 5.2, 7.5]
wind_usage = [1.2, 2.3, 1.8, 0.8, 5.3, 3.6, 3.0, 4.7, 4.1, 6.0]
hydro_usage = [4.0, 5.0, 4.5, 3.5, 7.5, 6.0, 5.5, 7.0, 6.5, 8.0]
geothermal_usage = [0.8, 1.2, 1.0, 0.5, 2.3, 1.7, 1.5, 2.1, 1.9, 2.5]
biomass_usage = [0.5, 0.9, 0.7, 0.3, 1.9, 1.3, 1.1, 1.7, 1.5, 2.2]

fig, ax = plt.subplots(figsize=(12, 8))

single_color = 'midnightblue'

ax.plot(years, solar_usage, marker='v', linestyle=':', color=single_color, label='Sunshine Energy', linewidth=3)
ax.plot(years, wind_usage, marker='d', linestyle='-', color=single_color, label='Breeze Power', linewidth=2.5)
ax.plot(years, hydro_usage, marker='*', linestyle='--', color=single_color, label='Water Force', linewidth=2.5)
ax.plot(years, geothermal_usage, marker='p', linestyle='-.', color=single_color, label='Earth Heat', linewidth=2)
ax.plot(years, biomass_usage, marker='h', linestyle='-', color=single_color, label='Eco Biomatter', linewidth=3)

ax.set_title('EcoTrends in Renewable Power\n(2020-2030)', fontsize=18, fontweight='bold')
ax.set_xlabel('Timeline - Years', fontsize=14)
ax.set_ylabel('Consumption (TWh)', fontsize=14)

ax.legend(title='Power Types', loc='lower right', fontsize=10, shadow=True)

ax.grid(True, linestyle='-.', linewidth=0.7, alpha=0.5)

plt.tight_layout()

plt.show()