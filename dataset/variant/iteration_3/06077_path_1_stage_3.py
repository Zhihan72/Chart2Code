import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051)

urban_parks = np.linspace(50, 500, len(years))
roof_gardens = 20 + 10 * np.log1p(years - 2000)
green_walls = 5 + (years - 2000) ** 1.5

# create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# define width for the bars and create offset arrays for the grouped bars
width = 1.5
years_offsets = np.arange(len(years))

# plot the first subplot as a grouped bar chart
ax1.bar(years_offsets - width, urban_parks, width, label='Parks', color='#63A375')
ax1.bar(years_offsets, roof_gardens, width, label='Roofs', color='#FFD57E')
ax1.bar(years_offsets + width, green_walls, width, label='Walls', color='#CC444B')

ax1.set_title('Urban Green Spaces Growth (2000-2050)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Yr', fontsize=14)
ax1.set_ylabel('Area (sq km)', fontsize=14)
ax1.set_xticks(years_offsets)
ax1.set_xticklabels(years, rotation=90)
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)

# annotate the subplot similar to the line chart with updated coordinates
ax1.annotate('Uptake Post-2025', xy=(25, urban_parks[25]), xytext=(30, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# second subplot remains unchanged
expansion_projects_urban_parks = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
expansion_projects_roof_gardens = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
expansion_projects_green_walls = [1, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

decades = np.arange(2000, 2060, 5)

width = 8
ax2.bar(decades - width, expansion_projects_urban_parks, width, label='Parks', color='#63A375')
ax2.bar(decades, expansion_projects_roof_gardens, width, label='Roofs', color='#FFD57E')
ax2.bar(decades + width, expansion_projects_green_walls, width, label='Walls', color='#CC444B')

ax2.set_title('Proj. by Decade (2000-2050)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Decade', fontsize=14)
ax2.set_ylabel('Projects', fontsize=14)
ax2.set_xticks(decades)
ax2.legend(loc='upper left', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()