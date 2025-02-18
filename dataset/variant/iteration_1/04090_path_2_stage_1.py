import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

# Constructing the data
years = np.linspace(1800, 2000, 101)
co2_levels_pre_industrial = [280]*20 + [281, 281, 282, 283, 283, 284, 285, 286, 287, 287, 
                                        288, 289, 290, 292, 294, 298, 301, 305, 310, 315] + [320 + i for i in range(61)]
co2_levels_post_industrial = [370 + 2*i for i in range(41)]
# New data for hypothetical future era
co2_levels_future = [450 + 3*i for i in range(41)]

# Merging the data
all_years = np.concatenate((years, np.linspace(2001, 2081, 81)))
all_co2_levels = np.concatenate((co2_levels_pre_industrial, co2_levels_post_industrial, co2_levels_future))

# Plotting the data
fig, ax = plt.subplots(1, 3, figsize=(21, 6))

# KDE calculations
density_pre_industrial = kde.gaussian_kde(co2_levels_pre_industrial, bw_method=0.3)
density_post_industrial = kde.gaussian_kde(co2_levels_post_industrial, bw_method=0.3)
density_future = kde.gaussian_kde(co2_levels_future, bw_method=0.3)

x_range_pre = np.linspace(min(co2_levels_pre_industrial), max(co2_levels_pre_industrial), 300)
x_range_post = np.linspace(min(co2_levels_post_industrial), max(co2_levels_post_industrial), 300)
x_range_future = np.linspace(min(co2_levels_future), max(co2_levels_future), 300)

# Plot 1: Pre-Industrial Era
ax[0].plot(x_range_pre, density_pre_industrial(x_range_pre), label="Pre-Industrial Era", color='blue')
ax[0].fill_between(x_range_pre, density_pre_industrial(x_range_pre), color='blue', alpha=0.2)

# Plot 2: Post-Industrial Era
ax[1].plot(x_range_post, density_post_industrial(x_range_post), label="Post-Industrial Era", color='red')
ax[1].fill_between(x_range_post, density_post_industrial(x_range_post), color='red', alpha=0.2)

# Plot 3: Hypothetical Future Era
ax[2].plot(x_range_future, density_future(x_range_future), label="Hypothetical Future Era", color='green')
ax[2].fill_between(x_range_future, density_future(x_range_future), color='green', alpha=0.2)

# Adding titles and labels
fig.suptitle('Historical and Projected CO2 Concentration Levels\n(1800-2081)', fontsize=16, fontweight='bold')

ax[0].set_title('Pre-Industrial Era (1800-1900)', fontsize=13, fontweight='bold')
ax[0].set_xlabel('CO2 Concentration (ppm)', fontsize=12)
ax[0].set_ylabel('Density', fontsize=12)
ax[0].legend(loc='upper left')
ax[0].grid(True, linestyle='--', alpha=0.5)

ax[1].set_title('Post-Industrial Era (2001-2041)', fontsize=13, fontweight='bold')
ax[1].set_xlabel('CO2 Concentration (ppm)', fontsize=12)
ax[1].set_ylabel('Density', fontsize=12)
ax[1].legend(loc='upper left')
ax[1].grid(True, linestyle='--', alpha=0.5)

ax[2].set_title('Hypothetical Future Era (2041-2081)', fontsize=13, fontweight='bold')
ax[2].set_xlabel('CO2 Concentration (ppm)', fontsize=12)
ax[2].set_ylabel('Density', fontsize=12)
ax[2].legend(loc='upper left')
ax[2].grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plot
plt.show()