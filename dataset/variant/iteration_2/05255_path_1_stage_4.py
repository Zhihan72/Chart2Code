import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2000, 2021)

sea_levels_global = np.array([20, 22, 23, 25, 27, 30, 32, 35, 36, 38, 40, 44, 45, 47, 48, 50, 52, 53, 54, 57, 60])
sea_levels_pacific = np.array([18, 19, 20, 21, 23, 25, 26, 29, 30, 31, 33, 35, 36, 37, 39, 41, 43, 44, 46, 48, 49])
sea_levels_atlantic = np.array([22, 24, 25, 26, 28, 30, 31, 33, 34, 36, 37, 40, 42, 43, 45, 47, 49, 50, 52, 54, 56])
sea_levels_indian = np.array([21, 23, 24, 26, 28, 29, 32, 34, 35, 37, 39, 41, 42, 44, 46, 48, 50, 51, 53, 55, 58])

temp_anomaly = np.array([0.35, 0.38, 0.39, 0.41, 0.45, 0.48, 0.50, 0.52, 0.53, 0.55, 0.57, 0.60, 0.62, 0.65, 0.67, 0.70, 0.72, 0.74, 0.75, 0.77, 0.80])

fig, ax1 = plt.subplots(figsize=(14, 8))

common_color = 'blue'

ax1.plot(years, sea_levels_global, color=common_color, linewidth=2)
ax1.plot(years, sea_levels_pacific, color=common_color, linestyle='--', linewidth=2)
ax1.plot(years, sea_levels_atlantic, color=common_color, linestyle='-.', linewidth=2)
ax1.plot(years, sea_levels_indian, color=common_color, linestyle=':', linewidth=2)

ax1.set_title('Sea Changes Over Time (2000-2020)', fontsize=16, weight='bold')
ax1.set_xlabel('Time (Years)', fontsize=14)
ax1.set_ylabel('Level Rise (Millimeters)', fontsize=14)

ax2 = ax1.twinx()
ax2.plot(years, temp_anomaly, color='orange', linestyle=':', linewidth=2)
ax2.set_ylabel('Temp. Anomaly (Celsius)', fontsize=14, color='orange')

fig.tight_layout()

plt.show()