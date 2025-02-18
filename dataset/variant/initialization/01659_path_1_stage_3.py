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
cmap = cm.viridis

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(decades, temperature_anomalies - uncertainties, temperature_anomalies + uncertainties, 
                color='lightgray', alpha=0.5)

shuffled_colors = [cmap(norm(temp)) for temp in reversed(temperature_anomalies)]

for i in range(len(decades) - 1):
    ax.plot(decades[i:i+2], temperature_anomalies[i:i+2], marker='o', 
            color=shuffled_colors[i], markersize=8, linewidth=2)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.set_yticks(np.arange(-0.2, 1.0, 0.1))

# Additional y-axis for CO2 Levels
ax2 = ax.twinx()
ax2.plot(decades, co2_levels, color='tab:red', linestyle='--', linewidth=2)
ax2.tick_params(axis='y', labelcolor='tab:red')

# New plot for GHG Emissions
ax3 = ax.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(decades, ghg_emissions, color='tab:green', linestyle='-', linewidth=2)
ax3.tick_params(axis='y', labelcolor='tab:green')

plt.tight_layout()
plt.show()