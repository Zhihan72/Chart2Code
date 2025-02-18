import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

art_movements = ['Postmodernism', 'Modernism', 'Baroque', 'Renaissance']
buildings = np.array([500, 300, 800, 350])
years_since_emergence = np.array([600, 400, 100, 50])

sorted_indices = np.argsort(years_since_emergence)
years_since_emergence_sorted = years_since_emergence[sorted_indices]
buildings_sorted = buildings[sorted_indices]

x_smooth = np.linspace(years_since_emergence_sorted.min(), years_since_emergence_sorted.max(), 300)
spline = make_interp_spline(years_since_emergence_sorted, buildings_sorted, k=3)
y_smooth = spline(x_smooth)

plt.figure(figsize=(12, 8))
plt.scatter(years_since_emergence_sorted, buildings_sorted, color='firebrick', s=100, label='Influence of Art Trends', zorder=3)
plt.plot(x_smooth, y_smooth, color='darkred', linewidth=2, linestyle='--', label='Trend: B-spline Fit', zorder=2)

for i, movement in enumerate(art_movements):
    plt.annotate(movement, (years_since_emergence_sorted[i], buildings_sorted[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9)

plt.xlabel('Time Since Introduction', fontsize=12)
plt.ylabel('Buildings Impacted', fontsize=12)
plt.title('Artistic Waves: Urban Shaping through Time', fontsize=14, weight='bold')

plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.show()