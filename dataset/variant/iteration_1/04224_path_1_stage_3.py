import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2040, 2071)

tubers = np.array([10, 12, 14, 18, 22, 28, 34, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155])
legumes = np.array([5, 7, 9, 12, 16, 20, 25, 30, 36, 42, 48, 55, 62, 70, 78, 87, 96, 106, 116, 127, 138, 150, 162, 175, 188, 202, 216, 231, 246, 262, 278])
leafy_greens = np.array([3, 4, 6, 8, 10, 12, 15, 17, 20, 23, 26, 30, 33, 37, 41, 45, 50, 54, 59, 64, 70, 75, 81, 87, 93, 100, 106, 113, 120, 128, 135])
fruits = np.array([2, 3, 5, 7, 10, 15, 20, 26, 32, 39, 46, 54, 63, 72, 82, 92, 103, 114, 126, 139, 152, 166, 181, 196, 212, 229, 247, 266, 285, 305, 325])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(years, tubers, legumes, leafy_greens, fruits,
             colors=['#98FB98', '#20B2AA', '#FF6347', '#FFD700'], alpha=0.7)

ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Volume (Tons)", fontsize=14)

ax.set_xticks(years[::2])
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()