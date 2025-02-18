import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

assembly_robots = [0, 5, 10, 20, 35, 50, 70, 85, 100, 120, 140, 150, 155, 160, 150, 130, 110, 90, 60, 30, 15]
painting_robots = [0, 2, 5, 10, 18, 30, 45, 55, 65, 75, 85, 90, 95, 98, 92, 80, 65, 55, 35, 20, 10]
welding_robots = [0, 3, 8, 15, 25, 40, 55, 70, 90, 110, 130, 145, 150, 155, 145, 125, 105, 80, 50, 25, 10]
packaging_robots = [0, 1, 3, 6, 10, 15, 22, 30, 42, 54, 68, 75, 80, 85, 80, 70, 55, 45, 30, 15, 5]

robots_data = np.vstack([assembly_robots, painting_robots, welding_robots, packaging_robots])
cumulative_data = np.cumsum(robots_data, axis=0)

colors = ['#FF4500', '#4682B4', '#32CD32', '#DAA520']

fig, ax = plt.subplots(figsize=(14, 9))

ax.fill_between(years, 0, cumulative_data[0], color=colors[0], alpha=0.85)
ax.fill_between(years, cumulative_data[0], cumulative_data[1], color=colors[1], alpha=0.85)
ax.fill_between(years, cumulative_data[1], cumulative_data[2], color=colors[2], alpha=0.85)
ax.fill_between(years, cumulative_data[2], cumulative_data[3], color=colors[3], alpha=0.85)

# Remove legends, grids, and borders
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.tight_layout()

plt.show()