import matplotlib.pyplot as plt
import numpy as np

attributes = ['Wisdom', 'Dexterity', 'Bravery', 'Honor', 'Strength']
n_attributes = len(attributes)

lancelot = [10, 9, 8, 7, 9]
gawain = [7, 8, 10, 9, 7]
percival = [8, 7, 9, 10, 8]

lancelot += lancelot[:1]
gawain += gawain[:1]
percival += percival[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold')

single_color = '#1f77b4'
knight_data = [lancelot, gawain, percival]

for knight in knight_data:
    ax.plot(angles, knight, color=single_color, linewidth=2, linestyle='solid')
    ax.fill(angles, knight, color=single_color, alpha=0.25)

ax.set_yticklabels([])

plt.show()