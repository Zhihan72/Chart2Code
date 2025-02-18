import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)

solar = np.array([100, 120, 150, 190, 240, 300, 360, 430, 510, 600])
wind = np.array([200, 230, 270, 320, 380, 450, 530, 620, 710, 810])
hydro = np.array([1000, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100])
geothermal = np.array([50, 52, 55, 58, 62, 67, 73, 80, 88, 97])

energy_sources = np.vstack([solar, wind, hydro, geothermal])

altered_colors = ['#6495ED', '#FFD700', '#228B22', '#FF69B4']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal'], colors=altered_colors, alpha=0.7)

ax.set_title('Trends in Global Renewable Energy Production\n(2012-2021)', fontsize=18, fontweight='normal', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('Energy Production (TWh)', fontsize=13)

ax.legend(loc='lower right', title='Energy Types', fontsize=11, title_fontsize='13')

ax.xaxis.grid(True, linestyle='-', alpha=0.5)

ax.set_xticks(years)
ax.set_xticklabels([str(year) for year in years], fontsize=10, rotation=45)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()