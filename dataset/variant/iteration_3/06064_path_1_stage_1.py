import numpy as np
import matplotlib.pyplot as plt

# Define the attributes in which superheroes are evaluated
categories = ['Strength', 'Speed', 'Intelligence', 'Endurance', 'Agility', 'Healing']
num_vars = len(categories)

# Superhero team abilities: each team's strengths in the given attributes
team_abilities = {
    'Team Alpha': [85, 70, 95, 60, 75, 80],
    'Team Beta': [70, 60, 85, 80, 65, 90],
    'Team Gamma': [90, 85, 75, 70, 80, 60],
    'Team Delta': [95, 85, 70, 75, 90, 85]
}

angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the last angle

# Create a figure for the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Defining a new set of colors
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700']  # Tomato, SteelBlue, LimeGreen, Gold

# Draw the radar chart with filled areas using the new colors
for idx, (team, abilities) in enumerate(team_abilities.items()):
    abilities += abilities[:1]  # Repeat the first value to close the radar chart loop
    ax.fill(angles, abilities, color=colors[idx], alpha=0.25, label=team)
    ax.plot(angles, abilities, color=colors[idx], linewidth=2, marker='o')

plt.xticks(angles[:-1], categories, color='navy', size=12)
ax.set_ylim(0, 100)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=10)

plt.title('Superhero Team Comparison\nBased on Abilities', size=18, color='darkred', y=1.1, weight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11, title='Teams')

plt.tight_layout()
plt.show()