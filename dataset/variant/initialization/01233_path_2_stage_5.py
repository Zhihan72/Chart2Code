import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2029)
countries = ['A', 'B', 'C', 'D']

solar = np.array([
    [10, 15, 20, 25, 30, 35],
    [5, 10, 15, 20, 25, 30],
    [8, 12, 18, 23, 28, 34],
    [12, 17, 22, 28, 33, 38]
])

wind = np.array([
    [15, 20, 25, 30, 35, 40],
    [12, 16, 22, 27, 32, 37],
    [10, 15, 20, 27, 33, 38],
    [18, 24, 30, 35, 40, 45]
])

hydro = np.array([
    [20, 25, 28, 32, 35, 40],
    [18, 23, 28, 32, 36, 41],
    [14, 20, 24, 30, 36, 42],
    [16, 21, 27, 33, 38, 44]
])

total_renewable = solar + wind + hydro
annual_totals = total_renewable.sum(axis=0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

bar_height = 0.15
y_indexes = np.arange(len(years))
single_color = '#4682B4'

for i in range(len(countries)):
    ax1.barh(y_indexes + i * bar_height, solar[i], height=bar_height, color=single_color, alpha=0.8)
    ax1.barh(y_indexes + i * bar_height, wind[i], left=solar[i], height=bar_height, color=single_color, alpha=0.8)
    ax1.barh(y_indexes + i * bar_height, hydro[i], left=solar[i] + wind[i], height=bar_height, color=single_color, alpha=0.8)

ax1.set_ylabel('Year', fontsize=12)
ax1.set_xlabel('Renewable (%)', fontsize=12)
ax1.set_title('Renewable Energy (2023-28)', fontsize=14, fontweight='bold')
ax1.set_yticks(y_indexes + bar_height * 1.5)
ax1.set_yticklabels(years)

ax2.plot(years, annual_totals, marker='o', color=single_color, linewidth=2)

for (year, total) in zip(years, annual_totals):
    ax2.text(year, total + 2, f'{total}', ha='center', fontsize=9, color=single_color)

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Total (%)', fontsize=12)
ax2.set_title('Cumulative Growth (2023-28)', fontsize=14, fontweight='bold')
ax2.set_xticks(years)
ax2.set_xticklabels(years)

plt.tight_layout()
plt.show()