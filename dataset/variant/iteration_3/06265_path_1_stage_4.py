import matplotlib.pyplot as plt
import numpy as np

green_spaces_hectares = [300, 150, 220, 280]
air_quality_index = [45, 70, 55, 60]
population_density = [5000, 7000, 6000, 6500]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Changed the marker type, color map, edge color and alpha for scatter
scatter = ax1.scatter(green_spaces_hectares, air_quality_index, c=range(len(green_spaces_hectares)), cmap='plasma', s=150, edgecolor='red', alpha=0.6)

# Changed the line style and color for the first plot
ax1.plot(green_spaces_hectares, air_quality_index, color='purple', linewidth=3, linestyle='-.')

# Changed the line style, color, and marker type for the second plot
ax2 = ax1.twinx()
ax2.plot(green_spaces_hectares, population_density, color='darkorange', linewidth=3, linestyle=':', marker='o', markersize=8)

# Changed the grid style
ax1.grid(True, linestyle=':', alpha=0.5)

plt.xlim(100, 350)
ax1.set_ylim(40, 80)
ax2.set_ylim(4000, 7500)

plt.tight_layout()
plt.show()