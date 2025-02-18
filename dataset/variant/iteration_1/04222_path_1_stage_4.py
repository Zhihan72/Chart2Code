import matplotlib.pyplot as plt
import numpy as np

creatures = ['Elf', 'Wizard', 'Dragon', 'Orc']
attributes = ['Magic Power', 'Intelligence', 'Agility', 'Strength', 'Stealth']

data = {
    'Elf': [5, 8, 9, 6, 8],
    'Wizard': [4, 10, 5, 9, 7],
    'Dragon': [9, 7, 6, 10, 5],
    'Orc': [10, 5, 7, 3, 6]
}

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def radar_chart(ax, values, creature_name, color):
    values += values[:1]
    ax.plot(angles, values, color=color, linestyle='--', marker='o')
    ax.fill(angles, values, color=color, alpha=0.25, linewidth=2.5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, color='grey', fontsize=10)
    ax.set_yticklabels([])  
    ax.set_title(creature_name, size=12, color=color, pad=15)

colors = ['#FF1493', '#228B22', '#B22222', '#FFD700']

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(9, 9), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.35, wspace=0.35)

for ax, (creature, color) in zip(axs.flat, zip(creatures, colors)):
    radar_chart(ax, data[creature], creature, color)
    ax.grid(linewidth=0.75, linestyle=':', color='grey')

plt.suptitle("Fantastical Creatures' Skill Overview", 
             fontsize=13, fontweight='bold', color='darkslateblue')

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plt.show()