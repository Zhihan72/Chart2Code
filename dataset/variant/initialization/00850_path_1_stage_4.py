import matplotlib.pyplot as plt
import numpy as np

light_intensity = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height_1 = np.array([15, 20, 25, 30, 35, 33, 31, 30, 28, 25])

water_level = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plant_height_2 = np.array([12, 18, 24, 29, 34, 32, 30, 28, 27, 26])

plt.figure(figsize=(10, 6))

# Plot original data
plt.scatter(light_intensity, plant_height_1, color='royalblue', edgecolors='black', s=100, alpha=0.7, label='Light Intensity')

# Plot additional data
plt.scatter(water_level, plant_height_2, color='royalblue', edgecolors='black', s=100, alpha=0.7, label='Water Level')

# Fit curve for the original data
z1 = np.polyfit(light_intensity, plant_height_1, 2)
p1 = np.poly1d(z1)
plt.plot(light_intensity, p1(light_intensity), "royalblue", linestyle='--', linewidth=1.5)

# Fit curve for the additional dataset
z2 = np.polyfit(water_level, plant_height_2, 2)
p2 = np.poly1d(z2)
plt.plot(water_level, p2(water_level), "royalblue", linestyle='--', linewidth=1.5)

plt.xticks([])
plt.yticks([])
plt.legend()
plt.show()