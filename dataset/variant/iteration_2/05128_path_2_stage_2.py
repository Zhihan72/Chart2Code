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

# New set of colors
colors = ['#7393B3', '#B3A739', '#93B373', '#B37393']
for idx, (team, scores) in enumerate(teams_scores.items()):
    scores += scores[:1]
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