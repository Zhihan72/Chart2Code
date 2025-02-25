import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

hiking_east = [18, 20, 15, 22, 28, 30, 25, 38, 35, 40, 45]
hiking_west = [12, 14, 10, 21, 16, 18, 24, 30, 27, 36, 33]
cycling_east = [10, 7, 5, 12, 15, 25, 20, 33, 28, 30, 35]
cycling_west = [12, 8, 15, 22, 10, 18, 28, 25, 30, 33, 32]
running_east = [17, 15, 20, 28, 12, 24, 37, 33, 42, 47, 45]
running_west = [25, 20, 30, 35, 22, 28, 40, 38, 42, 45, 48]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

ax1.plot(years, hiking_west, marker='o', color='purple', linestyle='-', linewidth=2)
ax1.plot(years, cycling_west, marker='s', color='orange', linestyle='-', linewidth=2)
ax1.plot(years, running_west, marker='^', color='cyan', linestyle='-', linewidth=2)
ax1.set_ylabel('Rate (%)', fontsize=14)
ax1.set_title('Western Region (2010-2020)', fontsize=16, weight='bold')

ax2.plot(years, hiking_east, marker='o', color='purple', linestyle='-', linewidth=2)
ax2.plot(years, cycling_east, marker='s', color='orange', linestyle='-', linewidth=2)
ax2.plot(years, running_east, marker='^', color='cyan', linestyle='-', linewidth=2)
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Rate (%)', fontsize=14)
ax2.set_title('Eastern Region (2010-2020)', fontsize=16, weight='bold')

plt.suptitle('Activity Trends (East vs West)', fontsize=20, weight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.show()