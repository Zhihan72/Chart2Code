import numpy as np
import matplotlib.pyplot as plt
from math import pi

attributes = ['Strength', 'Agility', 'Intelligence', 'Endurance', 'Charisma']
attribute_values = {
    'Warrior': [8, 5, 3, 9, 4],
    'Rogue': [5, 9, 4, 6, 5],
    'Mage': [3, 5, 9, 4, 6],
    'Paladin': [7, 4, 6, 8, 7]
    # 'Bard' removed
}

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

ax.set_rscale('log')
plt.ylim(0, 10)

# Plot all remaining data using a single color
for values in attribute_values.values():
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', color='blue')

plt.tight_layout()
plt.show()