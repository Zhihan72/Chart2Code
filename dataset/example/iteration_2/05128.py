import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories and data for each team
skills = ['Leadership', 'Technical Expertise', 'Physical Fitness', 'Medical Knowledge', 'Problem Solving']
num_skills = len(skills)

# Skill scores for each team
teams_scores = {
    'Alpha Centauri': [8, 7, 9, 6, 8],
    'Galactic Voyagers': [7, 9, 6, 8, 7],
    'Solar Pioneers': [9, 6, 8, 7, 9],
    'Lunar Legends': [6, 8, 7, 9, 6],
}

# Create the radar chart
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Create angles for each category
angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1] # Close the circle

# Plot each team's data
colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8']
for idx, (team, scores) in enumerate(teams_scores.items()):
    scores += scores[:1]  # Close the loop
    ax.plot(angles, scores, label=team, linewidth=2, linestyle='solid', color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

# Add labels and title
plt.xticks(angles[:-1], skills, color='black', size=12)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

# Adding annotations
ax.set_title('Space Expedition Team Skill Analysis\nComparison for Upcoming Mars Mission', 
              size=16, color='navy', weight='bold', pad=20, va='bottom')

# Adding a legend and layout adjustment
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Teams")

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the radar chart
plt.show()