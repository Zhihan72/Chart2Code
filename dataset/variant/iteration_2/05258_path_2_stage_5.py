import numpy as np
import matplotlib.pyplot as plt

categories = ['Story', 'Music', 'Herbs', 'Combat', 'Magic', 'Charm', 'Alchemy']

bard_1 = np.array([8, 7, 7, 6, 6, 8, 5])
bard_2 = np.array([6, 9, 8, 6, 8, 5, 7])
bard_3 = np.array([7, 6, 6, 8, 9, 8, 5])

bards_data = [bard_1, bard_2, bard_3]
bards_names = ['Linden', 'Melody', 'Harper']

colors = ['#32CD32', '#FF6347', '#4682B4']

fig, axs = plt.subplots(3, 1, figsize=(8, 10))

for ax, bard_data, bard_name, color in zip(axs, bards_data, bards_names, colors):
    ax.barh(categories, bard_data, color=color, edgecolor='black')
    ax.set_xlim(0, 10)
    ax.set_title(bard_name, fontsize=12, fontweight='bold', color='darkblue')
    ax.set_xlabel('Skill', fontsize=10)
    ax.set_yticks(np.arange(len(categories)))
    ax.set_yticklabels(categories, fontsize=10)

fig.suptitle('Bards: Skills', size=14, color='darkblue', y=0.95, fontweight='bold')
plt.tight_layout()
plt.show()