import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2025)
species_a = np.array([30, 32, 35, 38, 41, 44, 47, 51, 55, 60, 66, 72, 79, 85, 92, 100, 110, 120, 130, 140])
species_b = np.array([45, 46, 48, 51, 54, 56, 59, 61, 63, 65, 68, 71, 73, 75, 78, 80, 82, 84, 86, 88])
species_c = np.array([20, 21, 24, 27, 29, 31, 34, 36, 39, 42, 45, 49, 53, 57, 61, 65, 70, 75, 80, 85])

population_data = np.vstack([species_a, species_b, species_c])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.stackplot(years, population_data, colors=['#ffcc99', '#66b3ff', '#99ff99'], alpha=0.8)

ax1.set_title('Biodiversity in the Reserve: Growth Trends of Different Species (2005-2025)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Population (millions)', fontsize=14)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=12)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()