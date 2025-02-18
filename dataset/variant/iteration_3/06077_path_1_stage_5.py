import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2051)
urban_parks = np.linspace(50, 500, len(years))
roof_gardens = 20 + 10 * np.log1p(years - 2000)
green_walls = 5 + (years - 2000) ** 1.5

fig, ax1 = plt.subplots(1, 1, figsize=(14, 8))

width = 1.5
years_offsets = np.arange(len(years))

ax1.bar(years_offsets - width, urban_parks, width, color='#63A375')
ax1.bar(years_offsets, roof_gardens, width, color='#FFD57E')
ax1.bar(years_offsets + width, green_walls, width, color='#CC444B')

ax1.set_title('Urban Green Spaces Growth (2000-2050)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Yr', fontsize=14)
ax1.set_ylabel('Area (sq km)', fontsize=14)
ax1.set_xticks(years_offsets)
ax1.set_xticklabels(years, rotation=90)
ax1.annotate('Uptake Post-2025', xy=(25, urban_parks[25]), xytext=(30, 300),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

plt.tight_layout()
plt.show()