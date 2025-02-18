import matplotlib.pyplot as plt
import numpy as np

attributes = ['Bravery', 'Strength', 'Wisdom', 'Dexterity', 'Honor']
n_attributes = len(attributes)

lancelot = [10, 9, 9, 8, 7]
gawain = [9, 10, 7, 8, 7]
percival = [8, 8, 9, 10, 7]

lancelot += lancelot[:1]
gawain += gawain[:1]
percival += percival[:1]

angles = np.linspace(0, 2 * np.pi, n_attributes, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
plt.xticks(angles[:-1], attributes, fontsize=12, fontweight='bold')

# New set of colors to replace the original ones
new_colors = ['#e41a1c', '#377eb8', '#4daf4a']

knight_names = ['Sir Lancelot', 'Sir Gawain', 'Sir Percival']
knight_data = [lancelot, gawain, percival]

for idx, knight in enumerate(knight_data):
    ax.plot(angles, knight, color=new_colors[idx], linewidth=2, linestyle='solid', label=knight_names[idx])
    ax.fill(angles, knight, color=new_colors[idx], alpha=0.25)

ax.set_yticklabels([])

plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1), title='Legendary Knights')
plt.title('Attributes of Legendary Knights in Astoria', size=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()