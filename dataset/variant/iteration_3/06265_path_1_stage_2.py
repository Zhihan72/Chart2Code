import matplotlib.pyplot as plt
import numpy as np

cities = ['City A', 'City B', 'City C', 'City D']
green_spaces_hectares = [300, 150, 220, 280]
air_quality_index = [45, 70, 55, 60]
population_density = [5000, 7000, 6000, 6500]

fig, ax1 = plt.subplots(figsize=(14, 8))

scatter = ax1.scatter(green_spaces_hectares, air_quality_index, c=range(len(cities)), cmap='viridis', s=200, edgecolor='black', alpha=0.8)
ax1.plot(green_spaces_hectares, air_quality_index, color='slategray', linewidth=2, linestyle='--')

ax1.set_title("Green Spaces and Air Quality: A Comparative Study of Urban Environments", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Green Spaces (Hectares)', fontsize=12)
ax1.set_ylabel('Air Quality Index (AQI)', fontsize=12, color='tab:blue')

for i, city in enumerate(cities):
    ax1.annotate(city, (green_spaces_hectares[i], air_quality_index[i]), fontsize=10, xytext=(10,5), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='slategray', lw=0.5))

ax2 = ax1.twinx()
ax2.set_ylabel('Population Density (people/sq km)', fontsize=12, color='tab:green')
ax2.plot(green_spaces_hectares, population_density, color='darkgreen', linewidth=2, linestyle='-', marker='D', markersize=10, label='Population Density')

fig.legend(loc='upper left', fontsize=10, title_fontsize=11)

cbar = fig.colorbar(scatter, ax=ax1, orientation='vertical')
cbar.set_label('City Index', rotation=270, labelpad=15)

ax1.grid(True, linestyle='--', alpha=0.7)
plt.xlim(100, 350)
ax1.set_ylim(40, 80)
ax2.set_ylim(4000, 7500)

plt.tight_layout()
plt.show()