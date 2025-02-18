import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
lake_spring = [70, 90, 150, 130]
lake_silver = [50, 80, 120, 110]
lake_blue = [40, 60, 90, 85]
lake_green = [30, 40, 60, 55]

lake_silver_cumulative = np.array(lake_spring) + np.array(lake_silver)
lake_blue_cumulative = lake_silver_cumulative + np.array(lake_blue)
total_water_levels = lake_blue_cumulative + np.array(lake_green)

fig, ax = plt.subplots(figsize=(14, 8))

# Assign shuffled colors to each lake
ax.fill_between(quarters, lake_spring, color='lightgreen', alpha=0.7)
ax.fill_between(quarters, lake_silver_cumulative, lake_spring, color='lightcoral', alpha=0.7)
ax.fill_between(quarters, lake_blue_cumulative, lake_silver_cumulative, color='lightgrey', alpha=0.7)
ax.fill_between(quarters, total_water_levels, lake_blue_cumulative, color='lightblue', alpha=0.7)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.6)
ax.set_ylim(0, 400)
ax.set_yticks(range(0, 401, 50))
ax.set_xticks(np.arange(len(quarters)))
ax.set_xticklabels(quarters, rotation=45, ha='right')

plt.tight_layout()
plt.show()