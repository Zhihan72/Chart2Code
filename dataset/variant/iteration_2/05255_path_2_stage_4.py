import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2000, 2021)
sea_levels_global = np.array([20, 22, 23, 25, 27, 30, 32, 35, 36, 38, 40, 44, 45, 47, 48, 50, 52, 53, 54, 57, 60])
sea_levels_atlantic = np.array([22, 24, 25, 26, 28, 30, 31, 33, 34, 36, 37, 40, 42, 43, 45, 47, 49, 50, 52, 54, 56])
temp_anomaly = np.array([0.35, 0.38, 0.39, 0.41, 0.45, 0.48, 0.50, 0.52, 0.53, 0.55, 0.57, 0.60, 0.62, 0.65, 0.67, 0.70, 0.72, 0.74, 0.75, 0.77, 0.80])

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, sea_levels_global, color='purple', marker='o', label='Global SL', linewidth=1)
ax1.plot(years, sea_levels_atlantic, color='green', linestyle='--', marker='x', label='Atlantic SL', linewidth=3)

ax1.set_title('Climate Impact on Sea Levels', fontsize=16, weight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Sea Level (mm)', fontsize=14)

ax1.grid(True, linestyle='-', alpha=0.7)
ax1.legend(loc='lower right', fontsize=12)

ax2 = ax1.twinx()
ax2.plot(years, temp_anomaly, color='brown', linestyle='-', marker='s', label='Temp Anomaly', linewidth=2)

ax2.set_ylabel('Temp Anomaly (°C)', fontsize=14, color='brown')

fig.tight_layout()
plt.show()