import matplotlib.pyplot as plt
import numpy as np

skills = ['Quick Decision Making', 'Physical Fitness', 'Science', 'Engineering', 'Teamwork', 'Piloting']
num_skills = len(skills)

neptune_academy = [8, 6, 9, 7, 8, 7]
jupiter_academy = [9, 8, 8, 9, 7, 6]

neptune_academy += neptune_academy[:1]
jupiter_academy += jupiter_academy[:1]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.fill(angles, neptune_academy, '#1f77b4', alpha=0.25)
ax.fill(angles, jupiter_academy, '#2ca02c', alpha=0.25)

plt.xticks(angles[:-1], skills, color='darkslategray', size=13, weight='bold')
ax.set_yticks([2, 4, 6, 8])
ax.set_ylim(0, 10)
ax.set_yticklabels(["2", "4", "6", "8"], color='gray', size=10)

plt.tight_layout()
plt.show()