import matplotlib.pyplot as plt
import numpy as np

years = np.arange(0, 11)  # 0 to 10 years

voyager_1 = np.array([0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55])
new_horizons = np.array([0, 1.2, 2.8, 5.1, 8.0, 11.0, 14.5, 18.5, 23.0, 28.0, 33.5])
juno = np.array([0, 0.8, 2.3, 4.5, 7.6, 11.2, 15.5, 20.2, 25.6, 31.5, 38.1])
cassini = np.array([0, 0.9, 2.5, 5.0, 8.5, 12.8, 17.4, 22.5, 28.3, 34.7, 41.8])

fig, ax = plt.subplots(figsize=(12, 8))

# Apply the same color to all plots
color = 'blue'

ax.plot(years, voyager_1, marker='o', linestyle='-', color=color, linewidth=2)
ax.plot(years, new_horizons, marker='s', linestyle='-.', color=color, linewidth=2)
ax.plot(years, juno, marker='D', linestyle=':', color=color, linewidth=2)
ax.plot(years, cassini, marker='x', linestyle='-', color=color, linewidth=2)

plt.tight_layout()
plt.show()