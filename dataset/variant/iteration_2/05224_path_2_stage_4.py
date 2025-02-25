import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1980, 1990, 2000, 2010, 2020])
species_a_population = np.array([50, 150, 300, 350, 400])
species_c_population = np.array([80, 130, 180, 240, 310])

plt.figure(figsize=(12, 8))

# Changed marker style, color, and added a linestyle
plt.plot(decades, species_a_population, color='red', label='A', linestyle='-', marker='o', markersize=8, linewidth=2, alpha=0.8)
plt.plot(decades, species_c_population, color='green', label='C', linestyle='--', marker='s', markersize=8, linewidth=2, alpha=0.8)

plt.title('Bird Population Growth (1980-2020)', fontsize=16, fontweight='bold', loc='center')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Birds', fontsize=12)

# Changed legend location and style
plt.legend(title='Species', loc='lower right', fontsize=10)

# Altered grid style
plt.grid(visible=True, linestyle=':', linewidth=1.5, alpha=0.5)

# Added plot border thickness
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['bottom'].set_linewidth(1.5)

plt.tight_layout()

plt.show()