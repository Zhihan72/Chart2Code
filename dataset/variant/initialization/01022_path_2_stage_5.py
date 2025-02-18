import matplotlib.pyplot as plt
import numpy as np

attributes = ['Brv', 'Str', 'Wis', 'Dex', 'Hon']
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

colors = ['#ff7f00', '#f781bf', '#984ea3']
markers = ['o', 's', '^']
line_styles = ['-', '--', '-.']
knight_names = ['Lancelot', 'Gawain', 'Percival']
knight_data = [lancelot, gawain, percival]

for idx, knight in enumerate(knight_data):
    ax.fill(angles, knight, color=colors[idx], alpha=0.25, label=knight_names[idx])
    ax.plot(angles, knight, color=colors[idx], linewidth=2.5, linestyle=line_styles[idx], marker=markers[idx])

ax.set_yticklabels([])
ax.grid(linewidth=1.5, linestyle=':')

plt.legend(loc='best', title='Knights')
plt.title('Knight Attributes', size=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()