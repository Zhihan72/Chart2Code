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

# Using different colors and line styles
colors = ['#FF6347', '#4682B4', '#32CD32']
markers = ['o', '^', 's']  # Circle, Triangle, Square
line_styles = ['-', '--', '-.']

ax.fill(angles, mage, color=colors[0], alpha=0.3, label='Mage')
ax.plot(angles, mage, color=colors[0], linewidth=2, linestyle=line_styles[0], marker=markers[0])

ax.fill(angles, knight, color=colors[1], alpha=0.3, label='Knight')
ax.plot(angles, knight, color=colors[1], linewidth=2, linestyle=line_styles[1], marker=markers[1])

ax.fill(angles, thief, color=colors[2], alpha=0.3, label='Thief')
ax.plot(angles, thief, color=colors[2], linewidth=2, linestyle=line_styles[2], marker=markers[2])

# Set grid and border
ax.grid(True)  # Enable grid
ax.spines['polar'].set_linestyle('dotted')  # Change border to dotted

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=13)

plt.title('Fantasy Game Character Skills', size=18, weight='bold')
ax.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.1))  # Move legend

ax.set_yticklabels([])
ax.set_rlabel_position(0)

plt.tight_layout()
plt.show()