import matplotlib.pyplot as plt
import numpy as np

countries = ['Germany', 'France', 'Italy', 'Spain', 'Sweden']
years = np.array([2019, 2020, 2021, 2022, 2023])
germany_farms = np.array([2300, 2450, 2600, 2750, 2900])
france_farms = np.array([2100, 2200, 2300, 2400, 2500])
italy_farms = np.array([1800, 1950, 2050, 2200, 2350])
spain_farms = np.array([1650, 1750, 1850, 2000, 2150])
sweden_farms = np.array([900, 950, 1000, 1050, 1100])

bar_height = 0.15
positions = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

ax.barh(positions, germany_farms, height=bar_height, color='cornflowerblue', edgecolor='grey', label='Germany')
ax.barh(positions + bar_height, france_farms, height=bar_height, color='seagreen', edgecolor='grey', label='France')
ax.barh(positions + 2 * bar_height, italy_farms, height=bar_height, color='tomato', edgecolor='grey', label='Italy')
ax.barh(positions + 3 * bar_height, spain_farms, height=bar_height, color='gold', edgecolor='grey', label='Spain')
ax.barh(positions + 4 * bar_height, sweden_farms, height=bar_height, color='mediumpurple', edgecolor='grey', label='Sweden')

for i in range(len(years)):
    ax.text(germany_farms[i] + 50, i, f'{germany_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(france_farms[i] + 50, i + bar_height, f'{france_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(italy_farms[i] + 50, i + 2 * bar_height, f'{italy_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(spain_farms[i] + 50, i + 3 * bar_height, f'{spain_farms[i]}', va='center', ha='left', color='black', fontsize=8)
    ax.text(sweden_farms[i] + 50, i + 4 * bar_height, f'{sweden_farms[i]}', va='center', ha='left', color='black', fontsize=8)

ax.set_ylabel('Year', fontsize=12, fontweight='bold')
ax.set_xlabel('Number of Organic Farms', fontsize=12, fontweight='bold')
ax.set_title('Growth of Organic Farms in Europe (2019-2023)', fontsize=16, fontweight='bold', pad=20)

ax.set_yticks(positions + 2 * bar_height)
ax.set_yticklabels(years)

ax.legend(loc='upper right', fontsize=12, title='Country')
ax.grid(axis='x', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()