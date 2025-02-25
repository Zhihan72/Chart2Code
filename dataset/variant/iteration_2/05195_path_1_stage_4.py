import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
species_f = [25, 28, 30, 35, 37, 39, 42, 45, 50, 55, 60]
species_g = [15, 17, 19, 20, 22, 24, 26, 30, 32, 34, 36]

data = np.array([
    [50, 60, 70, 80, 85, 90, 95, 100, 110, 120, 130],
    [30, 32, 34, 35, 38, 40, 45, 47, 50, 55, 58],
    [20, 18, 15, 17, 16, 19, 22, 25, 27, 29, 30],
    [10, 12, 14, 13, 11, 10, 12, 15, 20, 18, 15],
    [5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25],
    species_f,
    species_g
])

single_color = '#87cefa'

fig, ax = plt.subplots(figsize=(14, 9))
ax.stackplot(years, data, colors=[single_color] * data.shape[0], alpha=0.7)

ax.set_title('Avian Travel Patterns at Reserve (2010-2020)', fontsize=18, fontweight='bold', loc='left')
ax.set_xlabel('Calendar Year', fontsize=14)
ax.set_ylabel('Population Count', fontsize=14)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_color('none')

ax.set_xticks(years)

plt.tight_layout()
plt.show()