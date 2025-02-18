import matplotlib.pyplot as plt
import numpy as np

# Data construction
years = np.arange(2013, 2023)
northern_hills_temp = [-2, -1, 0, 1, 2, -1, 0, -2, 1, 2]
desert_valley_temp = [25, 26, 27, 28, 29, 28, 26, 25, 27, 28]
tropical_forest_temp = [30, 31, 30, 31, 32, 31, 30, 31, 32, 31]

# Plotting the chart
fig, ax = plt.subplots(figsize=(14, 8))

# Apply a single color consistently
color = 'g'

ax.plot(years, northern_hills_temp, marker='o', linestyle='-', color=color)
ax.plot(years, desert_valley_temp, marker='^', linestyle='-.', color=color)
ax.plot(years, tropical_forest_temp, marker='d', linestyle=':', color=color)

ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_xlim(2013, 2022)
ax.set_ylim(-5, 35)

plt.tight_layout()
plt.show()