import matplotlib.pyplot as plt
import numpy as np

# Data construction
years = np.arange(2013, 2023)
northern_hills_temp = [-2, -1, 0, 1, 2, -1, 0, -2, 1, 2]
desert_valley_temp = [25, 26, 27, 28, 29, 28, 26, 25, 27, 28]
tropical_forest_temp = [30, 31, 30, 31, 32, 31, 30, 31, 32, 31]

# Plotting the chart
fig, ax = plt.subplots(figsize=(14, 8))

# Randomly altering stylistic elements
ax.plot(years, northern_hills_temp, marker='s', linestyle='--', color='r', label='Northern Hills')
ax.plot(years, desert_valley_temp, marker='*', linestyle='-', color='b', label='Desert Valley')
ax.plot(years, tropical_forest_temp, marker='x', linestyle='-.', color='m', label='Tropical Forest')

# Adding legend
ax.legend(loc='upper left', frameon=False)

# Grid configuration
ax.grid(True, linestyle='-', linewidth=0.75)

# Borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Axis limits
ax.set_xlim(2013, 2022)
ax.set_ylim(-5, 35)

plt.tight_layout()
plt.show()