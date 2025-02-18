import matplotlib.pyplot as plt
import numpy as np

# Randomly altered categories and entity names
categories = ['Commune', 'Vitality', 'Transit', 'Wellbeing', 'Learning']
num_vars = len(categories)

aestra = [8, 9, 7, 8, 7]
belmara = [6, 7, 6, 8, 9]
calixen = [9, 6, 8, 7, 8]
dorvexa = [7, 8, 9, 6, 6]
elantor = [7, 9, 8, 7, 6]

average_scores = [
    np.mean([aestra[i], belmara[i], calixen[i], dorvexa[i], elantor[i]]) 
    for i in range(num_vars)
]

def create_fill_area_radar(ax, data, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

polar_ax = fig.add_subplot(121, polar=True)

create_fill_area_radar(polar_ax, aestra, '#FF7F50')  # Coral
create_fill_area_radar(polar_ax, belmara, '#4682B4')  # SteelBlue
create_fill_area_radar(polar_ax, calixen, '#2E8B57')  # SeaGreen
create_fill_area_radar(polar_ax, dorvexa, '#DA70D6')  # Orchid
create_fill_area_radar(polar_ax, elantor, '#FFD700')  # Gold

polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=10)

# Adjusted axis labels and group identifiers
ax2.bar(categories, average_scores, color=['#FF7F50', '#4682B4', '#2E8B57', '#DA70D6', '#FFD700'])
ax2.set_ylim(0, 10)
ax2.set_ylabel('Mean Score')
ax2.set_xlabel('Sector')
for i, score in enumerate(average_scores):
    ax2.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

plt.tight_layout()
plt.show()