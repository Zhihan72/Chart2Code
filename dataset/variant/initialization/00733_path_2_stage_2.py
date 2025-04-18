import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define decades and their influence scores (excluding 1940s)
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

# Title, labels, and axes ticks
plt.title('Evolving Trends in Vintage Fashion:\nInfluence of Decades on Modern Styles', fontsize=16, fontweight='bold')
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Influence Score', fontsize=12)
plt.xticks(decades)
plt.yticks(range(0, 101, 10))

# Automatically adjust layout
plt.tight_layout()

# Show plot
plt.show()