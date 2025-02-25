import numpy as np
import matplotlib.pyplot as plt
from math import pi

skills = ['Leadership', 'Technical Expertise', 'Physical Fitness', 'Medical Knowledge', 'Problem Solving']
num_skills = len(skills)

teams_scores = {
    'Alpha Centauri': [9, 6, 8, 7, 9],
    'Galactic Voyagers': [6, 8, 7, 9, 6],
    'Solar Pioneers': [8, 7, 9, 6, 8],
    'Lunar Legends': [7, 9, 6, 8, 7],
}

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#ff69b4']
markers = ['o-', 's--', '^-', 'd:']
for (team, scores), color, marker in zip(teams_scores.items(), colors, markers):
    scores += scores[:1]
    ax.plot(angles, scores, marker, label=team, color=color)
    ax.fill(angles, scores, alpha=0.3, color=color)

ax.set_yticklabels(['', '2', '4', '6', '8', '10'])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills)

ax.yaxis.grid(True, color='gray', linestyle=':', linewidth=0.5)
ax.spines['polar'].set_visible(False)

plt.ylim(0, 10)
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), frameon=False)

plt.tight_layout()

plt.show()