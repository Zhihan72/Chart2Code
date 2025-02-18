import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Data series
tree_heights = np.array([3.2, 4.1, 5.3, 6.5, 5.8, 6.2, 7.1, 8.0, 7.4, 8.5, 9.1, 9.5])
environmental_index = np.array([40, 42, 45, 48, 50, 53, 56, 60, 61, 63, 65, 68])
sunlight_hours = np.array([5, 6, 7, 8, 9, 10, 11, 12, 11, 13, 14, 15])
growth_rates = np.array([30, 35, 37, 40, 38, 39, 42, 45, 43, 47, 50, 52])
humidity_levels = np.array([70, 72, 73, 75, 77, 78, 80, 82, 83, 85, 86, 88])
leaf_sizes = np.array([10, 13, 14, 15, 15, 16, 17, 18, 17, 19, 20, 21])

# Spline model for humidity
spline_model_humidity = make_interp_spline(humidity_levels, tree_heights)
x_smooth_humidity = np.linspace(humidity_levels.min(), humidity_levels.max(), 300)
y_smooth_humidity = spline_model_humidity(x_smooth_humidity)

fig, axs = plt.subplots(1, 3, figsize=(27, 8))

# Using the same color 'forestgreen' for all plots
axs[0].scatter(environmental_index, tree_heights, color='forestgreen', s=100)
axs[0].set_title('Env Index vs. Tree Height', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Env Index', fontsize=14)
axs[0].set_ylabel('Height (m)', fontsize=14)

axs[1].bar(sunlight_hours, growth_rates, color='forestgreen', width=0.6, edgecolor='black')
axs[1].set_title('Sunlight vs. Growth Rates', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Sunlight (hrs)', fontsize=14)
axs[1].set_ylabel('Growth (cm/yr)', fontsize=14)

axs[2].scatter(humidity_levels, leaf_sizes, color='forestgreen', s=100)
axs[2].set_title('Humidity vs. Leaf Size', fontsize=16, fontweight='bold')
axs[2].set_xlabel('Humidity (%)', fontsize=14)
axs[2].set_ylabel('Leaf Size (cm²)', fontsize=14)

plt.tight_layout()
plt.show()