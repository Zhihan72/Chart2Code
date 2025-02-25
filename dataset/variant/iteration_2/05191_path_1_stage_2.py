import matplotlib.pyplot as plt
import numpy as np

categories = ['Bravery', 'Agility', 'Stamina', 'Knowledge', 'Insight', 'Charm']
n_vars = len(categories)

mage = [4, 6, 5, 9, 8, 6]
knight = [9, 7, 8, 5, 4, 6]
thief = [6, 9, 5, 7, 6, 7]

mage += mage[:1]
knight += knight[:1]
thief += thief[:1]

angles = np.linspace(0, 2 * np.pi, n_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

# Use the same color for all characters
color = 'blue'

ax.fill(angles, mage, color=color, alpha=0.25, label='Mage')
ax.plot(angles, mage, color=color, linewidth=2)

ax.fill(angles, knight, color=color, alpha=0.25, label='Knight')
ax.plot(angles, knight, color=color, linewidth=2)

ax.fill(angles, thief, color=color, alpha=0.25, label='Thief')
ax.plot(angles, thief, color=color, linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13)

plt.title('Fantasy Game Character Skills', size=18, weight='bold', va='top')
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

ax.set_yticklabels([])
ax.set_rlabel_position(0)
ax.spines['polar'].set_visible(False)

plt.tight_layout()
plt.show()