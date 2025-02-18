import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

art_movements = ['Postmodernism', 'Modernism', 'Baroque', 'Futurism', 'Renaissance']
buildings = np.array([300, 800, 150, 500, 350])
years_since_emergence = np.array([400, 100, 30, 600, 50])

sorted_indices = np.argsort(years_since_emergence)
years_since_emergence_sorted = years_since_emergence[sorted_indices]
buildings_sorted = buildings[sorted_indices]

x_smooth = np.linspace(years_since_emergence_sorted.min(), years_since_emergence_sorted.max(), 300)
spline = make_interp_spline(years_since_emergence_sorted, buildings_sorted, k=3)
y_smooth = spline(x_smooth)

plt.figure(figsize=(12, 8))
single_color = 'teal'
plt.scatter(years_since_emergence_sorted, buildings_sorted, color=single_color, s=100, label='Architectural Roles', zorder=3)
plt.plot(x_smooth, y_smooth, color=single_color, linewidth=2, linestyle='--', label='Historical Path (B-spline Fit)', zorder=2)

for i, movement in enumerate(art_movements):
    plt.annotate(movement, (years_since_emergence_sorted[i], buildings_sorted[i]), textcoords="offset points", xytext=(-10,10), ha='center', fontsize=9)

plt.xlabel('Time Gap Since Origin', fontsize=12) 
plt.ylabel('Count of Affected Structures', fontsize=12)
plt.title('Evolvement in Design: Art Impact on Cityscapes', fontsize=14, weight='bold')
plt.legend(loc='upper right', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()