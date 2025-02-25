import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Participation rates in the Eastern Region (%)
hiking_east = [15, 18, 20, 22, 25, 28, 30, 35, 38, 40, 45]
cycling_east = [5, 7, 10, 12, 15, 20, 25, 28, 30, 33, 35]
running_east = [12, 15, 17, 20, 24, 28, 33, 37, 42, 45, 47]

# Participation rates in the Western Region (%)
hiking_west = [10, 13, 15, 17, 19, 22, 25, 28, 30, 32, 35]
cycling_west = [8, 10, 12, 15, 18, 21, 23, 26, 29, 31, 34]
running_west = [11, 14, 16, 18, 20, 24, 27, 29, 32, 35, 38]

fig, ax = plt.subplots(figsize=(12, 8))

# Plot for Eastern Region
ax.plot(years, hiking_east, marker='o', color='purple', linestyle='-', linewidth=2, label='Hiking (East)')
ax.plot(years, cycling_east, marker='s', color='orange', linestyle='-', linewidth=2, label='Cycling (East)')
ax.plot(years, running_east, marker='^', color='cyan', linestyle='-', linewidth=2, label='Running (East)')

# Plot for Western Region
ax.plot(years, hiking_west, marker='o', color='green', linestyle='-', linewidth=2, label='Hiking (West)')
ax.plot(years, cycling_west, marker='s', color='red', linestyle='-', linewidth=2, label='Cycling (West)')
ax.plot(years, running_west, marker='^', color='blue', linestyle='-', linewidth=2, label='Running (West)')

ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Participation Rate (%)', fontsize=14)
ax.set_title('Outdoor Activity Participation in Eastern and Western Regions (2010-2020)', fontsize=16, weight='bold')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout(pad=2.0)
plt.show()