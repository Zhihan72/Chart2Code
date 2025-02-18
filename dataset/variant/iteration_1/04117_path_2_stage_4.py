import matplotlib.pyplot as plt
import numpy as np

soil_moisture_1 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
plant_growth_1 = np.array([2, 4, 7, 9, 13, 15, 16, 18, 20, 21, 23, 24])

soil_moisture_2 = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
plant_growth_2 = np.array([1, 3, 6, 10, 11, 14, 15, 17, 19, 20, 22, 23])

plt.figure(figsize=(12, 8))

plt.scatter(soil_moisture_1, plant_growth_1, color='seagreen', alpha=0.5, s=80, marker='^', edgecolor='orange', label='Data Series 1')
plt.scatter(soil_moisture_2, plant_growth_2, color='coral', alpha=0.5, s=80, marker='o', edgecolor='brown', label='Data Series 2')

z1 = np.polyfit(soil_moisture_1, plant_growth_1, 3)
p1 = np.poly1d(z1)

z2 = np.polyfit(soil_moisture_2, plant_growth_2, 3)
p2 = np.poly1d(z2)

xp = np.linspace(soil_moisture_1.min(), soil_moisture_1.max(), 500)
plt.plot(xp, p1(xp), color='slateblue', linestyle='-', linewidth=1.5, label='Polynomial Fit Series 1')
plt.plot(xp, p2(xp), color='crimson', linestyle='--', linewidth=1.5, label='Polynomial Fit Series 2')

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