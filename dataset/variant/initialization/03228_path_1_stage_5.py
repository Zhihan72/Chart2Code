import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ["Chopping", "Grilling", "Decoration", "Sauce Mixology", "Innovation", "Sanitation Protocol"]
num_vars = len(categories)

# Manually shuffled scores for both chefs
chef_amber = [9, 8, 7, 9, 8, 7]
chef_charlie = [8, 9, 9, 8, 7, 8]

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

amber_data = chef_amber + chef_amber[:1]
charlie_data = chef_charlie + chef_charlie[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='black', size=10)
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["1", "3", "5", "7", "9"], color="grey", size=8)
plt.ylim(0, 10)

ax.plot(angles, amber_data, linewidth=2, linestyle='dashdot', marker='o', label='Chef Amber', color='orange')
ax.fill(angles, amber_data, color='orange', alpha=0.25)

ax.plot(angles, charlie_data, linewidth=2, linestyle='dashed', marker='s', label='Chef Charlie', color='teal')
ax.fill(angles, charlie_data, color='teal', alpha=0.25)

ax.grid(True, linestyle='--')

ax.spines['polar'].set_visible(False)

plt.title("Gourmet Cooking Avengers: A Culinary Radar", size=15, color='black', weight='bold', pad=20)
plt.legend(loc='upper left')

plt.tight_layout()

plt.show()