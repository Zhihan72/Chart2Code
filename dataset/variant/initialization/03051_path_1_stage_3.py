import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

tree_heights = np.array([3.2, 4.1, 5.3, 6.5, 5.8, 6.2, 7.1, 8.0, 7.4, 8.5, 9.1, 9.5])
environmental_index = np.array([40, 42, 45, 48, 50, 53, 56, 60, 61, 63, 65, 68])

sunlight_hours = np.array([5, 6, 7, 8, 9, 10, 11, 12, 11, 13, 14, 15])
growth_rates = np.array([30, 35, 37, 40, 38, 39, 42, 45, 43, 47, 50, 52])

soil_moisture = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
nutrient_absorption = np.array([2, 3, 4.5, 5, 6, 6.5, 7.5, 8, 8.5, 9, 9.5, 10])

spline_model = make_interp_spline(environmental_index, tree_heights)
x_smooth = np.linspace(environmental_index.min(), environmental_index.max(), 300)
y_smooth = spline_model(x_smooth)

fig, axs = plt.subplots(1, 3, figsize=(24, 8))

axs[0].scatter(environmental_index, tree_heights, color='darkorange', s=100, label='Height Observations')
axs[0].plot(x_smooth, y_smooth, color='navy', linewidth=2.5, label='Spline Trendline')
axs[0].set_title('Ecological Influences on Tree Height', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Eco Index', fontsize=14)
axs[0].set_ylabel('Tree Height (m)', fontsize=14)
axs[0].legend(loc='upper left', fontsize=12, frameon=True)
axs[0].grid(True, linestyle='--', alpha=0.5)

axs[1].bar(sunlight_hours, growth_rates, color='teal', width=0.6, edgecolor='black', label='Expansion Rates')
axs[1].set_title('Sunlight Impact on Plant Growth', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Light Hours', fontsize=14)
axs[1].set_ylabel('Expansion Rate (cm/year)', fontsize=14)
axs[1].legend(loc='upper left', fontsize=12, frameon=True)
axs[1].grid(True, linestyle='--', alpha=0.5)

axs[2].plot(soil_moisture, nutrient_absorption, marker='o', linestyle='-', color='darkred', label='Uptake Efficiency')
axs[2].set_title('Moisture Influence on Nutrient Uptake', fontsize=16, fontweight='bold')
axs[2].set_xlabel('Moisture Level (%)', fontsize=14)
axs[2].set_ylabel('Uptake Efficiency (units)', fontsize=14)
axs[2].legend(loc='upper left', fontsize=12, frameon=True)
axs[2].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()