import matplotlib.pyplot as plt
import numpy as np

# Decades from 1970 to 2020
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Temperature anomalies and CO2 emissions for Polar and Temperate climatic zones
temperature_anomalies_polar = np.array([-0.3, 0.1, 0.5, 1.2, 1.8, 2.5])
temperature_anomalies_temperate = np.array([-0.2, 0.2, 0.6, 1.0, 1.4, 1.9])

co2_emissions_polar = np.array([2100, 2300, 2600, 2900, 3400, 3700])
co2_emissions_temperate = np.array([1800, 2000, 2300, 2700, 3000, 3300])

# Start plotting
fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# Plotting temperature anomalies
axes[0].plot(decades, temperature_anomalies_polar, marker='o', color='b', label='Polar')
axes[0].plot(decades, temperature_anomalies_temperate, marker='o', color='g', label='Temperate')

# Titles, labels, and legend for temperature anomalies plot
axes[0].set_title("Temperature Anomalies (1970-2020)", fontsize=16)
axes[0].set_xlabel("Decades", fontsize=12)
axes[0].set_ylabel("Temperature Anomalies (°C)", fontsize=12)
axes[0].legend(loc="upper left", fontsize=10)
axes[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Plotting CO2 emissions
axes[1].plot(decades, co2_emissions_polar, marker='o', color='b', label='Polar', linestyle='--')
axes[1].plot(decades, co2_emissions_temperate, marker='o', color='g', label='Temperate', linestyle='--')

# Titles, labels, and legend for CO2 emissions plot
axes[1].set_title("CO2 Emissions (1970-2020)", fontsize=16)
axes[1].set_xlabel("Decades", fontsize=12)
axes[1].set_ylabel("CO2 Emissions (Million Metric Tons)", fontsize=12)
axes[1].legend(loc="upper left", fontsize=10)
axes[1].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.suptitle("Climate Change Study: Temperature Anomalies and CO2 Emissions in Polar and Temperate Zones", fontsize=18, fontweight='bold', y=0.95)
plt.tight_layout(rect=[0, 0, 1, 0.93])

# Display the chart
plt.show()