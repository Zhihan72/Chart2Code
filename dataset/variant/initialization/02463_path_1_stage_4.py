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

# Randomly altered color selection
new_colors = ['#ffcc99', '#99ff99', '#c2c2f0', '#66b3ff', '#ff9999']

# Adjusting bar height and removing edge color for randomness
bars = ax1.barh(range(len(habitats)), sorted_total_populations, color=new_colors, height=0.7)

# Changing text formatting: different position and lighter font weight
for bar in bars:
    ax1.text(bar.get_width() + 10, bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}k', va='center', fontsize=9, fontweight='normal', color='blue')

# Adjusting grid style and turning it off for y-axis
ax1.xaxis.grid(True, linestyle='-.', alpha=0.75)
ax1.yaxis.grid(False)
ax1.set_xlim(0, 350)

# Change the style of the line in the second axis
ax2 = ax1.twiny()
ax2.axvline(average_dragonflies, color='purple', linestyle='--', linewidth=1.5)
ax2.set_xlim(0, 100)

plt.tight_layout()
plt.show()