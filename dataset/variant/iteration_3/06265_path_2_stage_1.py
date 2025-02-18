import matplotlib.pyplot as plt
import numpy as np

# Data for green spaces (in hectares) and air quality index (lower is better)
cities = ['City A', 'City B', 'City C']
green_spaces_hectares = [300, 150, 220]
air_quality_index = [45, 70, 55]
population_density = [5000, 7000, 6000]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Scatter plot for green space vs air quality with new color set
scatter = ax1.scatter(green_spaces_hectares, air_quality_index, c=range(len(cities)), cmap='Set2', s=200, edgecolor='black', alpha=0.8)
ax1.plot(green_spaces_hectares, air_quality_index, color='gray', linewidth=2, linestyle='--')

ax1.set_title("Green Spaces and Air Quality: A Comparative Study of Urban Environments", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Green Spaces (Hectares)', fontsize=12)
ax1.set_ylabel('Air Quality Index (AQI)', fontsize=12, color='tab:blue')

# Annotate each city
for i, city in enumerate(cities):
    ax1.annotate(city, (green_spaces_hectares[i], air_quality_index[i]), fontsize=10, xytext=(10,5), textcoords='offset points', arrowprops=dict(arrowstyle='->', color='gray', lw=0.5))

# Second y-axis for population density
ax2 = ax1.twinx()
ax2.set_ylabel('Population Density (people/sq km)', fontsize=12, color='tab:green')
ax2.plot(green_spaces_hectares, population_density, color='green', linewidth=2, linestyle='-', marker='D', markersize=10, label='Population Density')

fig.legend(loc='upper left', fontsize=10, title_fontsize=11)

# Color bar for scatter plot
cbar = fig.colorbar(scatter, ax=ax1, orientation='vertical')
cbar.set_label('City Index', rotation=270, labelpad=15)

ax1.grid(True, linestyle='--', alpha=0.7)
plt.xlim(100, 350)
ax1.set_ylim(40, 80)
ax2.set_ylim(4000, 7500)

plt.tight_layout()
plt.show()