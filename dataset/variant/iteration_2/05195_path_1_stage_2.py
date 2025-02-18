import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
species_a = [50, 60, 70, 80, 85, 90, 95, 100, 110, 120, 130]
species_b = [30, 32, 34, 35, 38, 40, 45, 47, 50, 55, 58]
species_c = [20, 18, 15, 17, 16, 19, 22, 25, 27, 29, 30]
species_d = [10, 12, 14, 13, 11, 10, 12, 15, 20, 18, 15]
species_e = [5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25]

data = np.array([species_a, species_b, species_c, species_d, species_e])

single_color = '#87cefa'  # Light sky blue

fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, data, colors=[single_color] * len(data), alpha=0.7)

ax.set_title('Bird Migration Patterns at Sanctuary (2010-2020)', fontsize=18, fontweight='bold', loc='center')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Bird Population', fontsize=14)

# Remove the axis border
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')

ax.set_xticks(years)

plt.tight_layout()
plt.show()