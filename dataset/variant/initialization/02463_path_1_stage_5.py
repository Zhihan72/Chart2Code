import matplotlib.pyplot as plt
import numpy as np

# Original habitat categories with additional 'Mountains' and 'Oceans'
habitats = ['Forests', 'Grasslands', 'Wetlands', 'Deserts', 'Urban Areas', 'Mountains', 'Oceans']

# Extended population data including data for the new habitats
population_data = np.array([
    [150, 50, 40, 10, 20, 15, 60],  # 'Forests'
    [70, 60, 25, 5, 10, 5, 20],      # 'Grasslands'
    [90, 70, 80, 15, 30, 10, 25],    # 'Wetlands'
    [15, 7, 3, 35, 5, 2, 5],         # 'Deserts'
    [50, 30, 60, 30, 20, 25, 35],    # 'Urban Areas'
    [25, 10, 5, 20, 15, 45, 50],     # 'Mountains'
    [30, 5, 10, 10, 5, 20, 70]       # 'Oceans'
])

total_populations = np.sum(population_data, axis=1)
sorted_indices = np.argsort(-total_populations)
sorted_total_populations = total_populations[sorted_indices]
sorted_habitats = [habitats[i] for i in sorted_indices]  # Sort habitats based on total populations

average_dragonflies = np.mean(population_data[:, -1])

fig, ax1 = plt.subplots(figsize=(14, 8))

new_colors = ['#ffcc99', '#99ff99', '#c2c2f0', '#66b3ff', '#ff9999', '#c2f0c2', '#ffb3e6']

bars = ax1.barh(range(len(habitats)), sorted_total_populations, color=new_colors, height=0.7)

for bar, habitat_name in zip(bars, sorted_habitats):
    ax1.text(bar.get_width() + 10, bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}k', va='center', fontsize=9, fontweight='normal', color='blue')

ax1.xaxis.grid(True, linestyle='-.', alpha=0.75)
ax1.yaxis.grid(False)
ax1.set_xlim(0, 350)
ax1.set_yticks(range(len(habitats)))
ax1.set_yticklabels(sorted_habitats)

ax2 = ax1.twiny()
ax2.axvline(average_dragonflies, color='purple', linestyle='--', linewidth=1.5)
ax2.set_xlim(0, 100)

plt.tight_layout()
plt.show()