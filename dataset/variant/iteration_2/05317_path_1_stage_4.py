import matplotlib.pyplot as plt
import numpy as np

years = np.arange(0, 11)

voyager_1 = np.array([0, 1, 2, 7, 9, 13, 21, 31, 33, 42, 56])
voyager_2 = np.array([0, 1, 1.5, 3, 6, 9, 17, 20, 32, 35, 47])
new_horizons = np.array([0, 1.5, 3, 5.5, 7.5, 12, 14, 19, 22.5, 30, 35])
juno = np.array([0, 1, 3, 4, 8, 10.2, 16.5, 19, 27, 30.5, 37.5])
cassini = np.array([0, 1.2, 2, 4, 9, 13, 16, 22, 29, 34, 40])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C', '#8A2BE2']

ax.plot(years, voyager_1, marker='o', linestyle='-', linewidth=2, color=colors[0], label='V1')
ax.plot(years, voyager_2, marker='^', linestyle='--', linewidth=2, color=colors[1], label='V2')
ax.plot(years, new_horizons, marker='s', linestyle='-.', linewidth=2, color=colors[2], label='NH')
ax.plot(years, juno, marker='D', linestyle=':', linewidth=2, color=colors[3], label='Juno')
ax.plot(years, cassini, marker='x', linestyle='-', linewidth=2, color=colors[4], label='Cassini')

ax.set_xlabel("Years", fontsize=14)
ax.set_ylabel("Distance (M km)", fontsize=14)

for i, d in enumerate([voyager_1, voyager_2, new_horizons, juno, cassini]):
    ax.text(years[-1] + 0.2, d[-1], f'{d[-1]:.1f}M', horizontalalignment='left', size=10, color=colors[i])

plt.legend()
plt.tight_layout()
plt.show()