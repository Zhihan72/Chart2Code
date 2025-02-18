import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)
solar = [20, 25, 30, 40, 50, 65, 80, 100, 130, 160]
wind = [50, 55, 60, 80, 100, 120, 150, 180, 210, 240]
bio = [30, 35, 40, 50, 55, 65, 75, 85, 95, 100]

# Removed 'hydro' data group
energy_data = np.vstack([solar, wind, bio])

fig, ax = plt.subplots(figsize=(10, 6))

ax.stackplot(years, energy_data, labels=['Solar', 'Wind', 'Biomass'],
             colors=['#ffa500', '#2e8b57', '#bc8f8f'], alpha=0.7,
             linewidth=2, edgecolor='white')

ax.set_title('Renewable Energy Usage: 2010-2019', fontsize=14, fontweight='bold', color='navy')
ax.set_xlabel('Year', fontsize=12, fontweight='bold', color='navy')
ax.set_ylabel('Energy (PJ)', fontsize=12, fontweight='bold', color='navy')

ax.grid(True, linestyle='-', linewidth=0.7, alpha=0.6)

ax.legend(loc='upper left', title='Energy Source', fontsize=11, title_fontsize='14', shadow=True, fancybox=True)

plt.xticks(years, rotation=30)
plt.yticks(np.arange(0, 301, 50))

plt.tight_layout()
plt.show()