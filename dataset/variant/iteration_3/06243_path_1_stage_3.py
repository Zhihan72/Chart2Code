import matplotlib.pyplot as plt
import numpy as np

skills = ['Quick Decision Making', 'Physical Fitness', 'Science', 'Engineering', 'Teamwork', 'Piloting']
num_skills = len(skills)

neptune_academy = [8, 6, 9, 7, 8, 7]
mars_academy = [8, 7, 6, 8, 9, 7]
jupiter_academy = [9, 8, 8, 9, 7, 6]

neptune_academy += neptune_academy[:1]
mars_academy += mars_academy[:1]
jupiter_academy += jupiter_academy[:1]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.fill(angles, neptune_academy, '#1f77b4', alpha=0.25, label='Neptune Institute')
ax.fill(angles, mars_academy, '#ff7f0e', alpha=0.25, label='Mars Institute')
ax.fill(angles, jupiter_academy, '#2ca02c', alpha=0.25, label='Jupiter Institute')

plt.title("Metrics in Galactic Training Centers", size=18, color='navy', pad=20)
plt.xticks(angles[:-1], skills, color='darkslategray', size=13, weight='bold')
ax.set_yticks([2, 4, 6, 8])
ax.set_ylim(0, 10)
ax.set_yticklabels(["2", "4", "6", "8"], color='gray', size=10)

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=12)
ax.spines['polar'].set_visible(False)
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, color='grey')

plt.tight_layout()
plt.show()