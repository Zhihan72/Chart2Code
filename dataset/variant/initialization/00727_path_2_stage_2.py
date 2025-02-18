import matplotlib.pyplot as plt
import numpy as np

categories = ['Communication', 'Energy', 'Transportation', 'Health', 'Education']
num_vars = len(categories)

nova_terra = [8, 9, 7, 8, 7]
zynorra = [6, 7, 6, 8, 9]
kaleron = [9, 6, 8, 7, 8]
pyrros = [7, 8, 9, 6, 6]
vextrax = [7, 9, 8, 7, 6]  # New data series

average_scores = [
    np.mean([nova_terra[i], zynorra[i], kaleron[i], pyrros[i], vextrax[i]]) 
    for i in range(num_vars)
]

def create_radar_chart(ax, data, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=False))

polar_ax = fig.add_subplot(121, polar=True)
create_radar_chart(polar_ax, nova_terra, 'b')
create_radar_chart(polar_ax, zynorra, 'r')
create_radar_chart(polar_ax, kaleron, 'g')
create_radar_chart(polar_ax, pyrros, 'orange')
create_radar_chart(polar_ax, vextrax, 'purple')  # Add new series to the radar chart
polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=10)

ax2.bar(categories, average_scores, color=['b', 'r', 'g', 'orange', 'purple'])
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Score')
ax2.set_xlabel('Category')
for i, score in enumerate(average_scores):
    ax2.text(i, score + 0.2, f'{score:.1f}', ha='center', color='black', fontweight='bold')

plt.tight_layout()
plt.show()