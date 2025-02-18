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

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

ax.fill(angles, knight_skills, color='tab:red', alpha=0.25)
ax.plot(angles, knight_skills, color='tab:red', linewidth=1.5)

ax.fill(angles, archer_skills, color='tab:green', alpha=0.25)
ax.plot(angles, archer_skills, color='tab:green', linewidth=1.5)

ax.fill(angles, mage_skills, color='tab:blue', alpha=0.25)
ax.plot(angles, mage_skills, color='tab:blue', linewidth=1.5)

ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12)

plt.show()