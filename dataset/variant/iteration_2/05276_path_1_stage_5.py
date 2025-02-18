import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

hiking_east = [15, 18, 20, 22, 25, 28, 30, 35, 38, 40, 45]
cycling_east = [5, 7, 10, 12, 15, 20, 25, 28, 30, 33, 35]
running_east = [12, 15, 17, 20, 24, 28, 33, 37, 42, 45, 47]

hiking_west = [10, 13, 15, 17, 19, 22, 25, 28, 30, 32, 35]
cycling_west = [8, 10, 12, 15, 18, 21, 23, 26, 29, 31, 34]
running_west = [11, 14, 16, 18, 20, 24, 27, 29, 32, 35, 38]

fig, ax = plt.subplots(figsize=(12, 8))

# Plot for Eastern Region
ax.plot(years, hiking_east, marker='D', color='turquoise', linestyle='--', linewidth=2)
ax.plot(years, cycling_east, marker='+', color='lime', linestyle='-.', linewidth=2)
ax.plot(years, running_east, marker='x', color='magenta', linestyle=':', linewidth=2)

# Plot for Western Region
ax.plot(years, hiking_west, marker='D', color='navy', linestyle=':', linewidth=2)
ax.plot(years, cycling_west, marker='+', color='maroon', linestyle='--', linewidth=2)
ax.plot(years, running_west, marker='x', color='darkorange', linestyle='-.')

ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.6)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout(pad=2.0)
plt.show()