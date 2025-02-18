import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1', '#A133FF', '#FFA133', '#33FFA1', '#57FF33']
ax.barh(decades, sea_surface_temp, height=8, color=colors, alpha=0.7, label=' SST (°C)')

ax.set_title('SST by Decade', fontsize=14, pad=20)
ax.set_xlabel('Temp (°C)', fontsize=12)
ax.set_ylabel('Decade', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='lower right', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()