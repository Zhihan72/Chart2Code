# With the removal of the plant_height data, there is no dependent variable to plot against.
# The chart cannot be plotted with just soil_carbon data alone, as there needs to be a corresponding dependent variable for meaningful visualization.
# Therefore, after removing plant_height, the code cannot provide a scatter plot or fit line.

import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

soil_carbon = np.array([1, 2, 3, 4, 5, 6,])
plant_height = np.array([10, 13, 21, 25, 33, 35,])

coefs = np.polyfit(soil_carbon, plant_height, 2)
poly_fit = Polynomial(coefs[::-1])

x_smooth = np.linspace(soil_carbon.min(), soil_carbon.max(), 200)
y_smooth = poly_fit(x_smooth)

plt.figure(figsize=(10, 6))
plt.scatter(soil_carbon, plant_height, color='darkorange', s=100, edgecolor='black', alpha=0.7)
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2)

plt.title("Carbon vs Growth\nGreenbelt", fontsize=16, fontweight='bold')
plt.xlabel("Carbon (%)", fontsize=12)
plt.ylabel("Growth (cm)", fontsize=12)

plt.tight_layout()
plt.show()