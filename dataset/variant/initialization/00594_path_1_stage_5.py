import matplotlib.pyplot as plt
import numpy as np

skills = ['Magic', 'Charisma', 'Crafting', 'Archery', 'Stealth', 'Swordsmanship']
num_skills = len(skills)

knight_skills = [3, 8, 5, 4, 2, 9]
archer_skills = [4, 6, 5, 9, 8, 5]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

knight_skills += knight_skills[:1]
archer_skills += archer_skills[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f7f9f9')

# Fill the area within the radar chart for each character
ax.fill(angles, knight_skills, color='#1f77b4', alpha=0.5)
ax.plot(angles, knight_skills, color='#1f77b4', linewidth=1.5)

ax.fill(angles, archer_skills, color='#ff7f0e', alpha=0.5)
ax.plot(angles, archer_skills, color='#ff7f0e', linewidth=1.5)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12)

ax.set_title('Mystic Abilities in\n"Realm of Legends"', fontsize=15, fontweight='bold', pad=20)

plt.tight_layout()
plt.show()