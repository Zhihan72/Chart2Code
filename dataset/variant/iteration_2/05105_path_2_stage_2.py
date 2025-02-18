import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

study_hours = np.array([1.0, 2.5, 3.0, 4.0, 5.5, 6.0, 7.5, 8.0, 9.0, 10.0])
sleep_quality = np.array([9.0, 8.5, 8.0, 7.0, 6.0, 5.5, 4.5, 4.0, 3.0, 2.5])

x_smooth = np.linspace(study_hours.min(), study_hours.max(), 300)
spline = make_interp_spline(study_hours, sleep_quality, k=3)
y_smooth = spline(x_smooth)

plt.figure(figsize=(10, 6))
plt.scatter(study_hours, sleep_quality, color='mediumseagreen', s=100, edgecolor='white', zorder=5)
plt.plot(x_smooth, y_smooth, color='coral', lw=2.5, zorder=4)

plt.title('Study vs Sleep Quality', fontsize=14, weight='bold', pad=20)
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Sleep Quality', fontsize=12)

# Remove grid
# plt.grid(True, linestyle='--', alpha=0.6)

# Hide the axes spines
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# Remove legend
# plt.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()