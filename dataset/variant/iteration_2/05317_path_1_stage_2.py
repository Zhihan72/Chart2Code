import matplotlib.pyplot as plt
import numpy as np

years = np.arange(0, 11)

voyager_1 = np.array([0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55])
voyager_2 = np.array([0, 0.5, 2, 4, 7, 11, 16, 22, 29, 37, 46])
new_horizons = np.array([0, 1.2, 2.8, 5.1, 8.0, 11.0, 14.5, 18.5, 23.0, 28.0, 33.5])
juno = np.array([0, 0.8, 2.3, 4.5, 7.6, 11.2, 15.5, 20.2, 25.6, 31.5, 38.1])
cassini = np.array([0, 0.9, 2.5, 5.0, 8.5, 12.8, 17.4, 22.5, 28.3, 34.7, 41.8])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#F0E68C', '#8A2BE2']

ax.plot(years, voyager_1, marker='o', linestyle='-', linewidth=2, color=colors[0])
ax.plot(years, voyager_2, marker='^', linestyle='--', linewidth=2, color=colors[1])
ax.plot(years, new_horizons, marker='s', linestyle='-.', linewidth=2, color=colors[2])
ax.plot(years, juno, marker='D', linestyle=':', linewidth=2, color=colors[3])
ax.plot(years, cassini, marker='x', linestyle='-', linewidth=2, color=colors[4])

ax.set_xlabel("Years since Launch", fontsize=14)
ax.set_ylabel("Distance Traveled (Million km)", fontsize=14)

for i, d in enumerate([voyager_1, voyager_2, new_horizons, juno, cassini]):
    ax.text(years[-1] + 0.2, d[-1], f'{d[-1]:.1f}M km', horizontalalignment='left', size=10, color=colors[i])

plt.tight_layout()
plt.show()