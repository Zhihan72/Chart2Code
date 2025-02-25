import matplotlib.pyplot as plt
import numpy as np

# Define the categories for fantasy role-playing game character attributes
categories = ['Bravery', 'Agility', 'Stamina', 'Knowledge', 'Insight', 'Charm']
n_vars = len(categories)

# Each character's attribute scores
mage = [4, 6, 5, 9, 8, 6]
knight = [9, 7, 8, 5, 4, 6]
thief = [6, 9, 5, 7, 6, 7]

# Repeat the first value to close the radar chart loop
mage += mage[:1]
knight += knight[:1]
thief += thief[:1]

# Calculate angles for each category (including closure)
angles = np.linspace(0, 2 * np.pi, n_vars, endpoint=False).tolist()
angles += angles[:1]

# Initialize the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each character and fill the areas
ax.fill(angles, mage, color='blue', alpha=0.25, label='Mage')
ax.plot(angles, mage, color='blue', linewidth=2)

ax.fill(angles, knight, color='red', alpha=0.25, label='Knight')
ax.plot(angles, knight, color='red', linewidth=2)

ax.fill(angles, thief, color='green', alpha=0.25, label='Thief')
ax.plot(angles, thief, color='green', linewidth=2)

# Set the labels for each category
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13)

# Title and legend
plt.title('Fantasy Game Character Skills', size=18, weight='bold', va='top')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

# Customize radial axis and hide y-ticks
ax.set_yticklabels([])
ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)

# Improve layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()