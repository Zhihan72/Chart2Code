import matplotlib.pyplot as plt
import numpy as np

categories = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
n_vars = len(categories)

wizard = [4, 6, 5, 9, 8, 6]
warrior = [9, 7, 8, 5, 4, 6]
rogue = [6, 9, 5, 7, 6, 7]
paladin = [8, 5, 9, 6, 7, 5]
druid = [5, 6, 7, 8, 9, 6]

wizard += wizard[:1]
warrior += warrior[:1]
rogue += rogue[:1]
paladin += paladin[:1]
druid += druid[:1]

angles = np.linspace(0, 2 * np.pi, n_vars, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))

ax.plot(angles, wizard, color='orange', linewidth=2)
ax.plot(angles, warrior, color='lime', linewidth=2)
ax.plot(angles, rogue, color='cyan', linewidth=2)
ax.plot(angles, paladin, color='magenta', linewidth=2)
ax.plot(angles, druid, color='gold', linewidth=2)

ax.set_xticks(angles[:-1])
ax.set_xticklabels([])  # Removed labels
ax.set_yticklabels([])  # Removed y-tick labels
ax.set_rlabel_position(0)

ax.spines['polar'].set_visible(False)

plt.tight_layout()
plt.show()