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

ax.fill(angles, neptune_academy, '#1f77b4', alpha=0.3, label='Neptune Academy')
ax.fill(angles, mars_academy, '#ff7f0e', alpha=0.3, label='Mars Academy')

ax.set_yticks([2, 4, 6, 8])
ax.set_ylim(0, 10)
ax.set_yticklabels([])

ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.show()