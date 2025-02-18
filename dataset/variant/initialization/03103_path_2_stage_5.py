import numpy as np
import matplotlib.pyplot as plt
from math import pi

attributes = ['Strength', 'Agility', 'Intelligence', 'Endurance', 'Charisma']
attribute_values = {
    'Warrior': [8, 5, 3, 9, 4],
    'Rogue': [5, 9, 4, 6, 5],
    'Mage': [3, 5, 9, 4, 6],
    'Paladin': [7, 4, 6, 8, 7]
}

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(pi / 4)  # Altered theta offset
ax.set_theta_direction(1)    # Changed theta direction

marker_types = ['o', 's', 'D', '^']  # New marker types
line_styles = ['-', '--', '-.', ':']  # Diverse line styles
colors = ['red', 'green', 'purple', 'orange']  # Varied colors

for (key, values), marker, linestyle, color in zip(attribute_values.items(), marker_types, line_styles, colors):
    values += values[:1]
    ax.plot(angles, values, marker=marker, linestyle=linestyle, linewidth=2, color=color, label=key)

ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))  # Added legend

ax.grid(True, linestyle='--', linewidth=0.5, color='gray')  # Modified grid style
ax.spines['polar'].set_color('black')  # Changed border color
ax.spines['polar'].set_linewidth(1)

plt.ylim(0, 10)

plt.tight_layout()
plt.show()