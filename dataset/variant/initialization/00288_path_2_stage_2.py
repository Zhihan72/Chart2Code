import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

soil_carbon = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plant_height = np.array([10, 13, 21, 25, 33, 35, 38, 45, 50, 58])

coefs = np.polyfit(soil_carbon, plant_height, 2)
poly_fit = Polynomial(coefs[::-1])

x_smooth = np.linspace(soil_carbon.min(), soil_carbon.max(), 200)
y_smooth = poly_fit(x_smooth)

plt.figure(figsize=(10, 6))
plt.scatter(soil_carbon, plant_height, color='forestgreen', s=100, edgecolor='black', alpha=0.7)
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2)

plt.title("Carbon vs Growth\nGreenbelt", fontsize=16, fontweight='bold')
plt.xlabel("Carbon (%)", fontsize=12)
plt.ylabel("Growth (cm)", fontsize=12)

plt.tight_layout()

plt.show()