import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])
# Additional data series
land_surface_temp = np.array([13.0, 13.5, 14.0, 14.5, 15.0, 15.3, 15.8, 16.1])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#33FFA1', '#FF5733', '#A133FF', '#3357FF', '#57FF33', '#33FF57', '#FF33A1', '#FFA133']
ax.barh(decades - 2, sea_surface_temp, height=3, color=colors, alpha=0.9, edgecolor='black', linewidth=1.5, label='Sea Surface Temp')
ax.barh(decades + 2, land_surface_temp, height=3, color=colors, alpha=0.6, edgecolor='black', linewidth=1.5, label='Land Surface Temp')

ax.set_title('Surface Temperature by Decade', fontsize=16, pad=40)
ax.set_xlabel('Temperature (°C)', fontsize=13, labelpad=10)
ax.set_ylabel('Decade', fontsize=13, labelpad=10)
ax.grid(True, linestyle='-', color='grey', alpha=0.5)
ax.legend(loc='upper left', fontsize=11, frameon=True)

plt.tight_layout()
plt.show()