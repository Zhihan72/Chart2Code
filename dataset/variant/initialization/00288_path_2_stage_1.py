import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

soil_carbon_content = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plant_growth_height = np.array([10, 13, 21, 25, 33, 35, 38, 45, 50, 58])

coefs = np.polyfit(soil_carbon_content, plant_growth_height, 2)
polynomial_fit = Polynomial(coefs[::-1])

x_smooth = np.linspace(soil_carbon_content.min(), soil_carbon_content.max(), 200)
y_smooth = polynomial_fit(x_smooth)

plt.figure(figsize=(10, 6))
plt.scatter(soil_carbon_content, plant_growth_height, color='forestgreen', s=100, edgecolor='black', alpha=0.7)
plt.plot(x_smooth, y_smooth, color='darkorange', linewidth=2)

plt.title("Soil Carbon Content vs Plant Growth\nAnalysis in the Greenbelt Zone", fontsize=16, fontweight='bold')
plt.xlabel("Soil Carbon Content (%)", fontsize=12)
plt.ylabel("Plant Growth (Height in cm)", fontsize=12)

plt.tight_layout()

plt.show()