import matplotlib.pyplot as plt
import numpy as np

years = np.array([2050, 2051, 2052, 2053, 2054])
martian_potatoes = np.array([1.2, 1.5, 1.7, 2.0, 2.3])
space_carrots = np.array([1.0, 1.2, 1.5, 1.7, 2.1])

plt.figure(figsize=(10, 6))

# Use a single consistent color for both crop types
plt.plot(years, martian_potatoes, marker='o', linestyle='-', linewidth=2, color='tab:green')
plt.plot(years, space_carrots, marker='^', linestyle='-', linewidth=2, color='tab:green')

plt.xticks(years)

plt.tight_layout()
plt.show()