import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2100, 2115)

red_dwarf = np.array([10, 15, 25, 35, 50, 70, 90, 110, 130, 150, 170, 200, 230, 260, 300])
yellow_dwarf = np.array([20, 28, 35, 45, 60, 80, 105, 130, 160, 190, 220, 250, 285, 320, 360])
blue_giant = np.array([5, 10, 17, 25, 35, 50, 65, 80, 95, 110, 130, 150, 170, 190, 210])
white_dwarf = np.array([2, 5, 9, 12, 16, 22, 28, 37, 43, 50, 60, 70, 82, 95, 110])
neutron_stars = np.array([1, 2, 4, 6, 9, 13, 17, 22, 28, 35, 42, 50, 59, 68, 78])
black_holes = np.array([3, 6, 10, 15, 21, 29, 39, 50, 63, 77, 92, 108, 125, 143, 162])
supernovae = np.array([0, 1, 3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68, 80, 93])

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(years, red_dwarf, yellow_dwarf, blue_giant, white_dwarf, neutron_stars, black_holes, supernovae,
             labels=['Stellar Remnants', 'Bright Dwarfs', 'Giant Stars', 'Dim Dwarfs', 'Collapsed Stars', 'Gravity Wells', 'Explosive Ends'],
             colors=['#1e90ff']*7)

ax.set_title('Universe Energy Patterns 2100-2115', fontsize=16)
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('Energy Levels (TJ)', fontsize=14)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()