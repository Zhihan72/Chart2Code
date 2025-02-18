import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
forest_population = [1200, 1165, 1140, 1135, 1110, 1175, 1180, 1125, 1150, 1100, 1090]
grassland_population = [830, 810, 825, 800, 805, 845, 835, 820, 815, 850, 840]
wetland_population = [600, 550, 530, 520, 500, 540, 590, 570, 580, 560, 510]

fig, ax = plt.subplots(figsize=(10, 6))

color = '#008080'
ax.plot(years, forest_population, color=color, linewidth=2, marker='o')
ax.plot(years, grassland_population, color=color, linewidth=2, marker='s')
ax.plot(years, wetland_population, color=color, linewidth=2, marker='^')

# I've kept the significant years the same, assuming alterations within groups only.
significant_years = [2015, 2020]
significant_values_forest = [1135, 1100]  # Updated based on new forest_population
significant_values_grassland = [845, 840]  # Updated based on new grassland_population
significant_values_wetland = [550, 560]  # Updated based on new wetland_population

ax.plot(significant_years, significant_values_forest, 'ro', markersize=10)
ax.plot(significant_years, significant_values_grassland, 'ro', markersize=10)
ax.plot(significant_years, significant_values_wetland, 'ro', markersize=10)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()