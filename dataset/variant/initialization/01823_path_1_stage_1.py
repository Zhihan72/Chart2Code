import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data preparation
star_ages = np.array([1.5, 2.0, 4.1, 5.5, 6.3, 7.9, 8.5, 9.1, 10.4, 11.2, 12.6, 13.3, 14.5, 15.0, 16.1])
exoplanets_count = np.array([2, 3, 4, 6, 5, 8, 7, 7, 9, 8, 10, 11, 13, 12, 14])
brightness = np.array([15, 20, 35, 40, 45, 60, 65, 50, 70, 80, 95, 90, 105, 110, 120])

colors = plt.cm.viridis((star_ages - star_ages.min()) / (star_ages.max() - star_ages.min()))

fig, ax1 = plt.subplots(figsize=(12, 8))

scatter = ax1.scatter(star_ages, exoplanets_count, s=brightness*10, c=colors, alpha=0.7, edgecolors='w', linewidth=0.5)
ax1.set_xlabel('Age (B Years)', fontsize=12)
ax1.set_ylabel('Exoplanets', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
x_smooth = np.linspace(star_ages.min(), star_ages.max(), 300)
spl = make_interp_spline(star_ages, brightness, k=3)
brightness_smooth = spl(x_smooth)
ax2.plot(x_smooth, brightness_smooth, color='orange', linewidth=2, linestyle='--')
ax2.set_ylabel('Brightness', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

plt.title('Star Age vs. Exoplanets', fontsize=16, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.6)

cbar = plt.colorbar(scatter, ax=ax1, orientation='vertical', fraction=0.05, pad=0.04)
cbar.set_label('Age (B Years)', fontsize=10)

ax1.annotate('Older stars,\nmore planets', xy=(12, 10), xytext=(14, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=10)

fig.tight_layout()

plt.show()