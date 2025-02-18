import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Define decades and their influence scores
decades = np.array([1940, 1950, 1960, 1970, 1980, 1990])
influence_scores = np.array([20, 35, 50, 70, 65, 55])

# Generate smooth curve using spline interpolation
decades_smooth = np.linspace(decades.min(), decades.max(), 300)
spline = make_interp_spline(decades, influence_scores, k=3)
influence_scores_smooth = spline(decades_smooth)

# Plot setup
plt.figure(figsize=(10, 6))

# Scatter plot with altered marker and edgecolor
plt.scatter(decades, influence_scores, color='navy', marker='x', label='Decade Points', s=100, edgecolor='orange')

# Smooth line with altered style
plt.plot(decades_smooth, influence_scores_smooth, color='green', linestyle='--', linewidth=2, label='Smooth Trend')

# Title, labels, and legend
plt.title('Impact of Decades on Fashion', fontsize=16, fontweight='bold')
plt.xlabel('Decade', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(decades)
plt.yticks(range(0, 101, 10))

# Legend with altered location
plt.legend(title='Legend', loc='lower right')

# Grid alteration and border removal
plt.grid(True, linestyle='-.', linewidth=0.5, color='gray', alpha=0.7)

# Removing the axhline for cleaner look
# plt.axhline(y=50, color='gray', linestyle='--', linewidth=1, alpha=0.7)

plt.xticks(decades)
plt.tight_layout()
plt.show()