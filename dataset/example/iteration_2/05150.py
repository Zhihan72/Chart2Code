import numpy as np
import matplotlib.pyplot as plt

# Backstory: In the world of mysticism, various arcane disciplines offer unique abilities.
# The chart compares these abilities across different magic disciplines.

# Define magical abilities and their ratings for each discipline
abilities = ['Spell Power', 'Mana Efficiency', 'Versatility', 'Ritual Complexity', 'Defense', 'Mobility']
num_vars = len(abilities)

# Ratings for each discipline
arcane_discs_data = {
    'Elemental Magic': [8, 7, 6, 5, 8, 7],
    'Necromancy': [6, 5, 7, 8, 8, 4],
    'Divination': [7, 8, 5, 3, 6, 5],
    'Enchantments': [8, 6, 9, 7, 5, 6],
    'Illusions': [6, 7, 7, 4, 6, 9]
}

# Calculate the angle for each ability
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the last angle

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Plot each discipline, fill the area, and add labels
for discipline, ratings in arcane_discs_data.items():
    ratings += ratings[:1]  # Repeat the first value to close the radar chart loop
    ax.fill(angles, ratings, alpha=0.25, label=discipline)
    ax.plot(angles, ratings, linewidth=2)

# Customize the appearance
plt.xticks(angles[:-1], abilities, color='slategray', size=12)
ax.set_ylim(0, 10)
plt.yticks(range(1, 10), map(str, range(1, 10)), color="slategray", size=10)

# Title and legend settings
plt.title('Comparative Analysis of Arcane Disciplines', size=18, color='indigo', pad=20)
ax.legend(loc='best', bbox_to_anchor=(0.1, 0.1), fontsize=12, title='Magic Disciplines')

# Adjust layout to ensure everything is neatly positioned
plt.tight_layout()

# Display the radar chart
plt.show()