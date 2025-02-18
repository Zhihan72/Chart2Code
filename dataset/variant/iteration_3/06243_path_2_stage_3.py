import matplotlib.pyplot as plt
import numpy as np

skills = ['Piloting', 'Engineering', 'Science', 'Physical Fitness', 'Teamwork', 'Quick Decision Making']
num_skills = len(skills)

neptune_academy = [8, 7, 9, 6, 8, 7]
mars_academy = [7, 8, 6, 7, 9, 8]

neptune_academy += neptune_academy[:1]
mars_academy += mars_academy[:1]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

consistent_color = '#1f77b4'

ax.plot(angles, neptune_academy, linewidth=2, linestyle='-', color=consistent_color, marker='o')
ax.fill(angles, neptune_academy, consistent_color, alpha=0.15)

ax.plot(angles, mars_academy, linewidth=2, linestyle='-', color=consistent_color, marker='s')
ax.fill(angles, mars_academy, consistent_color, alpha=0.15)

ax.set_yticks([2, 4, 6, 8])
ax.set_ylim(0, 10)
ax.set_yticklabels([])

plt.tight_layout()
plt.show()