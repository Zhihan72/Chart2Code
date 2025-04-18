import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Title and Backstory
# Imagine a scenario where different mythical creatures are evaluated based on various magical attributes.
# This chart compares the magical attributes of a Dragon, Phoenix, and Unicorn.

# Define magical attributes and their respective scores for each creature
attributes = ['Fire Power', 'Healing', 'Flight Speed', 'Mystical Aura', 'Wisdom', 'Strength']
dragonscore = [9, 6, 10, 7, 8, 9]
phoenixscore = [8, 9, 9, 5, 8, 7]
unicornscore = [6, 10, 6, 9, 9, 6]

# Number of variables/attributes
num_attributes = len(attributes)

# Compute the angle for each attribute
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]

# Duplicate the first score to close the radar chart
dragonscore += dragonscore[:1]
phoenixscore += phoenixscore[:1]
unicornscore += unicornscore[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define the radar plots for each creature
ax.plot(angles, dragonscore, linewidth=2, linestyle='-', marker='o', color='red', label='Dragon')
ax.fill(angles, dragonscore, 'red', alpha=0.25)

ax.plot(angles, phoenixscore, linewidth=2, linestyle='-', marker='o', color='orange', label='Phoenix')
ax.fill(angles, phoenixscore, 'orange', alpha=0.25)

ax.plot(angles, unicornscore, linewidth=2, linestyle='-', marker='o', color='purple', label='Unicorn')
ax.fill(angles, unicornscore, 'purple', alpha=0.25)

# Add attribute labels
plt.xticks(angles[:-1], attributes, color='darkslategray', size=12)

# Add title
plt.title("Mythical Creatures: Comparative Magical Attributes", size=16, weight='bold', pad=20)

# Customize radial labels and grid
ax.yaxis.set_tick_params(labelsize=10, colors='darkslategray')
ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
plt.yticks(range(1, 11), ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], color='grey', size=10)
plt.ylim(0, 10)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Adjust layout and display the radar chart
plt.tight_layout()
plt.show()