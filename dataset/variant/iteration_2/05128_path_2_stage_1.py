import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define categories and data for each team
skills = ['Leadership', 'Technical Expertise', 'Physical Fitness', 'Medical Knowledge', 'Problem Solving']
num_skills = len(skills)

# Skill scores for each team
teams_scores = {
    'Alpha Centauri': [7, 8, 9, 6, 8],  # Altered 'Leadership' and 'Technical Expertise'
    'Galactic Voyagers': [7, 9, 6, 7, 8],  # Altered 'Problem Solving' and others
    'Solar Pioneers': [9, 7, 8, 6, 9],  # Altered 'Technical Expertise' and 'Medical Knowledge'
    'Lunar Legends': [6, 6, 8, 9, 7],  # Altered 'Technical Expertise' and 'Problem Solving'
}

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8']
for idx, (team, scores) in enumerate(teams_scores.items()):
    scores += scores[:1]  # Close the loop
    ax.plot(angles, scores, label=team, linewidth=2, linestyle='solid', color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

plt.xticks(angles[:-1], skills, color='black', size=12)
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=10)
plt.ylim(0, 10)

ax.set_title('Space Expedition Team Skill Analysis\nComparison for Upcoming Mars Mission', 
              size=16, color='navy', weight='bold', pad=20, va='bottom')

plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Teams")
plt.tight_layout()

plt.show()