import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kde

# Data setup
years = np.linspace(1800, 2000, 101)
co2_levels = [280]*20 + [281, 281, 282, 283, 283, 284, 285, 286, 287, 287, 
                         288, 289, 290, 292, 294, 298, 301, 305, 310, 315] + [320 + i for i in range(61)]

# Plot setup
fig, ax = plt.subplots(figsize=(7, 6))

# Kernel Density Estimation
density_co2 = kde.gaussian_kde(co2_levels, bw_method=0.3)
x_range = np.linspace(min(co2_levels), max(co2_levels), 300)

# Plotting
ax.plot(density_co2(x_range), x_range, label="Pre-Industrial", color='green')
ax.fill_betweenx(x_range, 0, density_co2(x_range), color='green', alpha=0.2)

# Titles and labels
ax.set_title('Pre-Industrial (1800-1900)', fontsize=13, fontweight='bold')
ax.set_xlabel('Density', fontsize=12)
ax.set_ylabel('CO2 (ppm)', fontsize=12)
ax.legend(loc='upper left')
ax.grid(True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display
plt.show()