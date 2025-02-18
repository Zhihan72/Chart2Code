import matplotlib.pyplot as plt
import numpy as np

# Decades from 1970 to 2020
decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

# Temperature anomalies (in °C) for each climatic zone
temperature_anomalies_polar = np.array([-0.3, 0.1, 0.5, 1.2, 1.8, 2.5])
temperature_anomalies_temperate = np.array([-0.2, 0.2, 0.6, 1.0, 1.4, 1.9])
temperature_anomalies_tropical = np.array([-0.1, 0.3, 0.7, 1.2, 1.5, 2.1])

# Start plotting
fig, ax = plt.subplots(figsize=(7, 7))

# Plotting temperature anomalies
ax.plot(decades, temperature_anomalies_polar, marker='o', color='b', label='Polar')
ax.plot(decades, temperature_anomalies_temperate, marker='o', color='g', label='Temperate')
ax.plot(decades, temperature_anomalies_tropical, marker='o', color='r', label='Tropical')

# Titles, labels, and legend for temperature anomalies plot
ax.set_title("Temperature Anomalies (1970-2020)", fontsize=16)
ax.set_xlabel("Decades", fontsize=12)
ax.set_ylabel("Temperature Anomalies (°C)", fontsize=12)
ax.legend(loc="upper left", fontsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Adjust layout
plt.suptitle("Climate Change Study: Temperature Anomalies in Different Climatic Zones", fontsize=18, fontweight='bold', y=0.95)
plt.tight_layout(rect=[0, 0, 1, 0.93])

# Display the chart
plt.show()