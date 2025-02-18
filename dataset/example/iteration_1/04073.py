import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart depicts the population changes in different ecosystems over a decade.
# We focus on three main ecosystems: Forest, Grassland, and Wetland, and their evolution
# according to population growth and decline metrics.

# Define the years
years = np.arange(2010, 2021)

# Create contextual data inputs
# Population (in thousands) for three ecosystems
forest_population = [1200, 1180, 1175, 1165, 1150, 1140, 1135, 1125, 1110, 1100, 1090]
grassland_population = [800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850]
wetland_population = [600, 590, 580, 570, 560, 550, 540, 530, 520, 510, 500]

# Create the figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting line charts for each ecosystem
ax.plot(years, forest_population, label='Forest', color='#228B22', linewidth=2, marker='o')
ax.plot(years, grassland_population, label='Grassland', color='#FFD700', linewidth=2, marker='s')
ax.plot(years, wetland_population, label='Wetland', color='#4682B4', linewidth=2, marker='^')

# Adding highlights for significant shifts
significant_years = [2015, 2020]
significant_values_forest = [1140, 1090]
significant_values_grassland = [825, 850]
significant_values_wetland = [550, 500]

ax.plot(significant_years, significant_values_forest, 'ro', markersize=10)
ax.plot(significant_years, significant_values_grassland, 'ro', markersize=10)
ax.plot(significant_years, significant_values_wetland, 'ro', markersize=10)

# Annotating the highlights
ax.annotate('Significant Decline in Forest Ecosystem', xy=(2015, 1140), 
            xytext=(2016, 1150), arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')
ax.annotate('Steady Growth in Grassland Ecosystem', xy=(2020, 850), 
            xytext=(2019, 860), arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')
ax.annotate('Consistent Decline in Wetland Ecosystem', xy=(2020, 500), 
            xytext=(2018, 510), arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, ha='center')

# Adding titles and labels
ax.set_title('Population Dynamics in Different Ecosystems (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Population (in thousands)', fontsize=12)

# Adding grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding legend
ax.legend(title='Ecosystem', fontsize=10, title_fontsize='12')

# Prevent overlapping text and elements
plt.tight_layout()

# Show the plot
plt.show()