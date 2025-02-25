import matplotlib.pyplot as plt
import numpy as np

# Define the categories for character attributes
categories = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
n_vars = len(categories)

# Characters' attribute scores
wizard = [4, 6, 5, 9, 8, 6]
warrior = [9, 7, 8, 5, 4, 6]
rogue = [6, 9, 5, 7, 6, 7]
paladin = [8, 5, 9, 6, 7, 5]
druid = [5, 6, 7, 8, 9, 6]

# Repeat the first value to close the radar chart loop
wizard += wizard[:1]
warrior += warrior[:1]
rogue += rogue[:1]
paladin += paladin[:1]
druid += druid[:1]

# Calculate angles for each category (including closure)
angles = np.linspace(0, 2 * np.pi, n_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each character and fill the areas
ax.fill(angles, wizard, color='blue', alpha=0.25, label='Wizard')
ax.plot(angles, wizard, color='blue', linewidth=2)

ax.fill(angles, warrior, color='red', alpha=0.25, label='Warrior')
ax.plot(angles, warrior, color='red', linewidth=2)

ax.fill(angles, rogue, color='green', alpha=0.25, label='Rogue')
ax.plot(angles, rogue, color='green', linewidth=2)

ax.fill(angles, paladin, color='purple', alpha=0.25, label='Paladin')
ax.plot(angles, paladin, color='purple', linewidth=2)

ax.fill(angles, druid, color='brown', alpha=0.25, label='Druid')
ax.plot(angles, druid, color='brown', linewidth=2)

# Set the labels for each category
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13)

# Title and legend
plt.title('Role-Playing Game Character Attributes', size=18, weight='bold', va='top')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Hide y-ticks and customize axis
ax.set_yticklabels([])
ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()