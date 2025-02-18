import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Manually altered population data for three ecosystems while preserving structure
forest_population = [1200, 1170, 1165, 1160, 1155, 1145, 1130, 1115, 1120, 1105, 1085]
grassland_population = [805, 800, 808, 812, 822, 820, 828, 832, 838, 848, 845]
wetland_population = [605, 588, 582, 569, 562, 552, 544, 529, 524, 511, 498]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, forest_population, label='Forest', color='#228B22', linewidth=2, marker='o')
ax.plot(years, grassland_population, label='Grassland', color='#FFD700', linewidth=2, marker='s')
ax.plot(years, wetland_population, label='Wetland', color='#4682B4', linewidth=2, marker='^')

significant_years = [2015, 2020]
significant_values_forest = [1145, 1085]
significant_values_grassland = [820, 845]
significant_values_wetland = [552, 498]

ax.plot(significant_years, significant_values_forest, 'ro', markersize=10)
ax.plot(significant_years, significant_values_grassland, 'ro', markersize=10)
ax.plot(significant_years, significant_values_wetland, 'ro', markersize=10)

ax.annotate('Significant Decline in Forest Ecosystem', xy=(2015, 1145), 
            xytext=(2016, 1160), arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')
ax.annotate('Steady Growth in Grassland Ecosystem', xy=(2020, 845), 
            xytext=(2019, 860), arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')
ax.annotate('Consistent Decline in Wetland Ecosystem', xy=(2020, 498), 
            xytext=(2018, 510), arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')

ax.set_title('Population Dynamics in Different Ecosystems (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (in thousands)', fontsize=12)

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title='Ecosystem', fontsize=10, title_fontsize='12')

plt.tight_layout()
plt.show()