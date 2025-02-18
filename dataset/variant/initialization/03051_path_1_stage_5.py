import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

tree_heights = np.array([3.2, 4.1, 5.3, 6.5, 5.8, 6.2, 7.1, 8.0, 7.4, 8.5, 9.1, 9.5])
environmental_index = np.array([40, 42, 45, 48, 50, 53, 56, 60, 61, 63, 65, 68])

sunlight_hours = np.array([5, 6, 7, 8, 9, 10, 11, 12, 11, 13, 14, 15])
growth_rates = np.array([30, 35, 37, 40, 38, 39, 42, 45, 43, 47, 50, 52])

spline_model = make_interp_spline(environmental_index, tree_heights)
x_smooth = np.linspace(environmental_index.min(), environmental_index.max(), 300)
y_smooth = spline_model(x_smooth)

fig, axs = plt.subplots(1, 2, figsize=(16, 8))

axs[0].scatter(environmental_index, tree_heights, color='purple', s=100, label='Height Observations')
axs[0].plot(x_smooth, y_smooth, color='orange', linewidth=2, linestyle='--', label='Spline Trendline')
axs[0].set_title('Ecological Influences on Tree Height', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Eco Index', fontsize=14)
axs[0].set_ylabel('Tree Height (m)', fontsize=14)
axs[0].legend(loc='lower right', fontsize=12, frameon=False)
axs[0].grid(False)

axs[1].bar(sunlight_hours, growth_rates, color='maroon', width=0.3, edgecolor='green', label='Expansion Rates')
axs[1].set_title('Sunlight Impact on Plant Growth', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Light Hours', fontsize=14)
axs[1].set_ylabel('Growth Rate (cm/year)', fontsize=14)
axs[1].legend(loc='lower right', fontsize=12, frameon=False)
axs[1].get_yaxis().grid(True, linestyle='-', color='gray', linewidth=0.7, alpha=0.7)
axs[1].set_axisbelow(True)

plt.tight_layout()
plt.show()