import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Original data: Average tree heights (in meters) and corresponding environmental index values
tree_heights = np.array([3.2, 4.1, 5.3, 6.5, 5.8, 6.2, 7.1, 8.0, 7.4, 8.5, 9.1, 9.5])
environmental_index = np.array([40, 42, 45, 48, 50, 53, 56, 60, 61, 63, 65, 68])

# New synthetic data: Hours of sunlight vs growth rates (in cm/year)
sunlight_hours = np.array([5, 6, 7, 8, 9, 10, 11, 12, 11, 13, 14, 15])
growth_rates = np.array([30, 35, 37, 40, 38, 39, 42, 45, 43, 47, 50, 52])

# Additional synthetic data: Soil moisture (in %) vs nutrient absorption rates (arbitrary units)
soil_moisture = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
nutrient_absorption = np.array([2, 3, 4.5, 5, 6, 6.5, 7.5, 8, 8.5, 9, 9.5, 10])

# Spline interpolation for smooth curve of the original data
spline_model = make_interp_spline(environmental_index, tree_heights)
x_smooth = np.linspace(environmental_index.min(), environmental_index.max(), 300)
y_smooth = spline_model(x_smooth)

# Initialize the figure with 1x3 subplot structure
fig, axs = plt.subplots(1, 3, figsize=(24, 8))

# First subplot: Environmental Index vs. Tree Heights
axs[0].scatter(environmental_index, tree_heights, color='forestgreen', s=100, label='Measured Tree Heights')
axs[0].plot(x_smooth, y_smooth, color='royalblue', linewidth=2.5, label='Trend Line (Spline Fit)')
axs[0].set_title('Impact of Environmental Conditions\non Tree Growth in a Forest Ecosystem', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Environmental Index', fontsize=14)
axs[0].set_ylabel('Average Tree Height (meters)', fontsize=14)
axs[0].legend(loc='upper left', fontsize=12, frameon=True)
axs[0].grid(True, linestyle='--', alpha=0.5)

# Second subplot: Sunlight Hours vs. Growth Rates
axs[1].bar(sunlight_hours, growth_rates, color='salmon', width=0.6, edgecolor='black', label='Growth Rates')
axs[1].set_title('Influence of Sunlight\non Annual Tree Growth Rates', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Sunlight Hours', fontsize=14)
axs[1].set_ylabel('Growth Rate (cm/year)', fontsize=14)
axs[1].legend(loc='upper left', fontsize=12, frameon=True)
axs[1].grid(True, linestyle='--', alpha=0.5)

# Third subplot: Soil Moisture vs. Nutrient Absorption Rates
axs[2].plot(soil_moisture, nutrient_absorption, marker='o', linestyle='-', color='deepskyblue', label='Nutrient Absorption')
axs[2].set_title('Effect of Soil Moisture\non Nutrient Absorption', fontsize=16, fontweight='bold')
axs[2].set_xlabel('Soil Moisture (%)', fontsize=14)
axs[2].set_ylabel('Nutrient Absorption (units)', fontsize=14)
axs[2].legend(loc='upper left', fontsize=12, frameon=True)
axs[2].grid(True, linestyle='--', alpha=0.5)

# Adjust the layout to prevent overlapping of elements
plt.tight_layout()

# Display the plot
plt.show()