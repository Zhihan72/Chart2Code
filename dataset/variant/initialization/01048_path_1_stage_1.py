import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Define the art movements and corresponding data
art_movements = ['Postmodernism', 'Modernism', 'Baroque', 'Futurism', 'Renaissance'] # shuffled
buildings = np.array([500, 300, 800, 350, 150])
years_since_emergence = np.array([600, 400, 100, 50, 30])

# Sort the arrays by years_since_emergence to ensure they are strictly increasing
sorted_indices = np.argsort(years_since_emergence)
years_since_emergence_sorted = years_since_emergence[sorted_indices]
buildings_sorted = buildings[sorted_indices]

# Generate a smooth line fit using B-spline interpolation
x_smooth = np.linspace(years_since_emergence_sorted.min(), years_since_emergence_sorted.max(), 300)
spline = make_interp_spline(years_since_emergence_sorted, buildings_sorted, k=3)  # B-spline with degree 3
y_smooth = spline(x_smooth)

# Plotting the scatter chart with smooth fitting line
plt.figure(figsize=(12, 8))
plt.scatter(years_since_emergence_sorted, buildings_sorted, color='royalblue', s=100, label='Architectural Roles', zorder=3) # changed
plt.plot(x_smooth, y_smooth, color='navy', linewidth=2, linestyle='--', label='Historical Path (B-spline Fit)', zorder=2) # changed

# Annotate the points for clarity
for i, movement in enumerate(art_movements):
    plt.annotate(movement, (years_since_emergence_sorted[i], buildings_sorted[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9)

# Setting labels and title
plt.xlabel('Time Gap Since Origin', fontsize=12) # changed
plt.ylabel('Count of Affected Structures', fontsize=12) # changed
plt.title('Evolvement in Design: Art Impact on Cityscapes', fontsize=14, weight='bold') # changed

# Add a legend
plt.legend(loc='upper right', fontsize=10)

# Grid and layout adjustments
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Display the plot
plt.show()