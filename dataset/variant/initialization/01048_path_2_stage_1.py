import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the art movements and corresponding data
art_movements = ['Renaissance', 'Baroque', 'Modernism', 'Postmodernism', 'Futurism']
buildings = np.array([500, 300, 800, 350, 150])
years_since_emergence = np.array([600, 400, 100, 50, 30])

# Sort data by years_since_emergence
sorted_indices = np.argsort(years_since_emergence)
years_since_emergence_sorted = years_since_emergence[sorted_indices]
buildings_sorted = buildings[sorted_indices]

# Generate a smooth line fit using B-spline interpolation
x_smooth = np.linspace(years_since_emergence_sorted.min(), years_since_emergence_sorted.max(), 300)
spline = make_interp_spline(years_since_emergence_sorted, buildings_sorted, k=3)
y_smooth = spline(x_smooth)

# Plot the scatter chart with smooth line
plt.figure(figsize=(12, 8))
plt.scatter(years_since_emergence_sorted, buildings_sorted, color='firebrick', s=100, label='Art Movements Influence', zorder=3)
plt.plot(x_smooth, y_smooth, color='darkred', linewidth=2, linestyle='--', label='Trend Line (B-spline Fit)', zorder=2)

# Annotate the points
for i, movement in enumerate(art_movements):
    plt.annotate(movement, (years_since_emergence_sorted[i], buildings_sorted[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9)

# Labels and title
plt.xlabel('Years Since Emergence', fontsize=12)
plt.ylabel('Number of Influenced Buildings', fontsize=12)
plt.title('Cultural Flourish: Influence of Artistic Movements\non Urban Architecture', fontsize=14, weight='bold')

# Add legend, grid, and layout adjustments
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()