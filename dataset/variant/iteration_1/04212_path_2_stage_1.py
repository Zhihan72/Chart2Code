import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2100, 2115)

# Energy production data (in terajoules, TJ) for different star types (shortened for the example)
red_dwarf = np.array([10, 15, 25, 35, 50, 70, 90, 110, 130, 150, 170, 200, 230, 260, 300])
yellow_dwarf = np.array([20, 28, 35, 45, 60, 80, 105, 130, 160, 190, 220, 250, 285, 320, 360])
blue_giant = np.array([5, 10, 17, 25, 35, 50, 65, 80, 95, 110, 130, 150, 170, 190, 210])
white_dwarf = np.array([2, 5, 9, 12, 16, 22, 28, 37, 43, 50, 60, 70, 82, 95, 110])
neutron_stars = np.array([1, 2, 4, 6, 9, 13, 17, 22, 28, 35, 42, 50, 59, 68, 78])

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Stack the areas for each star type with new distinct colors
ax.stackplot(years, red_dwarf, yellow_dwarf, blue_giant, white_dwarf, neutron_stars,
             labels=['Red Dwarf', 'Yellow Dwarf', 'Blue Giant', 'White Dwarf', 'Neutron Stars'],
             colors=['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231'])

# Customize the chart
ax.set_title('Galactic Energy Distribution (2100 - 2200)', fontsize=16)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Energy Production (TJ)', fontsize=14)
ax.legend(loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()