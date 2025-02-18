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

# Changed the color for all bars to 'cornflowerblue'
ax.bar(positions, germany_farms, width=bar_width, color='cornflowerblue', edgecolor='grey', label='DE')
ax.bar(positions + bar_width, france_farms, width=bar_width, color='cornflowerblue', edgecolor='grey', label='FR')
ax.bar(positions + 2 * bar_width, italy_farms, width=bar_width, color='cornflowerblue', edgecolor='grey', label='IT')
ax.bar(positions + 3 * bar_width, spain_farms, width=bar_width, color='cornflowerblue', edgecolor='grey', label='ES')
ax.bar(positions + 4 * bar_width, sweden_farms, width=bar_width, color='cornflowerblue', edgecolor='grey', label='SE')

for i in range(len(years)):
    ax.text(i, germany_farms[i] + 50, f'{germany_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + bar_width, france_farms[i] + 50, f'{france_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + 2 * bar_width, italy_farms[i] + 50, f'{italy_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + 3 * bar_width, spain_farms[i] + 50, f'{spain_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)
    ax.text(i + 4 * bar_width, sweden_farms[i] + 50, f'{sweden_farms[i]}', ha='center', va='bottom', color='black', fontsize=8)

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('No. of Farms', fontsize=12, fontweight='bold')
ax.set_title('Organic Farm Growth (2019-23) - Altered', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(positions + 2 * bar_width)
ax.set_xticklabels(years)
ax.legend(loc='upper left', fontsize=12, title='Country')
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()