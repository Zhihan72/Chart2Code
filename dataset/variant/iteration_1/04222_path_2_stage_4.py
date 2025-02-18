import matplotlib.pyplot as plt
import numpy as np

creatures = ['Wizard', 'Dragon', 'Elf', 'Orc']
attributes = ['Magic Power', 'Stealth', 'Intelligence', 'Agility', 'Strength']

data = {
    'Wizard': [4, 10, 5, 9, 7],
    'Dragon': [9, 7, 6, 10, 5],
    'Elf': [5, 8, 9, 6, 8],
    'Orc': [10, 5, 7, 3, 6]
}

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def radar_chart(ax, values, creature_name, color):
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.25)  # Fill area under lines
    ax.plot(angles, values, color=color, linewidth=2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(attributes, color='grey', fontsize=12)
    ax.set_yticklabels([])

    ax.set_title(creature_name, size=15, color=color, pad=20)

single_color = '#1E90FF'

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for ax, creature in zip(axs.flat, creatures):
    radar_chart(ax, data[creature], creature, single_color)
    ax.spines['polar'].set_visible(False)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()