import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
temperature_anomalies = np.array([-0.05, 0.01, 0.12, 0.32, 0.45, 0.63, 0.80])
uncertainties = np.array([0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03])
co2_levels = np.array([320, 325, 340, 355, 370, 385, 410])
ghg_emissions = np.array([10, 15, 18, 20, 23, 27, 29])

norm = mcolors.Normalize(vmin=min(temperature_anomalies), vmax=max(temperature_anomalies))
cmap = cm.plasma  # Changed colormap for visual variation

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(decades, temperature_anomalies - uncertainties, temperature_anomalies + uncertainties, 
                color='silver', alpha=0.3)  # Altered color for the fill

shuffled_markers = ['s', 'D', '^', 'v', '<', '>', 'o']  # Different markers for each decade
shuffled_colors = [cmap(norm(temp)) for temp in temperature_anomalies]  # Different order of coloring

for i in range(len(decades) - 1):
    ax.plot(decades[i:i+2], temperature_anomalies[i:i+2], marker=shuffled_markers[i], 
            color=shuffled_colors[i], markersize=10, linewidth=3, linestyle='-.')  # Different linestyle, marker size

ax.grid(False)  # Turned off grid lines for a cleaner background
ax.set_yticks(np.arange(-0.2, 1.0, 0.1))

ax2 = ax.twinx()
ax2.plot(decades, co2_levels, color='tab:blue', linestyle='-', linewidth=3)  # Altered line style and color
ax2.tick_params(axis='y', labelcolor='tab:blue')

ax3 = ax.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(decades, ghg_emissions, color='tab:purple', linestyle=':', linewidth=2)  # Altered line style and color
ax3.tick_params(axis='y', labelcolor='tab:purple')

plt.tight_layout()
plt.show()