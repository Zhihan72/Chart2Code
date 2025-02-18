import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
forest_population = [1200, 1180, 1175, 1165, 1150, 1140, 1135, 1125, 1110, 1100, 1090]
grassland_population = [800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850]
wetland_population = [600, 590, 580, 570, 560, 550, 540, 530, 520, 510, 500]

fig, ax = plt.subplots(figsize=(10, 6))

color = '#008080'
ax.plot(years, forest_population, color=color, linewidth=2, marker='o')
ax.plot(years, grassland_population, color=color, linewidth=2, marker='s')
ax.plot(years, wetland_population, color=color, linewidth=2, marker='^')

significant_years = [2015, 2020]
significant_values_forest = [1140, 1090]
significant_values_grassland = [825, 850]
significant_values_wetland = [550, 500]

ax.plot(significant_years, significant_values_forest, 'ro', markersize=10)
ax.plot(significant_years, significant_values_grassland, 'ro', markersize=10)
ax.plot(significant_years, significant_values_wetland, 'ro', markersize=10)

ax.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()

plt.show()