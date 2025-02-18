import numpy as np
import matplotlib.pyplot as plt
from math import pi

skills = ['Leadership', 'Technical Expertise', 'Physical Fitness', 'Medical Knowledge', 'Problem Solving']
num_skills = len(skills)

# Randomly altered the scores for different teams while preserving the structure
teams_scores = {
    'Alpha Centauri': [9, 6, 8, 7, 9],  # altered
    'Galactic Voyagers': [6, 8, 7, 9, 6],  # altered
    'Solar Pioneers': [8, 7, 9, 6, 8],  # altered
    'Lunar Legends': [7, 9, 6, 8, 7],  # altered
}

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

single_color = '#33ff57'
for team, scores in teams_scores.items():
    scores += scores[:1]
    ax.fill(angles, scores, alpha=0.5, color=single_color)

ax.set_yticklabels([])
ax.set_xticklabels([])

plt.ylim(0, 10)

plt.tight_layout()

plt.show()