import matplotlib.pyplot as plt
import numpy as np

green_spaces_hectares = [300, 150, 220, 280]
air_quality_index = [45, 70, 55, 60]
population_density = [5000, 7000, 6000, 6500]

fig, ax1 = plt.subplots(figsize=(14, 8))

scatter = ax1.scatter(green_spaces_hectares, air_quality_index, c=range(len(green_spaces_hectares)), cmap='viridis', s=200, edgecolor='black', alpha=0.8)
ax1.plot(green_spaces_hectares, air_quality_index, color='slategray', linewidth=2, linestyle='--')

ax2 = ax1.twinx()
ax2.plot(green_spaces_hectares, population_density, color='darkgreen', linewidth=2, linestyle='-', marker='D', markersize=10)

ax1.grid(True, linestyle='--', alpha=0.7)
plt.xlim(100, 350)
ax1.set_ylim(40, 80)
ax2.set_ylim(4000, 7500)

plt.tight_layout()
plt.show()