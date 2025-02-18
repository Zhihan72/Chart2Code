import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051)

# Randomly altered data within the same group structure
urban_parks = np.linspace(50, 500, len(years))
roof_gardens = 10 + 14 * np.log1p(years - 2000)  # Slightly altered the multiplier and base value
green_walls = 7 + (years - 2000) ** 1.2  # Altered the exponent and base value

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 12))

# Plot using the altered data
ax1.plot(years, urban_parks, label='Urban Parks', color='#A44A3F', linewidth=2, marker='o')
ax1.plot(years, roof_gardens, label='Roof Gardens', color='#63A375', linewidth=2, marker='s')
ax1.plot(years, green_walls, label='Green Walls', color='#E6B655', linewidth=2, marker='^')

ax1.set_title('Growth of Urban Green Spaces (2000-2050)\nFostering Sustainable Urbanization', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Area (sq km)', fontsize=14)
ax1.legend(loc='upper left', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.5)

ax1.annotate('Significant Uptake Post-2025', xy=(2025, 150), xytext=(2030, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

# Randomized project numbers within the same Fibonacci structure
expansion_projects_urban_parks = [1, 3, 2, 8, 5, 13, 21, 34, 55, 144, 89, 233]  # Swapped some values
expansion_projects_roof_gardens = [1, 2, 1, 5, 3, 8, 13, 21, 34, 89, 55, 144]  # Swapped some values
expansion_projects_green_walls = [1, 2, 1, 3, 5, 8, 13, 13, 21, 34, 55, 89]  # Swapped some values

decades = np.arange(2000, 2060, 5)
width = 8

ax2.bar(decades - width, expansion_projects_urban_parks, width, label='Urban Parks', color='#A44A3F')
ax2.bar(decades, expansion_projects_roof_gardens, width, label='Roof Gardens', color='#63A375')
ax2.bar(decades + width, expansion_projects_green_walls, width, label='Green Walls', color='#E6B655')

ax2.set_title('Number of Expansion Projects by Decade\n(2000-2050)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Decade', fontsize=14)
ax2.set_ylabel('Number of Projects', fontsize=14)
ax2.set_xticks(decades)
ax2.legend(loc='upper left', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()