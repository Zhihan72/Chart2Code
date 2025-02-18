import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Original data
latitudes = np.array([-70, -50, -30, -10, 10, 30, 50, 70, 85])
water_intensity = np.array([5, 15, 25, 40, 60, 45, 30, 20, 10])

# Additional data series for another set of observations
latitudes_advanced = np.array([-75, -55, -35, -15, 15, 35, 55, 75, 90])
water_intensity_advanced = np.array([8, 18, 22, 35, 55, 40, 35, 22, 15])

# Fitting polynomial for original series
coefs = np.polyfit(latitudes, water_intensity, 2)
poly_fit = Polynomial(coefs)
latitudes_fit = np.linspace(-90, 90, 500)
water_intensity_fit = poly_fit(latitudes_fit)

# Fitting polynomial for additional series
coefs_advanced = np.polyfit(latitudes_advanced, water_intensity_advanced, 2)
poly_fit_advanced = Polynomial(coefs_advanced)
water_intensity_fit_advanced = poly_fit_advanced(latitudes_fit)

# Plot initial data
plt.figure(figsize=(12, 6))
plt.scatter(latitudes, water_intensity, color='navy', edgecolors='k', s=100)
plt.plot(latitudes_fit, water_intensity_fit, color='navy', linewidth=2, linestyle='--')

# Plot additional data
plt.scatter(latitudes_advanced, water_intensity_advanced, color='darkorange', edgecolors='k', s=100)
plt.plot(latitudes_fit, water_intensity_fit_advanced, color='darkorange', linewidth=2, linestyle='--')

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()