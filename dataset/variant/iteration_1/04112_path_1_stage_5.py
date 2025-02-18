import matplotlib.pyplot as plt
import numpy as np

years = np.array([2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023])

species_a_landing_density = np.array([33, 37, 30, 65, 45, 55, 35, 62, 60, 50])
species_b_landing_density = np.array([27, 20, 25, 42, 32, 40, 38, 45, 30, 35])
species_c_landing_density = np.array([13, 17, 10, 35, 23, 30, 32, 25, 27, 15])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.25
indices = np.arange(len(years))
common_color = 'blue'  # Apply a single color across all groups
ax.barh(indices, species_a_landing_density, bar_width, color=common_color, alpha=0.7)
ax.barh(indices + bar_width, species_b_landing_density, bar_width, color=common_color, alpha=0.7)
ax.barh(indices + 2 * bar_width, species_c_landing_density, bar_width, color=common_color, alpha=0.7)

ax.set_yticks(indices + bar_width)
ax.set_yticklabels(years)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()