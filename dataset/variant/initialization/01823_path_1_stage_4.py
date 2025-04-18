import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

star_ages = np.array([1.5, 2.0, 4.1, 5.5, 6.3, 7.9, 8.5, 9.1, 10.4, 11.2, 12.6, 13.3, 14.5, 15.0, 16.1])
exoplanets_count = np.array([2, 3, 4, 6, 5, 8, 7, 7, 9, 8, 10, 11, 13, 12, 14])
brightness = np.array([15, 20, 35, 40, 45, 60, 65, 50, 70, 80, 95, 90, 105, 110, 120])

star_ages_group2 = np.array([1.0, 2.5, 3.0, 4.5, 5.8, 6.7, 7.0, 8.3, 9.6, 10.5, 11.8, 12.5, 13.1, 15.5, 16.5])
exoplanets_count_group2 = np.array([1, 2, 3, 5, 4, 6, 7, 6, 7, 7, 9, 10, 11, 11, 13])
brightness_group2 = np.array([10, 18, 30, 38, 42, 58, 60, 48, 66, 76, 90, 89, 103, 112, 117])

colors1 = plt.cm.plasma((star_ages - star_ages.min()) / (star_ages.max() - star_ages.min()))
colors2 = plt.cm.viridis((star_ages_group2 - star_ages_group2.min()) / (star_ages_group2.max() - star_ages_group2.min()))

fig, ax1 = plt.subplots(figsize=(12, 8))

ax1.scatter(star_ages, exoplanets_count, s=brightness*10, c=colors1, alpha=0.7, edgecolors='w', linewidth=0.5)

ax1.scatter(star_ages_group2, exoplanets_count_group2, s=brightness_group2*10, c=colors2, alpha=0.7, edgecolors='gray', linewidth=0.5, marker='s')

ax1.set_xlabel('Age (B Years)', fontsize=12)
ax1.set_ylabel('Exoplanets', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()

x_smooth1 = np.linspace(star_ages.min(), star_ages.max(), 300)
spl1 = make_interp_spline(star_ages, brightness, k=3)
brightness_smooth1 = spl1(x_smooth1)
ax2.plot(x_smooth1, brightness_smooth1, color='orange', linewidth=2, linestyle='--')

x_smooth2 = np.linspace(star_ages_group2.min(), star_ages_group2.max(), 300)
spl2 = make_interp_spline(star_ages_group2, brightness_group2, k=3)
brightness_smooth2 = spl2(x_smooth2)
ax2.plot(x_smooth2, brightness_smooth2, color='green', linewidth=2, linestyle=':')

ax2.set_ylabel('Brightness', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

plt.title('Star Age vs. Exoplanets with Additional Data Series', fontsize=16, fontweight='bold')

plt.show()