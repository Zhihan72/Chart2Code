import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s', '2010s', '2020s']
solar = [2, 3, 5, 10, 20, 30, 40]
wind = [1, 2, 10, 15, 25, 30, 25]
hydropower = [25, 30, 35, 28, 22, 18, 15]
biomass = [9, 8, 6, 5, 3, 2, 2]

data = np.vstack([solar, wind, hydropower, biomass])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(decades, data, labels=['Solar', 'Wind', 'Hydropower', 'Biomass'],
             colors=['#FFC300', '#FF5733', '#C70039', '#900C3F'], alpha=0.85, 
             edgecolor='darkgrey', linestyle='--')

ax.set_title('Renewable Energy Sources in Urban Development (1960s to 2020s)', fontsize=15, style='italic', loc='right')
ax.set_xlabel('Decade', fontsize=11)
ax.set_ylabel('Energy %', fontsize=11)

ax.legend(loc='lower left', bbox_to_anchor=(0, -0.2), fontsize=9, frameon=False)

ax.grid(True, linestyle=':', linewidth=0.5, color='gray')

plt.xticks(rotation=30, ha='left')
plt.tight_layout()

plt.show()