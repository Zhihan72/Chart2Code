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

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

bar_width = 0.3
bar_depth = 0.5
colors = ['#12CBC4', '#FFC312', '#C4E538']  # Shuffled color assignments

for i, region in enumerate(regions):
    x_positions = np.arange(len(years))
    ax.bar3d(x_positions, i, np.zeros_like(years), bar_width, bar_depth, solar[i], color=colors[0], edgecolor='black', linewidth=0.5, linestyle='-.')
    ax.bar3d(x_positions, i, solar[i], bar_width, bar_depth, wind[i], color=colors[1], edgecolor='black', linewidth=0.5, linestyle=':')
    ax.bar3d(x_positions, i, solar[i] + wind[i], bar_width, bar_depth, hydro[i], color=colors[2], edgecolor='black', linewidth=0.5, linestyle='--')

ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')

ax.set_xticks([])
ax.set_yticks([])

ax.set_title('')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.spines['top'].set_linestyle('dotted')
ax.spines['top'].set_linewidth(0.8)

ax.view_init(elev=25, azim=135)

plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()