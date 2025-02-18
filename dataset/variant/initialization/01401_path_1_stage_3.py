import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

latitudes = np.array([-70, -50, -30, -10, 10, 30, 50, 70])
water_intensity = np.array([5, 15, 25, 40, 60, 45, 30, 20])

coefs = np.polyfit(latitudes, water_intensity, 2)
poly_fit = Polynomial(coefs)

latitudes_fit = np.linspace(-90, 90, 500)
water_intensity_fit = poly_fit(latitudes_fit)

plt.figure(figsize=(12, 6))
plt.scatter(latitudes, water_intensity, color='mediumorchid', edgecolors='k', s=100)
plt.plot(latitudes_fit, water_intensity_fit, color='seagreen', linewidth=2, linestyle='--')

for lat, intensity in zip(latitudes, water_intensity):
    plt.annotate(f'({lat}, {intensity})', (lat, intensity), textcoords="offset points", xytext=(-10,10), ha='center')

plt.title("Exploration of Mars:\nMapping Water Traces Across Latitudes", fontsize=16, fontweight='bold')
plt.xlabel("Latitude (degrees)", fontsize=12)
plt.ylabel("Water Trace Intensity (arbitrary units)", fontsize=12)

plt.tight_layout()
plt.show()