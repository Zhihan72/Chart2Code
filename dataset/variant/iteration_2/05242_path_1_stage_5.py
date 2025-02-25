import matplotlib.pyplot as plt
import numpy as np

countries = ['DE', 'FR', 'IT', 'ES', 'SE']
years = np.array([2019, 2020, 2021, 2022, 2023])

germany_farms = np.array([2900, 2450, 2750, 2300, 2600])
france_farms = np.array([2400, 2500, 2200, 2300, 2100])
italy_farms = np.array([2050, 1800, 2200, 1950, 2350])
spain_farms = np.array([2000, 1650, 2150, 1750, 1850])
sweden_farms = np.array([1000, 1100, 950, 900, 1050])

bar_width = 0.15
positions = np.arange(len(years))
fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(positions, germany_farms, height=bar_width, color='cornflowerblue', label='Germany')
ax.barh(positions + bar_width, france_farms, height=bar_width, color='lightcoral', label='France')
ax.barh(positions + 2 * bar_width, italy_farms, height=bar_width, color='mediumseagreen', label='Italy')
ax.barh(positions + 3 * bar_width, spain_farms, height=bar_width, color='gold', label='Spain')
ax.barh(positions + 4 * bar_width, sweden_farms, height=bar_width, color='orange', label='Sweden')

for i in range(len(years)):
    ax.text(germany_farms[i] + 50, i, f'{germany_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(france_farms[i] + 50, i + bar_width, f'{france_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(italy_farms[i] + 50, i + 2 * bar_width, f'{italy_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(spain_farms[i] + 50, i + 3 * bar_width, f'{spain_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(sweden_farms[i] + 50, i + 4 * bar_width, f'{sweden_farms[i]}', va='center', ha='left', color='black', fontsize=8)

ax.set_ylabel('Year', fontsize=12, fontweight='bold')
ax.set_xlabel('No. of Farms', fontsize=12, fontweight='bold')
ax.set_title('Organic Farm Growth (2019-23) - Altered', fontsize=16, fontweight='bold', pad=20)
ax.set_yticks(positions + 2 * bar_width)
ax.set_yticklabels(years)
ax.legend()

plt.tight_layout()
plt.show()