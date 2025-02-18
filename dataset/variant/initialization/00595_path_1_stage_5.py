import matplotlib.pyplot as plt
import numpy as np

skills = ['Sword', 'Arch', 'Magic', 'Stealth', 'Craft', 'Charisma']
num_skills = len(skills)

knight_skills = [9, 4, 3, 2, 5, 8]
mage_skills = [2, 3, 10, 4, 7, 5]

angles = np.linspace(0, 2 * np.pi, num_skills, endpoint=False).tolist()
knight_skills += knight_skills[:1]
mage_skills += mage_skills[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.plot(angles, knight_skills, color='tab:red', linewidth=2, label='Knight')
ax.plot(angles, mage_skills, color='tab:blue', linewidth=2, label='Mage')

ax.fill(angles, knight_skills, color='tab:red', alpha=0.0)
ax.fill(angles, mage_skills, color='tab:blue', alpha=0.0)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(skills, fontsize=12, color='black')

ax.legend()
plt.show()