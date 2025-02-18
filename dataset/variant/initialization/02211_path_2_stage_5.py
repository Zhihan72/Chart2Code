import numpy as np
import matplotlib.pyplot as plt

continents = ['Afr', 'As', 'Eur', 'NA', 'SA', 'Oce']
energy_percentages = np.array([
    [25, 35, 10, 30], 
    [25, 15, 40, 20], 
    [15, 40, 20, 25],  
    [25, 10, 35, 30],  
    [15, 35, 20, 30],  
    [50, 10, 20, 20]   
])

total_percentages = energy_percentages.sum(axis=1)
sorted_indices = np.argsort(total_percentages)[::-1]
sorted_continents = [continents[i] for i in sorted_indices]
sorted_energy_percentages = energy_percentages[sorted_indices]

bar_width = 0.2
x_positions = np.arange(len(sorted_continents))

fig, ax = plt.subplots(figsize=(10, 6))
single_color = '#1E90FF'

for i in range(sorted_energy_percentages.shape[1]):
    ax.bar(x_positions + i * bar_width, sorted_energy_percentages[:, i], bar_width, color=single_color)

ax.set_xlabel('Cont.')
ax.set_ylabel('Pct.')
ax.set_title('Renewable Energy by Continent (2050)', fontsize=14, fontweight='bold')
ax.set_xticks(x_positions + bar_width * 1.5)
ax.set_xticklabels(sorted_continents, rotation=45, ha='right')

ax.grid(True, linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()