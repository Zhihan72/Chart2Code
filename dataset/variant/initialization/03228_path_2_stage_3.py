import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ["Hygiene Standards", "Creativity", "Knifing Skills", "Sauce Prep", "Baking", "Plating"]
num_vars = len(categories)

# Manually shuffled or altered data within each chef's skills
chef_aurora = [9, 7, 8, 9, 7, 8]
chef_blake = [8, 9, 7, 9, 8, 8]

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def complete_data(data):
    return data + data[:1]

aurora_data = complete_data(chef_aurora)
blake_data = complete_data(chef_blake)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='black', size=10)
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["II", "IV", "VI", "VIII", "X"], color="grey", size=8)
plt.ylim(0, 10)

color = 'royalblue'
ax.plot(angles, aurora_data, linewidth=2, linestyle='solid', label='Aurora the Chef', color=color)
ax.fill(angles, aurora_data, color=color, alpha=0.25)

ax.plot(angles, blake_data, linewidth=2, linestyle='dotted', label='Chef B', color=color)
ax.fill(angles, blake_data, color=color, alpha=0.25)

plt.title("Mastery in Culinary: Skills Radar", size=15, color='black', weight='bold', pad=20)
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.tight_layout()
plt.show()