import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])
species_a_population = np.array([50, 150, 300, 350, 400])
# species_b_population data has been removed
species_c_population = np.array([80, 130, 180, 240, 310])

plt.figure(figsize=(12, 8))

plt.scatter(decades, species_a_population, color='green', edgecolor='k', s=100, alpha=0.7)
# Removed the plot for species_b_population
plt.scatter(decades, species_c_population, color='blue', edgecolor='k', s=100, alpha=0.7)

plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()