import matplotlib.pyplot as plt
import numpy as np

skills = ['Swordsmanship', 'Archery', 'Magic', 'Stealth', 'Crafting', 'Charisma']
num_skills = len(skills)

knight_skills = [9, 4, 3, 2, 5, 8]
archer_skills = [5, 9, 4, 8, 5, 6]
mage_skills = [2, 3, 10, 4, 7, 5]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
knight_skills += knight_skills[:1]
archer_skills += archer_skills[:1]
mage_skills += mage_skills[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#ffffff')

ax.grid(color='black', linestyle='-', linewidth=1)

ax.fill(angles, knight_skills, color='tab:red', alpha=0.3)
ax.plot(angles, knight_skills, color='tab:red', linewidth=1, linestyle='solid', marker='o', label='Knight')

ax.fill(angles, archer_skills, color='tab:green', alpha=0.3)
ax.plot(angles, archer_skills, color='tab:green', linewidth=1, linestyle='solid', marker='s', label='Archer')

ax.fill(angles, mage_skills, color='tab:blue', alpha=0.3)
ax.plot(angles, mage_skills, color='tab:blue', linewidth=1, linestyle='solid', marker='^', label='Mage')

ax.set_yticklabels(['Low', '', '', 'Medium', '', '', 'High'], fontsize=10, color='black')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='darkred')

ax.annotate('Top Magic', xy=(angles[2], mage_skills[2]), xytext=(angles[2], mage_skills[2] + 2),
            arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=11, color='purple')

ax.set_title('Character Skills in Mythoria', fontsize=16, fontweight='bold', color='darkblue', pad=20)
ax.legend(loc='lower left', bbox_to_anchor=(-0.2, 0.2), frameon=True, fontsize=12)

plt.tight_layout()
plt.show()