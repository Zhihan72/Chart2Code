import matplotlib.pyplot as plt
import numpy as np

# Data setup
years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
regions = ['North America', 'Europe', 'Asia']

solar = np.array([
    [40, 45, 50, 60, 65, 70],
    [30, 35, 40, 50, 55, 60],
    [50, 60, 70, 80, 90, 100]
])

wind = np.array([
    [60, 65, 70, 80, 85, 90],
    [50, 55, 65, 75, 80, 85],
    [40, 50, 60, 70, 80, 90]
])

hydro = np.array([
    [80, 85, 90, 95, 100, 105],
    [60, 65, 70, 75, 80, 85],
    [70, 75, 80, 85, 90, 95]
])

bar_width = 0.2  # Adjust the bar width to accommodate grouped bars
x = np.arange(len(years))

fig, ax = plt.subplots(figsize=(14, 9))

# Plotting grouped bars
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