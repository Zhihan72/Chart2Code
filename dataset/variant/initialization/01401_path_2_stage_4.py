import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

latitudes = np.array([-70, -50, -30, -10, 10, 30, 50, 70, 85])
water_intensity = np.array([5, 15, 25, 40, 60, 45, 30, 20, 10])

latitudes_advanced = np.array([-75, -55, -35, -15, 15, 35, 55, 75, 90])
water_intensity_advanced = np.array([8, 18, 22, 35, 55, 40, 35, 22, 15])

coefs = np.polyfit(latitudes, water_intensity, 2)
poly_fit = Polynomial(coefs)
latitudes_fit = np.linspace(-90, 90, 500)
water_intensity_fit = poly_fit(latitudes_fit)

coefs_advanced = np.polyfit(latitudes_advanced, water_intensity_advanced, 2)
poly_fit_advanced = Polynomial(coefs_advanced)
water_intensity_fit_advanced = poly_fit_advanced(latitudes_fit)

plt.figure(figsize=(12, 6))
plt.scatter(latitudes, water_intensity, color='midnightblue', edgecolors='gray', s=120, marker='^')
plt.plot(latitudes_fit, water_intensity_fit, color='steelblue', linewidth=2.5, linestyle=':')

plt.scatter(latitudes_advanced, water_intensity_advanced, color='tomato', edgecolors='gray', s=120, marker='s')
plt.plot(latitudes_fit, water_intensity_fit_advanced, color='sandybrown', linewidth=2.5, linestyle='-.')

plt.grid(True, linestyle='-.', linewidth=0.7, alpha=0.9)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.tight_layout()
plt.show()