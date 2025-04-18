import matplotlib.pyplot as plt
import numpy as np

categories = ['Communication', 'Energy', 'Transportation', 'Health', 'Education']
num_vars = len(categories)

nova_terra = [8, 9, 7, 8, 7]
zynorra = [6, 7, 6, 8, 9]
kaleron = [9, 6, 8, 7, 8]
pyrros = [7, 8, 9, 6, 6]
vextrax = [7, 9, 8, 7, 6]

average_scores = [
    np.mean([nova_terra[i], zynorra[i], kaleron[i], pyrros[i], vextrax[i]]) 
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

create_fill_area_radar(polar_ax, nova_terra, '#FF7F50')  # Coral
create_fill_area_radar(polar_ax, zynorra, '#4682B4')  # SteelBlue
create_fill_area_radar(polar_ax, kaleron, '#2E8B57')  # SeaGreen
create_fill_area_radar(polar_ax, pyrros, '#DA70D6')   # Orchid
create_fill_area_radar(polar_ax, vextrax, '#FFD700')  # Gold

polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=10)

ax2.bar(categories, average_scores, color=['#FF7F50', '#4682B4', '#2E8B57', '#DA70D6', '#FFD700'])
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Score')
ax2.set_xlabel('Category')
for i, score in enumerate(average_scores):
    ax2.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

plt.tight_layout()
plt.show()