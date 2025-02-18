import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)

fruits = [20, 22, 25, 27, 29, 31, 33, 35, 37, 40, 42]
vegetables = [15, 16, 18, 19, 20, 23, 24, 25, 26, 28, 30]
grains = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dairy = [25, 24, 23, 22, 21, 21, 20, 19, 18, 17, 17]
proteins = [30, 28, 27, 25, 24, 22, 21, 20, 19, 18, 17]

plt.figure(figsize=(14, 8))
plt.stackplot(years, fruits, vegetables, grains, dairy, proteins, 
              colors=['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700'], alpha=0.8)

# Remove title, axis labels, legend, and annotations
plt.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()