import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = np.array([1, 2, 4, 8, 12, 18, 25, 32, 40, 50, 60])
wind = np.array([5, 8, 11, 15, 20, 25, 31, 37, 45, 52, 60])
hydro = np.array([20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32])
biomass = np.array([2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16])
geothermal = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6])

energy_sources = np.vstack([solar, wind, hydro, biomass, geothermal])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Biomass', 'Geothermal'],
             colors=['#4682B4'], alpha=0.8)

ax.set_title('Renewable Energy Growth in Greenville (2010-2020)', fontsize=14, fontweight='light', pad=15)
ax.set_xlabel('Year', fontsize=12, style='italic')
ax.set_ylabel('Energy Output (TWh)', fontsize=12, style='italic')

ax.legend(loc='center right', fontsize=10, title='Sources', shadow=True)

ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 151, 30))

ax.xaxis.grid(True, linestyle='-.', linewidth=0.6, alpha=0.6)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linestyle('--')

ax.annotate('Major Solar Investment', xy=(2013, 8), xytext=(2016, 55),
            arrowprops=dict(color='gray', shrink=0.05),
            fontsize=9, ha='right', backgroundcolor='lightgrey')

ax.annotate('Wind Energy Boost', xy=(2017, 31), xytext=(2019, 70),
            arrowprops=dict(color='gray', shrink=0.05),
            fontsize=9, ha='center', backgroundcolor='lightgrey')

plt.tight_layout()
plt.show()