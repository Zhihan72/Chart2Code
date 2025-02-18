import matplotlib.pyplot as plt
import numpy as np

# Shuffling creatures and re-labeling for randomness
creatures = ['Orc', 'Dragon', 'Wizard', 'Elf'] 
attributes = ['Stealth', 'Magic Power', 'Agility', 'Intelligence', 'Strength']

# Updating data according to shuffled creatures
data = {
    'Orc': [10, 5, 7, 3, 6],
    'Dragon': [9, 7, 6, 10, 5],
    'Wizard': [4, 10, 5, 9, 7],
    'Elf': [5, 8, 9, 6, 8]
}

num_vars = len(attributes)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

def radar_chart(ax, values, creature_name, color):
    values += values[:1]
    ax.fill(angles, values, color=color, alpha=0.5)

    ax.set_xticks(angles[:-1])

    # Changed attribute labels and creature name
    ax.set_xticklabels(attributes, color='grey', fontsize=12)
    ax.set_yticklabels([])  
    ax.set_title(creature_name, size=15, color=color, pad=20)

# New colors kept the same, for simplified visual integrity
colors = ['#B22222', '#228B22', '#FF1493', '#FFD700']

fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 10), subplot_kw=dict(polar=True))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for ax, (creature, color) in zip(axs.flat, zip(creatures, colors)):
    radar_chart(ax, data[creature], creature, color)

# Altered the title for a random theme
plt.suptitle("Mythical Beings' Diverse Skill Overview", 
             fontsize=18, fontweight='bold', color='darkslateblue')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()