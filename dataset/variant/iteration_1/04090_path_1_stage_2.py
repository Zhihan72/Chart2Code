import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

# Constructing the data
years = np.linspace(1800, 2000, 101)
co2_levels_pre_industrial = [280]*20 + [281, 281, 282, 283, 283, 284, 285, 286, 287, 287, 
                                        288, 289, 290, 292, 294, 298, 301, 305, 310, 315] + [320 + i for i in range(61)]

# Plotting the data
fig, axs = plt.subplots(1, 1, figsize=(7, 6))  # Grid of 1 row, 1 column

# Kernel Density Estimation for density plot
density_pre_industrial = kde.gaussian_kde(co2_levels_pre_industrial, bw_method=0.3)
x_range_pre = np.linspace(min(co2_levels_pre_industrial), max(co2_levels_pre_industrial), 300)

# Plotting the density plot for pre-industrial CO2 levels
axs.plot(x_range_pre, density_pre_industrial(x_range_pre), label="Pre-Industrial Era", color='blue')
axs.fill_between(x_range_pre, density_pre_industrial(x_range_pre), color='blue', alpha=0.2)

# Adding titles and labels
axs.set_title('Pre-Industrial Era (1800-1900)', fontsize=13, fontweight='bold')
axs.set_xlabel('CO2 Concentration (ppm)', fontsize=12)
axs.set_ylabel('Density', fontsize=12)
axs.legend(loc='upper left')
axs.grid(True, linestyle='--', alpha=0.5)

# Automatically adjusting layout
plt.tight_layout()

# Display the plot
plt.show()