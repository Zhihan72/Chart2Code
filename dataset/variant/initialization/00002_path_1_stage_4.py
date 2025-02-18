import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])

fig, ax = plt.subplots(figsize=(12, 8))

# Shuffled colors and added another color
colors = ['#33FFA1', '#FF5733', '#A133FF', '#3357FF', '#57FF33', '#33FF57', '#FF33A1', '#FFA133']
# Changed the opacity and border width
ax.barh(decades, sea_surface_temp, height=8, color=colors, alpha=0.9, edgecolor='black', linewidth=1.5)

# Changed title position (using pad)
ax.set_title('SST by Decade', fontsize=16, pad=40)
# Changed xlabel styling
ax.set_xlabel('Temperature (°C)', fontsize=13, labelpad=10)
# Changed ylabel styling
ax.set_ylabel('Decade', fontsize=13, labelpad=10)
# Modified grid style
ax.grid(True, linestyle='-', color='grey', alpha=0.5)
# Changed legend location and added legend frame
ax.legend(loc='upper left', fontsize=11, frameon=True)

plt.tight_layout()
plt.show()