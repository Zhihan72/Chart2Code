import matplotlib.pyplot as plt
import numpy as np

habitats = ['Forests', 'Grasslands', 'Wetlands', 'Deserts', 'Urban Areas']
population_data = np.array([
    [150, 50, 40, 10, 20],
    [70, 60, 25, 5, 10],
    [90, 70, 80, 15, 30],
    [15, 7, 3, 35, 5],
    [50, 30, 60, 30, 20]
])

total_populations = np.sum(population_data, axis=1)
sorted_indices = np.argsort(-total_populations)
sorted_total_populations = total_populations[sorted_indices]

average_dragonflies = np.mean(population_data[:, -1])

fig, ax1 = plt.subplots(figsize=(14, 8))
new_colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
bars = ax1.barh(range(len(habitats)), sorted_total_populations, color=new_colors, edgecolor='black', height=0.6)

for bar in bars:
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}k', va='center', fontsize=10, fontweight='bold', color='black')

ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 350)
ax2 = ax1.twiny()
ax2.axvline(average_dragonflies, color='darkred', linestyle='-', linewidth=2)
ax2.set_xlim(0, 100)

plt.tight_layout()
plt.show()