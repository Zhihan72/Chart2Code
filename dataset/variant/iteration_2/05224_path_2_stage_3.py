import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])
species_a_population = np.array([50, 150, 300, 350, 400])
species_c_population = np.array([80, 130, 180, 240, 310])

plt.figure(figsize=(12, 8))

plt.scatter(decades, species_a_population, color='blue', label='A', edgecolor='k', s=100, alpha=0.7)
plt.scatter(decades, species_c_population, color='blue', label='C', edgecolor='k', s=100, alpha=0.7)

plt.title('Bird Population Growth (1980-2020)', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Birds', fontsize=12)

plt.legend(title='Species', loc='upper left')
plt.grid(visible=True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()