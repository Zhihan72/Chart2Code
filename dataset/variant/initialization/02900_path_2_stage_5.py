import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2021, 2022, 2023, 2024, 2025])
regions = ['North America', 'Europe', 'Asia', 'South America']

solar = np.array([
    [40, 45, 50, 60, 65, 70],
    [30, 35, 40, 50, 55, 60],
    [50, 60, 70, 80, 90, 100],
    [20, 25, 30, 35, 40, 45]
])

wind = np.array([
    [60, 65, 70, 80, 85, 90],
    [50, 55, 65, 75, 80, 85],
    [40, 50, 60, 70, 80, 90],
    [30, 35, 40, 45, 50, 55]
])

hydro = np.array([
    [80, 85, 90, 95, 100, 105],
    [60, 65, 70, 75, 80, 85],
    [70, 75, 80, 85, 90, 95],
    [50, 55, 60, 65, 70, 75]
])

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.25
x_positions = np.arange(len(years))
colors = ['#12CBC4', '#FFC312', '#C4E538']

for i, region in enumerate(regions):
    offset = i * bar_width
    ax.bar(x_positions + offset, solar[i], bar_width, label=f'Solar - {region}', color=colors[0], edgecolor='black', linewidth=0.5)
    ax.bar(x_positions + offset + len(regions) * bar_width, wind[i], bar_width, label=f'Wind - {region}', color=colors[1], edgecolor='black', linewidth=0.5)
    ax.bar(x_positions + offset + 2 * len(regions) * bar_width, hydro[i], bar_width, label=f'Hydro - {region}', color=colors[2], edgecolor='black', linewidth=0.5)

ax.set_xlabel('Year')
ax.set_ylabel('Energy Production')
ax.set_title('Grouped Bar Chart of Energy Production by Region')
ax.set_xticks(x_positions + len(regions) * bar_width)
ax.set_xticklabels(years)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()