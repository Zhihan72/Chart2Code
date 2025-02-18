import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)

solar = np.array([120, 100, 150, 240, 190, 300, 360, 510, 430, 600])  # Altered slightly within range
wind = np.array([270, 200, 230, 380, 320, 450, 530, 710, 620, 810])  # Altered slightly within range
hydro = np.array([1030, 1000, 1020, 1050, 1040, 1060, 1090, 1070, 1080, 1100])  # Altered slightly within range
geothermal = np.array([55, 50, 52, 62, 58, 67, 73, 88, 80, 97])  # Altered slightly within range
biomass = np.array([88, 75, 80, 105, 95, 118, 143, 130, 157, 172])  # Altered slightly within range

energy_sources = np.vstack([solar, wind, hydro, geothermal, biomass])

colors = ['#32CD32', '#FFD700', '#FF6347', '#00BFFF', '#1E90FF']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_sources, labels=['Sun Power', 'Wind Force', 'Water Flow', 'Earth Heat', 'Organic Mass'], colors=colors, alpha=0.8)

ax.set_title('Global Renewable Power Growth\n(Yearly Analysis 2012-2021)', fontsize=18, fontweight='heavy', pad=15)
ax.set_xlabel('Timeline (Years)', fontsize=12)
ax.set_ylabel('Production (Terawatt-hours)', fontsize=12)

ax.legend(loc='upper right', title='Source Types', fontsize=10, shadow=True, frameon=True, fancybox=True)

ax.set_xticks(years)
ax.set_xticklabels([f'Year {year}' for year in years], fontsize=10, rotation=45)

ax.yaxis.grid(True, linestyle='-.', linewidth=0.9, alpha=0.5)

ax.spines['top'].set_linestyle(':')
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_color('green')

plt.tight_layout()

plt.show()