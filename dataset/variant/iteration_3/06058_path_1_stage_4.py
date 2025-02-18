import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

trees = np.array([50, 52, 54, 58, 64, 70, 75, 80, 85, 87, 89, 90, 92, 94, 95, 97, 98, 100, 103, 107, 110])
shrubs = np.array([30, 32, 34, 36, 38, 40, 44, 48, 50, 53, 56, 58, 60, 64, 68, 72, 76, 78, 80, 82, 85])
wildflowers = np.array([20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180])

# Added new data for grasses
grasses = np.array([10, 15, 18, 22, 27, 32, 37, 40, 45, 50, 55, 60, 65, 68, 72, 75, 78, 81, 85, 90, 95])

# Combined all data into a single array
flora_data = np.vstack([trees, shrubs, wildflowers, grasses])

fig, ax = plt.subplots(figsize=(14, 9))

ax.stackplot(years, flora_data, colors=['#AFEEEE', '#FFE4C4', '#8A2BE2', '#98FB98'], alpha=0.8, edgecolor='black', linewidth=0.5)

# Updated legend to include new data
ax.legend(['Trees', 'Shrubs', 'Wildflowers', 'Grasses'], loc='upper left', fontsize=10, frameon=True)

ax.grid(axis='y', alpha=0.5, linestyle=':')

ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')

plt.tight_layout()
plt.show()