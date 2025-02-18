import matplotlib.pyplot as plt
import numpy as np
from math import pi

categories = ["Hygiene Standards", "Creativity", "Knifing Skills", "Sauce Prep", "Baking", "Plating"]
num_vars = len(categories)

chef_aurora = [9, 7, 8, 9, 7, 8]
chef_blake = [8, 9, 7, 9, 8, 8]

angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def complete_data(data):
    return data + data[:1]

aurora_data = complete_data(chef_aurora)
blake_data = complete_data(chef_blake)

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], categories, color='darkred', size=11)
ax.set_rlabel_position(45)
plt.yticks([2, 4, 6, 8, 10], ["II", "IV", "VI", "VIII", "X"], color="black", size=9)
plt.ylim(0, 10)

# Plotting and filling data for Aurora
ax.fill(angles, aurora_data, color='coral', alpha=0.5, label='Aurora')

# Plotting and filling data for Blake
ax.fill(angles, blake_data, color='teal', alpha=0.5, label='Blake')

plt.title("Mastery in Culinary: Skills Radar", size=16, color='navy', weight='bold', pad=15)
plt.legend(loc='upper left', bbox_to_anchor=(0.9, 0.9), fontsize=10, frameon=False)
ax.yaxis.grid(True, color='gray', linestyle=':', linewidth=0.7)

plt.tight_layout()
plt.show()