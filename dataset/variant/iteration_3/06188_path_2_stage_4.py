import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2036)

fruits = [20, 22, 25, 27, 29, 31, 33, 35, 37, 40, 42]
grains = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
dairy = [25, 24, 23, 22, 21, 21, 20, 19, 18, 17, 17]
proteins = [30, 28, 27, 25, 24, 22, 21, 20, 19, 18, 17]

plt.figure(figsize=(14, 8))
plt.stackplot(years, fruits, grains, dairy, proteins, 
              colors=['#FFA500', '#9370DB', '#3CB371', '#FFD700'], alpha=0.85)

plt.grid(True, linestyle='-.', which='major', color='black', alpha=0.5)
plt.legend(['Fruits', 'Grains', 'Dairy', 'Proteins'], loc='upper left', fontsize=12, frameon=True, shadow=True)
plt.tight_layout()
plt.show()