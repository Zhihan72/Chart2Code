import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

decades = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
temperature_anomalies = np.array([-0.05, 0.01, 0.12, 0.32, 0.45, 0.63, 0.80])
uncertainties = np.array([0.1, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03])

# Swapping colormap for a shuffled effect
shuffled_colors = ['aqua', 'orange', 'darkgreen', 'darkblue', 'lime', 'red', 'blue']

fig, ax = plt.subplots(figsize=(12, 8))

ax.fill_between(decades, temperature_anomalies - uncertainties, temperature_anomalies + uncertainties, 
                color='khaki', alpha=0.3, label='Unc.')

for i in range(len(decades) - 1):
    ax.plot(decades[i:i+2], temperature_anomalies[i:i+2], marker='s', 
            color=shuffled_colors[i], markersize=10, linewidth=3, linestyle='-.')

for decade, anomaly in zip(decades, temperature_anomalies):
    ax.annotate(f'{anomaly:+.2f}°C', xy=(decade, anomaly), xytext=(-5, -15),
                textcoords='offset points', ha='center', fontsize=10, color='black')

ax.set_title('Temp. Anomalies', fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Temp. Anomaly (°C)', fontsize=12)

ax.grid(True, which='both', linestyle='-', linewidth=0.3, alpha=0.5)
ax.set_axisbelow(True)

ax.set_yticks(np.arange(-0.2, 1.0, 0.1))

ax.legend(loc='lower right', fontsize=10)

co2_levels = np.array([320, 326, 342, 356, 371, 389, 412])
ax2 = ax.twinx()

# Changing color for the CO2 line as well
ax2.plot(decades, co2_levels, color='brown', linestyle=':', linewidth=2, label='CO2')
ax2.set_ylabel('CO2 (ppm)', fontsize=12, color='brown')
ax2.tick_params(axis='y', labelcolor='brown')
ax2.legend(loc='upper center', fontsize=10)

plt.tight_layout()
plt.show()