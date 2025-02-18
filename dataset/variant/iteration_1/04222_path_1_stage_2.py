import matplotlib.pyplot as plt
import numpy as np

creatures = ['Dragon', 'Elf', 'Orc', 'Wizard']
attributes = ['Strength', 'Intelligence', 'Agility', 'Magic Power', 'Stealth']

data = {
    'Dragon': [9, 7, 6, 10, 5],
    'Elf': [5, 8, 9, 6, 8],
    'Orc': [10, 5, 7, 3, 6],
    'Wizard': [4, 10, 5, 9, 7]
}

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def radar_chart(ax, values, creature_name, color):
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, color='grey', fontsize=12)
    ax.set_yticklabels([])

    ax.set_title(creature_name, size=15, color=color, pad=20)

# New set of colors
colors = ['#B22222', '#228B22', '#FF1493', '#FFD700']

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for ax, (creature, color) in zip(axs.flat, zip(creatures, colors)):
    radar_chart(ax, data[creature], creature, color)

plt.suptitle("Fantasy Creatures' Competency Assessment Across Various Attributes", 
             fontsize=18, fontweight='bold', color='darkslateblue')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()