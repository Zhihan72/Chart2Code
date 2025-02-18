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
single_color = 'orange'
plt.scatter(years_since_emergence_sorted, buildings_sorted, color=single_color, s=70, label='Architectural Influences', marker='s', zorder=3)
plt.plot(x_smooth, y_smooth, color='blue', linewidth=3, linestyle=':', label='Artistic Trajectory (B-spline)', zorder=2)

for i, movement in enumerate(art_movements):
    plt.annotate(movement, (years_since_emergence_sorted[i], buildings_sorted[i]), textcoords="offset points",
                 xytext=(-5, 5), ha='right', fontsize=10, color='green')

plt.xlabel('Time Since Origin (years)', fontsize=13, color='purple') 
plt.ylabel('Number of Affected Structures', fontsize=13, color='purple')
plt.title('Art Movements and their Influence on Architecture', fontsize=16, weight='bold', color='darkred')

plt.legend(loc='upper left', fontsize=11, frameon=False)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()