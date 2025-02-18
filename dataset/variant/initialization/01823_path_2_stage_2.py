import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data preparation
star_ages = np.array([1.5, 2.0, 4.1, 5.5, 6.3, 7.9, 8.5, 9.1, 10.4, 11.2, 12.6, 13.3, 14.5, 15.0, 16.1])
exoplanets_count = np.array([2, 3, 4, 6, 5, 8, 7, 7, 9, 8, 10, 11, 13, 12, 14])
brightness = np.array([15, 20, 35, 40, 45, 60, 65, 50, 70, 80, 95, 90, 105, 110, 120])
galactic_temperature = np.array([3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800])

colors = plt.cm.viridis((star_ages - star_ages.min()) / (star_ages.max() - star_ages.min()))

fig, ax1 = plt.subplots(figsize=(12, 8))

scatter = ax1.scatter(star_ages, exoplanets_count, s=brightness*10, c=colors, alpha=0.7, edgecolors='w', linewidth=0.5)
ax1.set_xlabel('tSra gaeA (illnoBi sraeY)', fontsize=12)
ax1.set_ylabel('oNremu fo eincdrofm xEoanltpse', fontsize=12, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
x_smooth = np.linspace(star_ages.min(), star_ages.max(), 300)
spl = make_interp_spline(star_ages, brightness, k=3)
brightness_smooth = spl(x_smooth)
ax2.plot(x_smooth, brightness_smooth, color='orange', linewidth=2, linestyle='--')
ax2.set_ylabel('SartrBhgis nte (tryArabutia stUni)', fontsize=12, color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
x_smooth_temp = np.linspace(star_ages.min(), star_ages.max(), 300)
spl_temp = make_interp_spline(star_ages, galactic_temperature, k=3)
temp_smooth = spl_temp(x_smooth_temp)
ax3.plot(x_smooth_temp, temp_smooth, color='green', linewidth=2, linestyle='-')
ax3.set_ylabel('laGciatTm ueprtaRet (K)', fontsize=12, color='green')
ax3.tick_params(axis='y', labelcolor='green')

title = ('Satr AegE, tonplExae atCnuo, tsBerginhss, dna ticGalata erumpeTraet\n'
         'tsIgisnnht fo calhyHepot tiStar msyeStes')
plt.title(title, fontsize=16, fontweight='bold')
ax1.grid(True, linestyle='--', alpha=0.6)
cbar = plt.colorbar(scatter, ax=ax1, orientation='vertical', fraction=0.05, pad=0.04)
cbar.set_label('trsA geaS (Bililon esYar)', fontsize=10)

ax1.annotate('dOlder strasim etsh\naveo mre xpoaeltepsn', xy=(12, 10), xytext=(14, 5),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=10)

fig.tight_layout()

plt.show()