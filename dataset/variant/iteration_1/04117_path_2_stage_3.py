import matplotlib.pyplot as plt
import numpy as np

soil_moisture = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
plant_growth = np.array([2, 4, 7, 9, 13, 15, 16, 18, 20, 21, 23, 24])

plt.figure(figsize=(12, 8))

plt.scatter(soil_moisture, plant_growth, color='seagreen', alpha=0.5, s=80, marker='^', edgecolor='orange', label='Data Points')

z = np.polyfit(soil_moisture, plant_growth, 3)
p = np.poly1d(z)
xp = np.linspace(soil_moisture.min(), soil_moisture.max(), 500)
plt.plot(xp, p(xp), color='slateblue', linestyle='-', linewidth=1.5, label='Polynomial Fit')

plt.title('Soil Moisture vs. Plant Growth', fontsize=18, fontweight='bold')
plt.xlabel('Moisture (%)', fontsize=13)
plt.ylabel('Growth (cm)', fontsize=13)
plt.legend(loc='lower right', fontsize=10, frameon=False)
plt.grid(True, linestyle='-', alpha=0.3)

plt.annotate('Growth Peak', 
             xy=(40, 21), 
             xytext=(45, 24), 
             arrowprops=dict(facecolor='gray', arrowstyle='->'), 
             fontsize=10, color='darkorange')

plt.tight_layout()
plt.show()