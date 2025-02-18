import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data series
tree_heights = np.array([3.2, 4.1, 5.3, 6.5, 5.8, 6.2, 7.1, 8.0, 7.4, 8.5, 9.1, 9.5])
environmental_index = np.array([40, 42, 45, 48, 50, 53, 56, 60, 61, 63, 65, 68])
sunlight_hours = np.array([5, 6, 7, 8, 9, 10, 11, 12, 11, 13, 14, 15])
growth_rates = np.array([30, 35, 37, 40, 38, 39, 42, 45, 43, 47, 50, 52])

# New data series
humidity_levels = np.array([70, 72, 73, 75, 77, 78, 80, 82, 83, 85, 86, 88])
leaf_sizes = np.array([10, 13, 14, 15, 15, 16, 17, 18, 17, 19, 20, 21])

# Creating a spline model for an additional curve
spline_model_humidity = make_interp_spline(humidity_levels, tree_heights)
x_smooth_humidity = np.linspace(humidity_levels.min(), humidity_levels.max(), 300)
y_smooth_humidity = spline_model_humidity(x_smooth_humidity)

fig, axs = plt.subplots(1, 3, figsize=(27, 8))

# Original scatter plot and line
axs[0].scatter(environmental_index, tree_heights, color='forestgreen', s=100)
axs[0].plot(x_smooth, y_smooth, color='royalblue', linewidth=2.5)
axs[0].set_title('Impact of Environmental Conditions\non Tree Growth in a Forest Ecosystem', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Environmental Index', fontsize=14)
axs[0].set_ylabel('Average Tree Height (meters)', fontsize=14)

# Original bar chart
axs[1].bar(sunlight_hours, growth_rates, color='salmon', width=0.6, edgecolor='black')
axs[1].set_title('Influence of Sunlight\non Annual Tree Growth Rates', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Sunlight Hours', fontsize=14)
axs[1].set_ylabel('Growth Rate (cm/year)', fontsize=14)

# New scatter plot and line
axs[2].scatter(humidity_levels, leaf_sizes, color='orchid', s=100)
axs[2].plot(x_smooth_humidity, y_smooth_humidity, color='darkorange', linewidth=2.5)
axs[2].set_title('Relation between Humidity Levels and Tree Leaf Size', fontsize=16, fontweight='bold')
axs[2].set_xlabel('Humidity Level (%)', fontsize=14)
axs[2].set_ylabel('Average Leaf Size (cm^2)', fontsize=14)

plt.tight_layout()
plt.show()