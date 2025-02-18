import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Study hours and corresponding sleep quality scores
study_hours = np.array([1.0, 2.5, 3.0, 4.0, 5.5, 6.0, 7.5, 8.0, 9.0, 10.0])
sleep_quality = np.array([9.0, 8.5, 8.0, 7.0, 6.0, 5.5, 4.5, 4.0, 3.0, 2.5])

# Smooth the scatter plot using spline interpolation
x_smooth = np.linspace(study_hours.min(), study_hours.max(), 300)
spline = make_interp_spline(study_hours, sleep_quality, k=3)
y_smooth = spline(x_smooth)

# Create the scatter plot with smooth fitting
plt.figure(figsize=(10, 6))
plt.scatter(study_hours, sleep_quality, color='mediumseagreen', s=100, edgecolor='white', zorder=5, label='Data')
plt.plot(x_smooth, y_smooth, color='coral', lw=2.5, zorder=4, label='Trend')

# Customize the plot with title and labels
plt.title('Study vs Sleep Quality', fontsize=14, weight='bold', pad=20)
plt.xlabel('Study Hours', fontsize=12)
plt.ylabel('Sleep Quality', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Add a legend
plt.legend(loc='upper right', fontsize=10)

# Automatically adjust layout to fit elements neatly
plt.tight_layout()

# Display the plot
plt.show()