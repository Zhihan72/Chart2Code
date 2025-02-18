import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Data for plotting
decades = np.array([1950, 1960, 1970, 1980, 1990])
influence_scores = np.array([35, 50, 70, 65, 55])

# Generate a smooth curve using spline interpolation
decades_smooth = np.linspace(decades.min(), decades.max(), 300)
spline = make_interp_spline(decades, influence_scores, k=3)
influence_scores_smooth = spline(decades_smooth)

# Plot setup with new colors
plt.figure(figsize=(10, 6))
plt.scatter(decades, influence_scores, color='cyan', s=100, edgecolor='black')
plt.plot(decades_smooth, influence_scores_smooth, color='green', linestyle='-', linewidth=2)

plt.xticks([])
plt.yticks([])

plt.tight_layout()

plt.show()