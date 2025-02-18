import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Skill categories
categories = ['Navigation', 'Engineering', 'Life Sciences', 'Communication', 'Survival Skills']
num_skills = len(categories)

# Skill levels for each team
apollo_astronauts = [9, 8, 7, 6, 9]
mars_rover_engineers = [6, 9, 8, 5, 6]
iss_scientists = [5, 8, 9, 8, 5]
spacex_pilots = [8, 7, 5, 9, 8]

# Data preparation for radar chart
data = np.array([apollo_astronauts, mars_rover_engineers, iss_scientists, spacex_pilots])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate angles for each skill
angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Define colors
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A1']

# Plot each team's skill levels
for i, color in enumerate(colors):
    ax.fill(angles, data[i], color=color, alpha=0.25)
    ax.plot(angles, data[i], color=color, linewidth=2)

# Label skill categories
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Display the radar chart
plt.show()