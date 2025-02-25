import numpy as np
import matplotlib.pyplot as plt
from math import pi

skills = ['Leadership', 'Technical Expertise', 'Physical Fitness', 'Medical Knowledge', 'Problem Solving']
num_skills = len(skills)

teams_scores = {
    'Alpha Centauri': [7, 8, 9, 6, 8],
    'Galactic Voyagers': [7, 9, 6, 7, 8],
    'Solar Pioneers': [9, 7, 8, 6, 9],
    'Lunar Legends': [6, 6, 8, 9, 7],
}

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]
colors = ['#8B0000', '#006400', '#8A2BE2', '#FF8C00']

for idx, (team, scores) in enumerate(teams_scores.items()):
    scores += scores[:1]
    # Remove the plot() function call to get rid of chart lines
    ax.fill(angles, scores, alpha=0.3, color=colors[idx], label=team)

plt.xticks(angles[:-1], skills, color='navy', size=10)
ax.set_rlabel_position(40)
plt.yticks([2, 5, 8], ["2", "5", "8"], color="darkgrey", size=9)
plt.ylim(0, 10)

ax.set_title('Mars Mission Team Skill Comparison', 
              size=18, color='darkred', weight='bold', pad=25, va='bottom')

plt.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1), title="Teams", fontsize=9)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()