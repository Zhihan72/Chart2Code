import matplotlib.pyplot as plt
import numpy as np

categories = ['Communication', 'Energy', 'Transportation', 'Health', 'Education']
num_vars = len(categories)

nova_terra = [8, 9, 7, 8, 7]
zynorra = [6, 7, 6, 8, 9]
kaleron = [9, 6, 8, 7, 8]
pyrros = [7, 8, 9, 6, 6]
elumir = [7, 7, 8, 7, 7]
thulani = [6, 8, 7, 9, 8]

average_scores = [
    np.mean([nova_terra[i], zynorra[i], kaleron[i], pyrros[i], elumir[i], thulani[i]]) 
    for i in range(num_vars)
]

def create_radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    
    ax.fill(angles, data, color=color, alpha=0.3)
    ax.plot(angles, data, color=color, linestyle='--', linewidth=2, label=label, marker='o')

fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={'projection': 'polar'})

axs[0].set_title('Radar Chart: Technological Infrastructure\nAssessment of Planets', fontsize=12, fontweight='bold')
create_radar_chart(axs[0], nova_terra, '#1f77b4', 'Nova Terra')
create_radar_chart(axs[0], zynorra, '#ff7f0e', 'Zynorra')
create_radar_chart(axs[0], kaleron, '#2ca02c', 'Kaleron')
create_radar_chart(axs[0], pyrros, '#d62728', 'Pyrros')
create_radar_chart(axs[0], elumir, '#9467bd', 'Elumir')
create_radar_chart(axs[0], thulani, '#8c564b', 'Thulani')
axs[0].set_yticklabels([])
axs[0].set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
axs[0].set_xticklabels(categories, fontsize=10)
axs[0].grid(True, linestyle='-', linewidth=0.6)
axs[0].legend(loc='upper left', bbox_to_anchor=(-0.1, 1.2), frameon=False)

axs[1] = fig.add_subplot(1, 2, 2)
axs[1].barh(categories, average_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
axs[1].set_xlim(0, 10)
axs[1].set_title('Average Scores Across Categories', fontsize=12, fontweight='bold')
axs[1].set_xlabel('Average Score')
axs[1].invert_yaxis()
for i, score in enumerate(average_scores):
    axs[1].text(score + 0.2, i, f'{score:.1f}', va='center', color='black', fontweight='bold')

plt.tight_layout()
plt.show()