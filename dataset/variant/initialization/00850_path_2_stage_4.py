import matplotlib.pyplot as plt
import numpy as np

light_intensity_1 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height_1 = np.array([15, 20, 25, 30, 35, 33, 31, 30, 28, 25])

light_intensity_2 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height_2 = np.array([10, 18, 22, 29, 33, 30, 29, 27, 26, 24])

plt.figure(figsize=(10, 6))
plt.scatter(light_intensity_1, plant_height_1, color='orange', edgecolors='grey', s=80, alpha=0.6, marker='^', label='Group A')
plt.scatter(light_intensity_2, plant_height_2, color='purple', edgecolors='grey', s=120, alpha=0.6, marker='x', label='Group B')

z1 = np.polyfit(light_intensity_1, plant_height_1, 2)
p1 = np.poly1d(z1)
plt.plot(light_intensity_1, p1(light_intensity_1), "red", label='Trend A', linewidth=2, linestyle='-.')
z2 = np.polyfit(light_intensity_2, plant_height_2, 2)
p2 = np.poly1d(z2)
plt.plot(light_intensity_2, p2(light_intensity_2), "blue", label='Trend B', linewidth=2, linestyle=':')

plt.title('Illumination vs. Vegetation', fontsize=16, fontweight='bold', pad=30)
plt.xlabel('Light (Lux)', fontsize=13)
plt.ylabel('Height (cm)', fontsize=13)

plt.grid(True, linestyle='-', alpha=0.3)
plt.legend(title='Pattern Type', loc='lower left', ncol=2)

plt.tight_layout()

plt.show()