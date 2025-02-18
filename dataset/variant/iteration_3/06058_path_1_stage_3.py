import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

trees = np.array([50, 52, 54, 58, 64, 70, 75, 80, 85, 87, 89, 90, 92, 94, 95, 97, 98, 100, 103, 107, 110])
shrubs = np.array([30, 32, 34, 36, 38, 40, 44, 48, 50, 53, 56, 58, 60, 64, 68, 72, 76, 78, 80, 82, 85])
wildflowers = np.array([20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 100, 110, 120, 130, 140, 150, 160, 170, 180])

flora_data = np.vstack([trees, shrubs, wildflowers])

fig, ax = plt.subplots(figsize=(14, 9))

# Changed colors and line styles
ax.stackplot(years, flora_data, colors=['#AFEEEE', '#FFE4C4', '#8A2BE2'], alpha=0.8, edgecolor='black', linewidth=0.5)

# Added legend
ax.legend(['Trees', 'Shrubs', 'Wildflowers'], loc='upper left', fontsize=10, frameon=True)

# Changed grid style
ax.grid(axis='y', alpha=0.5, linestyle=':')

# Added borders
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_color('grey')
ax.spines['right'].set_color('grey')

plt.tight_layout()
plt.show()