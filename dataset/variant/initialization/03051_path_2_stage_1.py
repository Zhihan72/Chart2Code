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

fig, axs = plt.subplots(1, 2, figsize=(18, 8))

axs[0].scatter(environmental_index, tree_heights, color='forestgreen', s=100)
axs[0].plot(x_smooth, y_smooth, color='royalblue', linewidth=2.5)
axs[0].set_title('Impact of Environmental Conditions\non Tree Growth in a Forest Ecosystem', fontsize=16, fontweight='bold')
axs[0].set_xlabel('Environmental Index', fontsize=14)
axs[0].set_ylabel('Average Tree Height (meters)', fontsize=14)

axs[1].bar(sunlight_hours, growth_rates, color='salmon', width=0.6, edgecolor='black')
axs[1].set_title('Influence of Sunlight\non Annual Tree Growth Rates', fontsize=16, fontweight='bold')
axs[1].set_xlabel('Sunlight Hours', fontsize=14)
axs[1].set_ylabel('Growth Rate (cm/year)', fontsize=14)

plt.tight_layout()
plt.show()