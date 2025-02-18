import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051)

urban_parks = np.linspace(50, 500, len(years))
roof_gardens = 10 + 14 * np.log1p(years - 2000)
green_walls = 7 + (years - 2000) ** 1.2

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

ax1.plot(years, urban_parks, label='Urban Parks', color='#7F91C0', linewidth=3, linestyle='--', marker='d')
ax1.plot(years, roof_gardens, label='Roof Gardens', color='#D88C9A', linewidth=3, linestyle=':', marker='x')
ax1.plot(years, green_walls, label='Green Walls', color='#97C891', linewidth=3, linestyle='-.', marker='v')

ax1.set_title('Growth of Urban Green Spaces (2000-2050)\nFostering Sustainable Urbanization', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Area (sq km)', fontsize=14)
ax1.legend(loc='lower right', fontsize=10)
ax1.grid(True, linestyle='-', alpha=0.3)

ax1.annotate('Significant Uptake Post-2025', xy=(2025, 150), xytext=(2030, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

expansion_projects_urban_parks = np.array([1, 3, 2, 8, 5, 13, 21, 34, 55, 144, 89, 233])
expansion_projects_roof_gardens = np.array([1, 2, 1, 5, 3, 8, 13, 21, 34, 89, 55, 144])
expansion_projects_green_walls = np.array([1, 2, 1, 3, 5, 8, 13, 13, 21, 34, 55, 89])

# Balancing data around a center point (e.g., average)
average_projects = (expansion_projects_urban_parks + expansion_projects_roof_gardens + expansion_projects_green_walls) / 3

decades = np.arange(2000, 2060, 5)
width = 8

# Adjusting each subplot to make bars diverge from the central axis
ax2.bar(decades - width, expansion_projects_urban_parks - average_projects, width, label='Urban Parks', color='#7F91C0', hatch='/')
ax2.bar(decades, expansion_projects_roof_gardens - average_projects, width, label='Roof Gardens', color='#D88C9A', hatch='\\')
ax2.bar(decades + width, expansion_projects_green_walls - average_projects, width, label='Green Walls', color='#97C891', hatch='|')

ax2.axhline(0, color='grey', linewidth=0.8)

ax2.set_title('Number of Expansion Projects (Variation from Average) by Decade\n(2000-2050)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Decade', fontsize=14)
ax2.set_ylabel('Difference from Average', fontsize=14)
ax2.set_xticks(decades)
ax2.legend(loc='upper left', fontsize=11)
ax2.grid(False)

plt.tight_layout()
plt.show()