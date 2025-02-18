import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
lake_spring = [70, 90, 150, 130]
lake_silver = [50, 80, 120, 110]

lake_silver_cumulative = np.array(lake_spring) + np.array(lake_silver)

fig, ax = plt.subplots(figsize=(14, 8))

single_color = 'cornflowerblue'
alpha_value = 0.7

ax.fill_between(quarters, lake_spring, color=single_color, alpha=alpha_value)
ax.fill_between(quarters, lake_silver_cumulative, lake_spring, color=single_color, alpha=alpha_value)

ax.set_ylim(0, 250)
ax.set_yticks(range(0, 251, 50))
ax.set_xticks(np.arange(len(quarters)))
ax.set_xticklabels([''] * len(quarters))  # Empty string for labels to remove them

plt.tight_layout()
plt.show()