import matplotlib.pyplot as plt
import numpy as np

# Data
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
gulf_stream = np.array([5, 12, 20, 25, 35, 45, 60, 75])
kuroshio_current = np.array([3, 10, 15, 22, 30, 40, 55, 70])
antarctic_circumpolar = np.array([4, 9, 17, 22, 32, 42, 58, 68])
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])

# Plot setup
fig, ax1 = plt.subplots(figsize=(12, 8))
ax1.plot(decades, gulf_stream, marker='o', linestyle='-', color='b', linewidth=2, label='Gulf Stream')
ax1.plot(decades, kuroshio_current, marker='s', linestyle='--', color='g', linewidth=2, label='Kuroshio')
ax1.plot(decades, antarctic_circumpolar, marker='^', linestyle=':', color='r', linewidth=2, label='ACC')

# Second axis for bar chart
ax2 = ax1.twinx()
bar_width = 8
ax2.bar(decades - bar_width / 2, sea_surface_temp, width=bar_width, color='orange', alpha=0.5)

# Labels
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Intensity', fontsize=12)
ax2.set_ylabel('Temp (°C)', fontsize=12)

# Legend
ax1.legend(loc="upper left")

# Adjust layout
plt.tight_layout()
plt.show()