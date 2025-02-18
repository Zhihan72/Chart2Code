import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2018, 2023)

apples_production = [135, 150, 120, 140, 130]
bananas_production = [100, 90, 110, 95, 105]
oranges_production = [125, 130, 115, 110, 120]

bar_height = 0.25

r1 = np.arange(len(years))
r2 = [x + bar_height for x in r1]
r3 = [x + bar_height for x in r2]

fig, ax = plt.subplots(figsize=(12, 7))

# Plot horizontal bars
ax.barh(r1, apples_production, color='orange', height=bar_height, edgecolor='grey')
ax.barh(r2, bananas_production, color='red', height=bar_height, edgecolor='grey')
ax.barh(r3, oranges_production, color='yellow', height=bar_height, edgecolor='grey')

# The below lines have been removed to eliminate textual elements:
# add_labels(bars1, ax)
# add_labels(bars2, ax)
# add_labels(bars3, ax)
# ax.set_title(...)
# ax.set_ylabel(...)
# ax.set_xlabel(...)
# ax.set_yticks([...])
# ax.set_yticklabels(years)
# ax.legend()

ax.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()