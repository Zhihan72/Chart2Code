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

# Plot setup
plt.figure(figsize=(10, 6))
plt.scatter(decades, influence_scores, color='deeppink', s=100, edgecolor='black')
plt.plot(decades_smooth, influence_scores_smooth, color='purple', linestyle='-', linewidth=2)

# Remove title, labels, and tick labels
plt.xticks([])
plt.yticks([])

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()