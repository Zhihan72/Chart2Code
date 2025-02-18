import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

trees_area = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 110, 120])
shrubs_area = np.array([5, 6, 8, 10, 12, 15, 18, 21, 25, 29, 34, 38, 43, 47, 50, 55, 60, 65, 70, 76, 80])
flowers_area = np.array([2, 4, 8, 12, 15, 18, 22, 25, 29, 32, 35, 38, 40, 45, 48, 52, 55, 58, 62, 65, 68])
herbs_area = np.array([1, 2, 3, 5, 8, 12, 15, 18, 21, 24, 28, 31, 35, 38, 42, 45, 48, 50, 55, 58, 60])

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(
    years,
    trees_area,
    shrubs_area,
    flowers_area,
    herbs_area,
    labels=['Trees', 'Shrubs', 'Flowers', 'Herbs'],
    colors=['#228B22', '#FFD700', '#FF69B4', '#7B68EE'],
    alpha=0.6
)

ax.set_title("Flora Growth (2000-2020)", fontsize=18, fontweight='bold', pad=15)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Acreage", fontsize=14)

ax.set_xticks(years[::2])
ax.set_xticklabels([str(year) for year in years[::2]], rotation=45, ha='right', fontsize=12)
ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))

ax.legend(title="Varieties", fontsize=12, loc='lower right')

ax.grid(True, linestyle=':', color='gray', linewidth=0.5)
ax.spines['top'].set_visible(False)

plt.tight_layout()

plt.show()