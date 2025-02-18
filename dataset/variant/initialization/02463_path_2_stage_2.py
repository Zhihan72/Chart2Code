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

fig, ax = plt.subplots(figsize=(10, 6))

# Altering stylistic elements
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
bars = ax.barh(habitats, total_populations, color=colors, edgecolor='none')

# Adjusted data labels
for bar in bars:
    ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2,
            f'{int(bar.get_width())}k', va='center', fontsize=11, fontstyle='italic', color='darkblue')

ax.set_xlabel("Insect Population (Thousands)", fontsize=13, fontweight='light')
ax.xaxis.grid(True, linestyle='-.', alpha=0.7)
ax.set_xlim(0, 350)

ax.set_title("Insect Population Across Habitats", fontsize=18, fontweight='light', style='italic', pad=25)

plt.tight_layout()
plt.show()