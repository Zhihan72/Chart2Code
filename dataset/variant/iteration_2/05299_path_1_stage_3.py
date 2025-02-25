import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2025)
species_a_shuffled = np.array([30, 60, 66, 92, 41, 44, 38, 51, 35, 110, 55, 72, 79, 85, 32, 100, 140, 120, 130, 47])
species_b_shuffled = np.array([54, 46, 48, 51, 68, 56, 59, 71, 82, 84, 65, 80, 78, 75, 73, 61, 45, 86, 63, 88])
species_c_shuffled = np.array([57, 21, 24, 70, 77, 31, 34, 61, 29, 53, 20, 49, 42, 27, 39, 36, 75, 45, 80, 85])

population_data_shuffled = np.vstack([species_a_shuffled, species_b_shuffled, species_c_shuffled])

fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.stackplot(years, population_data_shuffled, colors=['#ffcc99', '#66b3ff', '#99ff99'], alpha=0.8)

ax1.set_title('Population Dynamics in Ecological Zones (2005-2025)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Counts (in thousands)', fontsize=14)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=12)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()