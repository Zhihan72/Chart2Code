import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

study_hours = np.array([1.0, 2.8, 3.5, 3.8, 5.7, 6.2, 7.3, 8.5, 9.3, 10.2])
sleep_quality = np.array([8.8, 8.1, 8.3, 7.5, 6.1, 5.7, 4.9, 4.2, 3.5, 2.8])

x_smooth = np.linspace(study_hours.min(), study_hours.max(), 300)
spline = make_interp_spline(study_hours, sleep_quality, k=3)
y_smooth = spline(x_smooth)

plt.figure(figsize=(10, 6))
plt.scatter(study_hours, sleep_quality, color='dodgerblue', s=100, edgecolor='white', zorder=5, label='Data')
plt.plot(x_smooth, y_smooth, color='firebrick', lw=2.5, zorder=4, label='Fit Line')

plt.title('Study vs. Sleep Quality', fontsize=14, weight='bold', pad=20)
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Sleep Quality', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.show()