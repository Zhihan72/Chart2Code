import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = np.array([1, 2, 4, 8, 12, 18, 25, 32, 40, 50, 60])
wind = np.array([5, 8, 11, 15, 20, 25, 31, 37, 45, 52, 60])
hydro = np.array([20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32])
biomass = np.array([2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16])
geothermal = np.array([1, 1, 2, 2, 3, 3, 4, 5, 7, 8, 10])

energy_sources = np.vstack([solar, wind, hydro, biomass, geothermal])

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, energy_sources, labels=['Sol', 'Wnd', 'Hyd', 'Bio', 'Geo'],
             colors=['#FF7F50', '#6A5ACD', '#FFA07A', '#20B2AA', '#778899'], alpha=0.8)

ax.set_title('Energy Growth (2010-20)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Yr', fontsize=14)
ax.set_ylabel('Output (TWh)', fontsize=14)

ax.legend(loc='upper left', fontsize=12, title='Source')

ax.set_xticks(years)
ax.set_yticks(np.arange(0, 171, 20))

ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax.annotate('Solar Up', xy=(2013, 8), xytext=(2015, 40),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

ax.annotate('Wind Boost', xy=(2017, 31), xytext=(2018, 70),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

plt.tight_layout()
plt.show()