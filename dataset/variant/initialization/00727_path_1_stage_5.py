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

def create_radar_chart(ax, data, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    
    ax.fill(angles, data, color=color, alpha=0.3)
    ax.plot(angles, data, color=color, linestyle='--', linewidth=2, marker='o')

fig, axs = plt.subplots(1, 2, figsize=(16, 8), subplot_kw={'projection': 'polar'})

create_radar_chart(axs[0], nova_terra, '#1f77b4')
create_radar_chart(axs[0], zynorra, '#ff7f0e')
create_radar_chart(axs[0], kaleron, '#2ca02c')
create_radar_chart(axs[0], pyrros, '#d62728')
create_radar_chart(axs[0], elumir, '#9467bd')
create_radar_chart(axs[0], thulani, '#8c564b')
axs[0].set_yticklabels([])
axs[0].set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
axs[0].set_xticklabels([])  # Removed category labels
axs[0].grid(True, linestyle='-', linewidth=0.6)

axs[1] = fig.add_subplot(1, 2, 2)
axs[1].barh(categories, average_scores, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
axs[1].set_xlim(0, 10)
axs[1].invert_yaxis()
axs[1].set_yticklabels([])  # Removed category labels
axs[1].set_xticks([])  # Removed x-axis labels
for i, score in enumerate(average_scores):
    pass  # Removed textual annotations

plt.tight_layout()
plt.show()