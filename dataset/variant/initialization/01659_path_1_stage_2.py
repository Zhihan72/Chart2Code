import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Existing data
decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
temperature_anomalies = np.array([-0.05, 0.01, 0.12, 0.32, 0.45, 0.63, 0.80])
uncertainties = np.array([0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03])
co2_levels = np.array([320, 325, 340, 355, 370, 385, 410])

# New data: hypothetical greenhouse gas (GHG) emissions (in million metric tons)
ghg_emissions = np.array([10, 15, 18, 20, 23, 27, 29])

norm = mcolors.Normalize(vmin=min(temperature_anomalies), vmax=max(temperature_anomalies))
cmap = cm.viridis

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(decades, temperature_anomalies - uncertainties, temperature_anomalies + uncertainties, 
                color='lightgray', alpha=0.5, label='Uncertainty Range')

shuffled_colors = [cmap(norm(temp)) for temp in reversed(temperature_anomalies)]

for i in range(len(decades) - 1):
    ax.plot(decades[i:i+2], temperature_anomalies[i:i+2], marker='o', 
            color=shuffled_colors[i], markersize=8, linewidth=2)

for decade, anomaly in zip(decades, temperature_anomalies):
    ax.annotate(f'{anomaly:+.2f}°C', xy=(decade, anomaly), xytext=(-5, 10),
                textcoords='offset points', ha='center', fontsize=10, color='darkblue')

ax.set_title('Climate Science Research:\nTemperature Anomalies and GHG Emissions Over Decades (1960-2020)', 
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Temperature Anomaly (°C)', fontsize=12)

ax.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
ax.set_axisbelow(True)
ax.set_yticks(np.arange(-0.2, 1.0, 0.1))

ax.legend(loc='upper left', fontsize=12)

# Additional y-axis for CO2 Levels
ax2 = ax.twinx()
ax2.plot(decades, co2_levels, color='tab:red', linestyle='--', linewidth=2, label='CO2 Levels')
ax2.set_ylabel('CO2 Levels (ppm)', fontsize=12, color='tab:red')
ax2.tick_params(axis='y', labelcolor='tab:red')
ax2.legend(loc='upper right', fontsize=12)

# New plot for GHG Emissions
ax3 = ax.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(decades, ghg_emissions, color='tab:green', linestyle='-', linewidth=2, label='GHG Emissions')
ax3.set_ylabel('GHG Emissions (M metric tons)', fontsize=12, color='tab:green')
ax3.tick_params(axis='y', labelcolor='tab:green')
ax3.legend(loc='upper center', fontsize=12)

plt.tight_layout()
plt.show()