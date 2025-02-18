import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

forest_population = [1200, 1170, 1165, 1160, 1155, 1145, 1130, 1115, 1120, 1105, 1085]
grassland_population = [805, 800, 808, 812, 822, 820, 828, 832, 838, 848, 845]
wetland_population = [605, 588, 582, 569, 562, 552, 544, 529, 524, 511, 498]

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(years, forest_population, label='Trees', color='darkgreen', linewidth=1.5, linestyle='--', marker='^')
ax.plot(years, grassland_population, label='Fields', color='peru', linewidth=2.5, linestyle=':', marker='d')
ax.plot(years, wetland_population, label='Swamps', color='teal', linewidth=1, linestyle='-.')

significant_years = [2015, 2020]
significant_values_forest = [1145, 1085]
significant_values_grassland = [820, 845]
significant_values_wetland = [552, 498]

ax.plot(significant_years, significant_values_forest, 'bo', markersize=8)
ax.plot(significant_years, significant_values_grassland, 'go', markersize=8)
ax.plot(significant_years, significant_values_wetland, 'mo', markersize=8)

ax.annotate('Critical Drop in Trees', xy=(2015, 1145), 
            xytext=(2016, 1160), arrowprops=dict(facecolor='orange', arrowstyle='->'),
            fontsize=9, ha='center')
ax.annotate('Positive Trend in Fields', xy=(2020, 845), 
            xytext=(2019, 860), arrowprops=dict(facecolor='red', arrowstyle='->'),
            fontsize=9, ha='center')
ax.annotate('Gradual Drop in Swamps', xy=(2020, 498), 
            xytext=(2018, 510), arrowprops=dict(facecolor='blue', arrowstyle='->'),
            fontsize=9, ha='center')

ax.set_title('Ecosystem Variations Over Time (2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Timeline', fontsize=11)
ax.set_ylabel('Counts (in thousands)', fontsize=11)

ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(title='Nature Types', fontsize=11, title_fontsize='13', loc='upper left')

plt.tight_layout()
plt.show()