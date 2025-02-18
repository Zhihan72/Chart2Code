import numpy as np
import matplotlib.pyplot as plt
from math import pi

categories = ['Storytelling', 'Musicianship', 'Herbal Knowledge', 'Combat Skills', 'Mysticism', 'Charm', 'Alchemy']

bard_1 = np.array([8, 7, 7, 6, 6, 8, 5])
bard_2 = np.array([6, 9, 8, 6, 8, 5, 7])
bard_3 = np.array([7, 6, 6, 8, 9, 8, 5])

bards_data = [bard_1, bard_2, bard_3]
bards_names = ['Lyrical Linden', 'Melodic Melody', 'Harmonious Harper']

num_vars = len(categories)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

colors = ['#32CD32', '#FF6347', '#4682B4']

def create_radar_chart(ax, data, categories, color):
    for bard_data, color in zip(data, color):
        values = np.concatenate((bard_data, [bard_data[0]]))
        ax.plot(angles, values, linewidth=2, linestyle='solid', color=color)
        ax.fill(angles, values, color=color, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, color='black', size=10)
    ax.set_ylim(0, 10)

fig, ax1 = plt.subplots(1, 1, figsize=(6, 6), subplot_kw=dict(polar=True))

create_radar_chart(ax1, bards_data, categories, colors)
ax1.set_title('Legendary Bards: Skills and Talents', size=14, color='darkblue', y=1.1, fontweight='bold')

plt.tight_layout()
plt.show()