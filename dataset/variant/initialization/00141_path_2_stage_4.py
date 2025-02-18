import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

vegetables = np.array([2, 3, 4, 5, 7, 9, 11, 13, 15, 18, 22])
grains = np.array([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5])

population_growth = np.array([100, 102, 104, 106, 108, 110, 113, 115, 118, 121, 124])

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.stackplot(years, vegetables, grains, colors=['#1f77b4', '#ff7f0e'], alpha=0.8)

ax1.set_title('Nutritional Trends in Foodistan: 2010-2020', fontsize=16, fontweight='bold')
ax1.set_xlabel('Timeline', fontsize=12)
ax1.set_ylabel('Edibles (Million Tons)', fontsize=12)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

ax2 = ax1.twinx()
ax2.plot(years, population_growth, color='b', linestyle='-', marker='o')
ax2.set_ylabel('Inhabitants (Million)', fontsize=12)
ax2.tick_params(axis='y', labelcolor='b')

plt.tight_layout()
plt.show()