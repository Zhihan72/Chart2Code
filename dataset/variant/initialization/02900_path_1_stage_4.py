import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
regions = ['North America', 'Europe', 'Asia']

# Alter data by shuffling values within each region (but not across energy types)
solar = np.array([
    [60, 65, 45, 70, 40, 50],
    [35, 30, 60, 50, 40, 55],
    [90, 70, 100, 60, 80, 50],
])

wind = np.array([
    [90, 70, 85, 60, 80, 65],
    [75, 55, 50, 80, 85, 65],
    [60, 70, 80, 90, 50, 40],
])

hydro = np.array([
    [100, 85, 80, 105, 95, 90],
    [60, 70, 65, 85, 75, 80],
    [75, 90, 85, 95, 80, 70],
])

bar_width = 0.2
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 9))

for i, region in enumerate(regions):
    ax.bar(x + i*bar_width, solar[i], width=bar_width, label=f'Solar - {region}')
    ax.bar(x + i*bar_width, wind[i], width=bar_width, bottom=solar[i], label=f'Wind - {region}')
    ax.bar(x + i*bar_width, hydro[i], width=bar_width, bottom=solar[i] + wind[i], label=f'Hydro - {region}')

ax.set_xlabel('Year')
ax.set_ylabel('Energy Production (TWh)')
ax.set_title('The Rise of Renewable Energy: Regional Production Trends (2020-2025)', fontweight='bold', fontsize=14)

ax.set_xticks(x + bar_width)
ax.set_xticklabels(years)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.show()