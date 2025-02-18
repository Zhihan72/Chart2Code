import matplotlib.pyplot as plt
import numpy as np

light_intensity = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height = np.array([15, 20, 25, 30, 35, 33, 31, 30, 28, 25])

plt.figure(figsize=(10, 6))
plt.scatter(light_intensity, plant_height, color='forestgreen', edgecolors='black', s=100, alpha=0.7)

z = np.polyfit(light_intensity, plant_height, 2)
p = np.poly1d(z)
plt.plot(light_intensity, p(light_intensity), "r--", label='Trend', linewidth=1.5)

plt.title('Light vs. Plant Growth', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Light (Lux)', fontsize=12)
plt.ylabel('Height (cm)', fontsize=12)

for i in range(len(light_intensity)):
    plt.text(light_intensity[i] + 10, plant_height[i] + 0.5, f'{plant_height[i]}', fontsize=9, ha='left')

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Pattern', loc='upper right')

plt.tight_layout()

plt.show()