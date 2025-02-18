import numpy as np
import matplotlib.pyplot as plt
from math import pi

skills = ['Leadership', 'Technical Expertise', 'Physical Fitness', 'Medical Knowledge', 'Problem Solving']
num_skills = len(skills)

teams_scores = {
    'Alpha Centauri': [8, 7, 9, 6, 8],
    'Galactic Voyagers': [7, 9, 6, 8, 7],
    'Solar Pioneers': [9, 6, 8, 7, 9],
    'Lunar Legends': [6, 8, 7, 9, 6],
}

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

colors = ['#ff5733', '#33ff57', '#3357ff', '#ff33a8']
for idx, (team, scores) in enumerate(teams_scores.items()):
    scores += scores[:1]
    ax.plot(angles, scores, linewidth=2, linestyle='solid', color=colors[idx])
    ax.fill(angles, scores, alpha=0.25, color=colors[idx])

ax.set_yticklabels([])  # Remove y-tick labels
ax.set_xticklabels([])  # Remove x-tick labels

plt.ylim(0, 10)

# Remove title
# Remove legend labels
plt.legend([])

plt.tight_layout()

plt.show()