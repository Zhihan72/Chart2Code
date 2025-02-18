import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

spring_wind_speeds = np.array([3.2, 2.8, 3.5, 4.0, 3.1, 2.7, 3.8, 3.0, 4.2])
summer_wind_speeds = np.array([2.0, 1.8, 2.2, 2.5, 2.5, 1.9, 2.3, 2.4, 2.1])
autumn_wind_speeds = np.array([4.5, 4.3, 4.6, 5.0, 4.8, 4.7, 4.4, 4.9, 5.1])
winter_wind_speeds = np.array([5.5, 5.2, 5.8, 6.0, 5.6, 5.4, 5.7, 5.3, 6.2])

# Define a figure for multiple subplots
fig, ax = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']
wind_speed_data = [spring_wind_speeds, summer_wind_speeds, autumn_wind_speeds, winter_wind_speeds]

# New set of colors for the density plots
new_colors = ['purple', 'cyan', 'magenta', 'lime']

for i, (ax_, season, data, color) in enumerate(zip(ax.flatten(), seasons, wind_speed_data, new_colors)):
    density = gaussian_kde(data)
    x_vals = np.linspace(0, 7, 200)
    y_vals = density(x_vals)

    ax_.plot(x_vals, y_vals, color=color, label=f'{season}')
    ax_.fill_between(x_vals, 0, y_vals, color=color, alpha=0.3)
    ax_.set_title(f'{season} Wind Speed Density', fontsize=12, fontweight='bold')
    ax_.set_xlabel('Wind Speed (m/s)', fontsize=10)
    ax_.set_ylabel('Density', fontsize=10)
    ax_.legend(loc='upper right')
    ax_.grid(True, linestyle='--', linewidth=0.6, alpha=0.7)

fig.suptitle("Wind Speeds in Urban Microclimates: Seasonal Variations", fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()