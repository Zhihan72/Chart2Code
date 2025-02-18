import matplotlib.pyplot as plt
import numpy as np

# Define the categories and data for each planet
categories = ['Communication', 'Energy', 'Transportation', 'Health', 'Education']
num_vars = len(categories)

nova_terra = [8, 9, 7, 8, 7]
zynorra = [6, 7, 6, 8, 9]
kaleron = [9, 6, 8, 7, 8]
pyrros = [7, 8, 9, 6, 6]

average_scores = [
    np.mean([nova_terra[i], zynorra[i], kaleron[i], pyrros[i]]) 
    for i in range(num_vars)
]

def create_radar_chart(ax, data, color, label):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.3)
    ax.plot(angles, data, color=color, linestyle='--', linewidth=2, label=label, marker='o')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), subplot_kw=dict(polar=False))

ax1.set_title('Radar Chart: Technological Infrastructure\nAssessment of Planets', fontsize=12, fontweight='bold')
polar_ax = fig.add_subplot(121, polar=True)
create_radar_chart(polar_ax, nova_terra, 'b', 'Nova Terra')
create_radar_chart(polar_ax, zynorra, 'r', 'Zynorra')
create_radar_chart(polar_ax, kaleron, 'g', 'Kaleron')
create_radar_chart(polar_ax, pyrros, 'orange', 'Pyrros')
polar_ax.set_yticklabels([])
polar_ax.set_xticks(np.linspace(0, 2 * np.pi, num_vars, endpoint=False))
polar_ax.set_xticklabels(categories, fontsize=10)
polar_ax.grid(True, linestyle='-', linewidth=0.6)
polar_ax.legend(loc='upper left', bbox_to_anchor=(-0.1, 1.1), frameon=False)

ax2.barh(categories, average_scores, color=['blue', 'crimson', 'forestgreen', 'darkorange', 'purple'])
ax2.set_xlim(0, 10)
ax2.set_title('Average Scores Across Categories', fontsize=12, fontweight='bold')
ax2.set_xlabel('Average Score')
ax2.invert_yaxis()  # Invert y-axis for horizontal bars
for i, score in enumerate(average_scores):
    ax2.text(score + 0.2, i, f'{score:.1f}', va='center', color='black', fontweight='bold')

plt.tight_layout()
plt.show()