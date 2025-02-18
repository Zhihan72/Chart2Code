import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2025)

species_a = np.array([30, 32, 35, 38, 41, 44, 47, 51, 55, 60, 66, 72, 79, 85, 92, 100, 110, 120, 130, 140])
species_b = np.array([45, 46, 48, 51, 54, 56, 59, 61, 63, 65, 68, 71, 73, 75, 78, 80, 82, 84, 86, 88])

population_data = np.vstack([species_a, species_b])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.stackplot(years, population_data, colors=['#66b3ff', '#99ff99'], alpha=0.8)

ax1.set_title('Ecosystem Dynamics: Populations of Various Fauna (2005-2025)', fontsize=18, fontweight='bold')
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Count (millions)', fontsize=14)

ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=12)

ax1.annotate('Accelerated expansion of Type A', xy=(2018, 100), xytext=(2013, 70),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkred')

plt.tight_layout()

plt.show()