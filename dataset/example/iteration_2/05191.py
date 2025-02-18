import matplotlib.pyplot as plt
import numpy as np

# Define the categories for fantasy role-playing game character attributes
categories = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
n_vars = len(categories)

# Each character's attribute scores
wizard = [4, 6, 5, 9, 8, 6]
warrior = [9, 7, 8, 5, 4, 6]
rogue = [6, 9, 5, 7, 6, 7]

# Repeat the first value to close the radar chart loop
wizard += wizard[:1]
warrior += warrior[:1]
rogue += rogue[:1]

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

# Set the labels for each category
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13)

# Title and legend with clear positioning
plt.title('Role-Playing Game Character Attributes', size=18, weight='bold', va='top')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Customize radial axis and hide y-ticks
ax.set_yticklabels([])
ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)

# Improve layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()