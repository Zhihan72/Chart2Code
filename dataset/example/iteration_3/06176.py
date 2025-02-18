import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Backstory:
# This radar chart shows the distribution of various skills required for successful space missions.
# It compares the skill levels assessed in different teams specialized in Space Exploration.
# Teams: "Apollo Astronauts", "Mars Rover Engineers", "ISS Scientists", "SpaceX Pilots"
# Skills: "Navigation", "Engineering", "Life Sciences", "Communication", "Survival Skills"

# Define the skill categories and number of skills
categories = ['Navigation', 'Engineering', 'Life Sciences', 'Communication', 'Survival Skills']
num_skills = len(categories)

# Define skill levels for each team (scale of 1 to 10)
apollo_astronauts = [9, 8, 7, 6, 9]
mars_rover_engineers = [6, 9, 8, 5, 6]
iss_scientists = [5, 8, 9, 8, 5]
spacex_pilots = [8, 7, 5, 9, 8]

# Consolidate and extend data to close the radar chart
data = np.array([apollo_astronauts, mars_rover_engineers, iss_scientists, spacex_pilots])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate the angle for each skill category
angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define labels for the different teams
labels = ["Apollo Astronauts", "Mars Rover Engineers", "ISS Scientists", "SpaceX Pilots"]

# Define colors for each team
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Plot each team's skill levels
for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.25, label=labels[i])
    ax.plot(angles, data[i], color=color, linewidth=2)

# Add skill category labels to the radar chart
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Customize the radial grid
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.xaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')
ax.set_ylim(0, 10)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10, color='grey')

# Set title and legend
ax.set_title('Skill Levels of Teams in Space Exploration Missions\nComparison Across Various Specializations', 
             fontsize=16, fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the radar chart
plt.show()