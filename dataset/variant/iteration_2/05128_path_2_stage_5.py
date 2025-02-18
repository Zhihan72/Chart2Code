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
    ax.fill(angles, scores, alpha=0.3, color=colors[idx])

plt.xticks(angles[:-1], [])
plt.yticks([])
plt.ylim(0, 10)

plt.grid(True, linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()