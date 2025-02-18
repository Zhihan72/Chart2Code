import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the attributes and character classes
attributes = ['Strength', 'Agility', 'Intelligence', 'Endurance', 'Charisma']
character_classes = ['Warrior', 'Rogue', 'Mage', 'Paladin', 'Bard']

# Define the attribute values for each class
attribute_values = {
    'Warrior': [8, 5, 3, 9, 4],
    'Rogue': [5, 9, 4, 6, 5],
    'Mage': [3, 5, 9, 4, 6],
    'Paladin': [7, 4, 6, 8, 7],
    'Bard': [4, 7, 5, 5, 9]
}

num_attributes = len(attributes)
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the circle

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], attributes, color='grey', size=10)

ax.set_rscale('log')
plt.yticks([1, 3, 5, 7, 9], ["1", "3", "5", "7", "9"], color='grey', size=7)
plt.ylim(0, 10)

# Plot data without filling
for char_class, values in attribute_values.items():
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=char_class)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), fontsize=10)

# Add a title
plt.title("Fantasy RPG Character Attributes\nClass Strengths and Weaknesses", size=15, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()