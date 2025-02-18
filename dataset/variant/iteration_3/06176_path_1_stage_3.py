import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Randomly altered skill categories
categories = ['Survival Skills', 'Navigation', 'Communication', 'Life Sciences', 'Engineering']
num_skills = len(categories)

# Skill levels for each team
# Randomly altered team labels
team_1 = [9, 8, 7, 6, 9]  # Previously apollo_astronauts
team_2 = [6, 9, 8, 5, 6]  # Previously mars_rover_engineers
team_3 = [5, 8, 9, 8, 5]  # Previously iss_scientists
team_4 = [8, 7, 5, 9, 8]  # Previously spacex_pilots

# Data preparation for radar chart
data = np.array([team_1, team_2, team_3, team_4])
data = np.concatenate((data, data[:, [0]]), axis=1)

# Calculate angles for each skill
angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

# Create radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Single color for all data groups
single_color = '#FF5733'

# Plot each team's skill levels with the same color
for i in range(len(data)):
    ax.fill(angles, data[i], color=single_color, alpha=0.25)
    ax.plot(angles, data[i], color=single_color, linewidth=2)

# Label skill categories with the altered order
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Altered the radar chart title
plt.title('Multi-team Capability Assessment', fontsize=15, fontweight='bold')

# Display the radar chart
plt.show()