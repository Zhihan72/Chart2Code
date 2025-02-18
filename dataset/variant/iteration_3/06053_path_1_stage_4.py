import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
trees_area = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120])
shrubs_area = np.array([5, 6, 8, 10, 12, 15, 18, 21, 25, 29, 34, 38, 43, 47, 50, 55, 60, 65, 70, 76, 80])
flowers_area = np.array([2, 4, 8, 12, 15, 18, 22, 25, 29, 32, 35, 38, 40, 45, 48, 52, 55, 58, 62, 65, 68])
herbs_area = np.array([1, 2, 3, 5, 8, 12, 15, 18, 21, 24, 28, 31, 35, 38, 42, 45, 48, 50, 55, 58, 60])
grasses_area = np.array([3, 5, 6, 8, 10, 12, 14, 16, 18, 21, 23, 26, 28, 30, 32, 35, 37, 40, 42, 44, 46])
bamboo_area = np.array([2, 3, 5, 7, 10, 13, 17, 20, 24, 26, 30, 33, 36, 40, 43, 46, 50, 54, 59, 63, 67])  # New data series added

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(
    years,
    trees_area, shrubs_area, flowers_area, herbs_area, grasses_area, bamboo_area,
    colors=['#228B22', '#BA55D3', '#FF69B4', '#ADFF2F', '#32CD32', '#FFD700'],  # Assigned a color for bamboo_area
    alpha=0.8
)

ax.set_xticks(years[::3])
ax.set_xticklabels([str(year) for year in years[::3]], rotation=30, ha='center', fontsize=10)
ax.yaxis.set_major_locator(plt.MaxNLocator(10))
ax.xaxis.grid(True, linestyle='-.', alpha=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.legend(['Grasses', 'Herbs', 'Flowers', 'Shrubs', 'Trees', 'Bamboo'], loc='upper left')  # Updated legend

plt.tight_layout()
plt.show()