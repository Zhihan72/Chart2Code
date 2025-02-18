import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)
months = np.arange(1, 13)

monthly_temps = np.array([
    [2, 4, 8, 12, 17, 21, 24, 23, 20, 15, 9, 5],
    [1, 3, 6, 10, 15, 19, 22, 21, 17, 13, 7, 2],
    [0, 2, 5, 9, 14, 18, 21, 20, 16, 11, 6, 1],
    [2, 4, 7, 11, 16, 21, 23, 22, 19, 14, 8, 4],
    [0, 2, 5, 8, 13, 18, 21, 20, 16, 11, 6, 1],
    [1, 3, 6, 10, 15, 19, 22, 21, 17, 13, 7, 2],
    [2, 4, 8, 12, 17, 21, 24, 23, 20, 15, 9, 5],
    [1, 3, 6, 10, 15, 19, 22, 21, 17, 13, 7, 3],
    [0, 2, 5, 9, 14, 18, 21, 20, 16, 11, 6, 2],
    [1, 4, 7, 11, 16, 20, 23, 22, 18, 13, 7, 3]
])

average_temps = np.mean(monthly_temps, axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33', '#a65628', '#f781bf', '#999999', '#66c2a5']

for i, year in enumerate(years):
    ax.plot(months, monthly_temps[i], marker='o', linestyle='-', linewidth=2, markersize=6, color=colors[i])

ax.plot(months, average_temps, marker='D', linestyle='--', color='black', linewidth=2, markersize=8, zorder=10)

ax.set_xticks(months)

ax.grid(True, linestyle='--', alpha=0.6)

ax.set_xlim(1, 12)
ax.set_ylim(-5, 30)

ax.legend(loc='upper left', fontsize=12, ncol=2)

plt.tight_layout()
plt.show()