import matplotlib.pyplot as plt
import numpy as np

decades = np.array([1970, 1980, 1990, 2000, 2010, 2020])

temperature_anomalies_polar = np.array([-0.3, 0.1, 0.5, 1.2, 1.8, 2.5])
temperature_anomalies_temperate = np.array([-0.2, 0.2, 0.6, 1.0, 1.4, 1.9])
temperature_anomalies_tropical = np.array([-0.1, 0.3, 0.7, 1.2, 1.5, 2.1])

fig, ax = plt.subplots(figsize=(7, 7))

ax.plot(decades, temperature_anomalies_polar, marker='o', color='b', label='Polar')
ax.plot(decades, temperature_anomalies_temperate, marker='o', color='g', label='Temperate')
ax.plot(decades, temperature_anomalies_tropical, marker='o', color='r', label='Tropical')

ax.set_title("Temp Anomalies (1970-2020)", fontsize=16)
ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Temp Anomalies (°C)", fontsize=12)
ax.legend(loc="upper left", fontsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.suptitle("Climate Study: Temp in Zones", fontsize=18, fontweight='bold', y=0.95)
plt.tight_layout(rect=[0, 0, 1, 0.93])

plt.show()