import matplotlib.pyplot as plt
import numpy as np

soil_moisture = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
plant_growth = np.array([2, 4, 7, 9, 13, 15, 16, 18, 20, 21, 23, 24])

plt.figure(figsize=(12, 8))

plt.scatter(soil_moisture, plant_growth, color='royalblue', alpha=0.7, s=100, edgecolor='black', label='Data')

z = np.polyfit(soil_moisture, plant_growth, 3)
p = np.poly1d(z)
xp = np.linspace(soil_moisture.min(), soil_moisture.max(), 500)
plt.plot(xp, p(xp), color='tomato', linestyle='--', linewidth=2, label='Fit')

plt.title('Soil vs. Growth', fontsize=16, fontweight='bold')
plt.xlabel('Moisture (%)', fontsize=14)
plt.ylabel('Growth (cm)', fontsize=14)
plt.legend(loc='upper left', fontsize=12, frameon=True, shadow=True)
plt.grid(True, linestyle='--', alpha=0.6)

plt.annotate('Optimal', 
             xy=(30, 15), 
             xytext=(35, 20), 
             arrowprops=dict(facecolor='black', arrowstyle='->'), 
             fontsize=12, color='purple')

plt.tight_layout()
plt.show()