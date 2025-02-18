import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Adding two made-up species f and g
species_f = [25, 28, 30, 35, 37, 39, 42, 45, 50, 55, 60]
species_g = [15, 17, 19, 20, 22, 24, 26, 30, 32, 34, 36]

# Including the new species data with the existing
data = np.array([
    [50, 60, 70, 80, 85, 90, 95, 100, 110, 120, 130],  # species_a
    [30, 32, 34, 35, 38, 40, 45, 47, 50, 55, 58],      # species_b
    [20, 18, 15, 17, 16, 19, 22, 25, 27, 29, 30],      # species_c
    [10, 12, 14, 13, 11, 10, 12, 15, 20, 18, 15],      # species_d
    [5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25],         # species_e
    species_f,                                         # species_f
    species_g                                          # species_g
])

single_color = '#87cefa'

fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, data, colors=[single_color] * data.shape[0], alpha=0.7)

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