import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

years = np.linspace(1800, 2000, 101)
co2_levels_pre_industrial = [280]*20 + [281, 281, 282, 283, 283, 284, 285, 286, 287, 287, 
                                        288, 289, 290, 292, 294, 298, 301, 305, 310, 315] + [320 + i for i in range(61)]
co2_levels_post_industrial = [370 + 2*i for i in range(41)]
co2_levels_future = [450 + 3*i for i in range(41)]

all_years = np.concatenate((years, np.linspace(2001, 2081, 81)))
all_co2_levels = np.concatenate((co2_levels_pre_industrial, co2_levels_post_industrial, co2_levels_future))

fig, ax = plt.subplots(1, 3, figsize=(21, 6))

density_pre_industrial = kde.gaussian_kde(co2_levels_pre_industrial, bw_method=0.3)
density_post_industrial = kde.gaussian_kde(co2_levels_post_industrial, bw_method=0.3)
density_future = kde.gaussian_kde(co2_levels_future, bw_method=0.3)

x_range_pre = np.linspace(min(co2_levels_pre_industrial), max(co2_levels_pre_industrial), 300)
x_range_post = np.linspace(min(co2_levels_post_industrial), max(co2_levels_post_industrial), 300)
x_range_future = np.linspace(min(co2_levels_future), max(co2_levels_future), 300)

# Plot 1: Pre-Industrial Era
ax[0].plot(x_range_pre, density_pre_industrial(x_range_pre), label="Era of Stable CO2", color='green', linestyle='-.')
ax[0].fill_between(x_range_pre, density_pre_industrial(x_range_pre), color='green', alpha=0.3)
ax[0].set_title('1800s Stability', fontsize=13, fontweight='bold')
ax[0].set_xlabel('Concentration of CO2 in Air (ppm)', fontsize=12)
ax[0].set_ylabel('Density Measurement', fontsize=12)
ax[0].legend(loc='lower right')
ax[0].grid(True, linestyle='-', linewidth=0.5)

# Plot 2: Post-Industrial Era
ax[1].plot(x_range_post, density_post_industrial(x_range_post), label="CO2 Surge Era", color='red', marker='o')
ax[1].fill_between(x_range_post, density_post_industrial(x_range_post), color='red', alpha=0.25)
ax[1].set_title('2001-2041 Surge', fontsize=13, fontweight='bold')
ax[1].set_xlabel('Atmospheric CO2 (ppm)', fontsize=12)
ax[1].set_ylabel('Measured Density', fontsize=12)
ax[1].legend(loc='upper right')
ax[1].grid(True, linestyle=':', color='gray')

# Plot 3: Hypothetical Future Era
ax[2].plot(x_range_future, density_future(x_range_future), label="Future Speculation Era", color='purple', linestyle='--', marker='x')
ax[2].fill_between(x_range_future, density_future(x_range_future), color='purple', alpha=0.2)
ax[2].set_title('Guesswork Future (2041-2081)', fontsize=13, fontweight='bold')
ax[2].set_xlabel('Projected CO2 Levels (ppm)', fontsize=12)
ax[2].set_ylabel('Estimated Density', fontsize=12)
ax[2].legend(loc='lower left')
ax[2].grid(True, linestyle='-.', color='black', alpha=0.3)

fig.suptitle('Projection of CO2 Density Patterns\n(1800-2081)', fontsize=16, fontweight='bold')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()