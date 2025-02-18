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

fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

bar_width = 0.4
bar_depth = 0.4
consistent_color = '#FF5733'

for i, region in enumerate(regions):
    x_positions = np.arange(len(years))
    ax.bar3d(x_positions, i, np.zeros_like(years), bar_width, bar_depth, solar[i], color=consistent_color)
    ax.bar3d(x_positions, i, solar[i], bar_width, bar_depth, wind[i], color=consistent_color)
    ax.bar3d(x_positions, i, solar[i] + wind[i], bar_width, bar_depth, hydro[i], color=consistent_color)

ax.set_xlabel('Year', labelpad=10)
ax.set_ylabel('Region', labelpad=10)
ax.set_zlabel('Energy Production (TWh)', labelpad=10)

ax.set_xticks(np.arange(len(years)))
ax.set_xticklabels(years)
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)

ax.view_init(elev=20, azim=120)

ax.set_title('The Rise of Renewable Energy:\nRegional Production Trends (2020-2025)', pad=20, fontweight='bold', fontsize=14)

plt.tight_layout()
plt.show()