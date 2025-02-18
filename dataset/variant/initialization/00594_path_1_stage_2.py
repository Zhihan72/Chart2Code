import matplotlib.pyplot as plt
import numpy as np

skills = ['Magic', 'Charisma', 'Crafting', 'Archery', 'Stealth', 'Swordsmanship']  # Shuffled skills
num_skills = len(skills)

knight_skills = [3, 8, 5, 4, 2, 9]  # Matching shuffled skills
archer_skills = [4, 6, 5, 9, 8, 5]  # Matching shuffled skills

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()

knight_skills += knight_skills[:1]
archer_skills += archer_skills[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#f7f9f9')

ax.fill(angles, knight_skills, color='tab:red', alpha=0.25, label='Guardian')  # Changed label
ax.plot(angles, knight_skills, color='tab:red', linewidth=1.5)

ax.fill(angles, archer_skills, color='tab:green', alpha=0.25, label='Ranger')  # Changed label
ax.plot(angles, archer_skills, color='tab:green', linewidth=1.5)

ax.set_yticklabels([])  
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12)

ax.set_title('Mystic Abilities in\n"Realm of Legends"', fontsize=15, fontweight='bold', pad=20)  # Changed title
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.tight_layout()
plt.show()