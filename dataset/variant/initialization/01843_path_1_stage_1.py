import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2022)

solar = np.array([100, 120, 150, 190, 240, 300, 360, 430, 510, 600])
wind = np.array([200, 230, 270, 320, 380, 450, 530, 620, 710, 810])
hydro = np.array([1000, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100])
geothermal = np.array([50, 52, 55, 58, 62, 67, 73, 80, 88, 97])
biomass = np.array([75, 80, 88, 95, 105, 118, 130, 143, 157, 172])

energy_sources = np.vstack([solar, wind, hydro, geothermal, biomass])

colors = ['#FFD700', '#00BFFF', '#1E90FF', '#FF6347', '#32CD32']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, energy_sources, labels=['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'], colors=colors, alpha=0.8)

# Customizing the title and labels
ax.set_title('Trends in Global Renewable Energy Production\n(2012-2021)', fontsize=18, fontweight='heavy', pad=15)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Energy Production (TWh)', fontsize=12)

# Modifying legend
ax.legend(loc='upper right', title='Energy Sources', fontsize=10, shadow=True, frameon=True, fancybox=True)

# Customizing x-ticks
ax.set_xticks(years)
ax.set_xticklabels([f'{year}' for year in years], fontsize=10, rotation=45)

# Customizing grid lines
ax.yaxis.grid(True, linestyle='-.', linewidth=0.9, alpha=0.5)

# Experimenting with additional stylistic elements by adding border
ax.spines['top'].set_linestyle(':')
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_color('green')

plt.tight_layout()

plt.show()