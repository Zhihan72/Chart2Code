import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

temperature_anomalies_polar = np.array([-0.3, 0.1, 0.5, 1.2, 1.8, 2.5])
temperature_anomalies_temperate = np.array([-0.2, 0.2, 0.6, 1.0, 1.4, 1.9])

co2_emissions_polar = np.array([2100, 2300, 2600, 2900, 3400, 3700])
co2_emissions_temperate = np.array([1800, 2000, 2300, 2700, 3000, 3300])

fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Temperature anomalies plot
axes[0].plot(decades, temperature_anomalies_polar, marker='x', color='cyan', linestyle='-', label='Arctic Zone')
axes[0].plot(decades, temperature_anomalies_temperate, marker='D', color='magenta', linestyle=':', label='Mid-latitude Zone')
axes[0].set_title("Temperature Changes (1970-2020)", fontsize=15)
axes[0].set_xlabel("Years", fontsize=11)
axes[0].set_ylabel("Temperature Change (°C)", fontsize=11)
axes[0].legend(loc="lower right", fontsize=10)
axes[0].grid(True, linestyle='-.', linewidth=0.6, alpha=0.3)

# CO2 emissions plot
axes[1].plot(decades, co2_emissions_polar, marker='s', color='brown', linestyle='-.', label='Arctic', linewidth=1.5)
axes[1].plot(decades, co2_emissions_temperate, marker='^', color='orange', linestyle='-', label='Mid-latitude', linewidth=1.5)
axes[1].set_title("CO2 Emissions (1970-2020)", fontsize=15)
axes[1].set_xlabel("Time", fontsize=11)
axes[1].set_ylabel("CO2 Emissions (Mt)", fontsize=11)
axes[1].legend(loc="upper right", fontsize=10)
axes[1].grid(False)  # Removed grid

plt.suptitle("Arctic & Mid-latitudes: Climate Change Overview", fontsize=17, fontweight='bold', color='purple', y=0.96)
plt.tight_layout(rect=[0, 0, 1, 0.94])

plt.show()