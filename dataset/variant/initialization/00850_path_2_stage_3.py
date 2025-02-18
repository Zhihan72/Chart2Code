import matplotlib.pyplot as plt
import numpy as np

# Original data series
light_intensity_1 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height_1 = np.array([15, 20, 25, 30, 35, 33, 31, 30, 28, 25])

# Additional made-up data series
light_intensity_2 = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height_2 = np.array([10, 18, 22, 29, 33, 30, 29, 27, 26, 24])

plt.figure(figsize=(10, 6))
# Plotting the original data series
plt.scatter(light_intensity_1, plant_height_1, color='navy', edgecolors='black', s=100, alpha=0.7, label='Group 1')
# Plotting the additional data series
plt.scatter(light_intensity_2, plant_height_2, color='green', edgecolors='black', s=100, alpha=0.7, label='Group 2')

# Trend line for the original data series
z1 = np.polyfit(light_intensity_1, plant_height_1, 2)
p1 = np.poly1d(z1)
plt.plot(light_intensity_1, p1(light_intensity_1), "gold", label='Trend Group 1', linewidth=1.5)

# Trend line for the additional data series
z2 = np.polyfit(light_intensity_2, plant_height_2, 2)
p2 = np.poly1d(z2)
plt.plot(light_intensity_2, p2(light_intensity_2), "lightgreen", label='Trend Group 2', linewidth=1.5)

plt.title('Light vs. Plant Growth', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Light (Lux)', fontsize=12)
plt.ylabel('Height (cm)', fontsize=12)

# Adding annotations for the original data series
for i in range(len(light_intensity_1)):
    plt.text(light_intensity_1[i] + 10, plant_height_1[i] + 0.5, f'{plant_height_1[i]}', fontsize=9, ha='left')

# Adding annotations for the additional data series
for i in range(len(light_intensity_2)):
    plt.text(light_intensity_2[i] - 30, plant_height_2[i] - 0.5, f'{plant_height_2[i]}', fontsize=9, ha='right')

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Pattern', loc='upper right')

plt.tight_layout()

plt.show()