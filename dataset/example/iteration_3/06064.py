import numpy as np
import matplotlib.pyplot as plt

# Backstory: 
# The chart compares the abilities of different superhero teams based on their strengths in various domains.

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

# Calculate the angle for each category on the radar chart
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop for the last angle

# Create a figure for the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Draw the radar chart with filled areas
for team, abilities in team_abilities.items():
    abilities += abilities[:1]  # Repeat the first value to close the radar chart loop
    ax.fill(angles, abilities, alpha=0.25, label=team)
    ax.plot(angles, abilities, linewidth=2, marker='o')

# Customize the chart's appearance
plt.xticks(angles[:-1], categories, color='navy', size=12)
ax.set_ylim(0, 100)
plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=10)

# Title and legend settings
plt.title('Superhero Team Comparison\nBased on Abilities', size=18, color='darkred', y=1.1, weight='bold')
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=11, title='Teams')

# Ensure everything is adjusted neatly
plt.tight_layout()

# Display the radar chart
plt.show()