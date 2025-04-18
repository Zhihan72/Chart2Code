import matplotlib.pyplot as plt
import numpy as np

# Data
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
gulf_stream = np.array([5, 12, 20, 25, 35, 45, 60, 75])
kuroshio_current = np.array([3, 10, 15, 22, 30, 40, 55, 70])
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])

# Plot setup as horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))
bar_height = 1.0

# Plot horizontal bars for each dataset with new colors
ax.barh(decades - bar_height, gulf_stream, height=bar_height, color='red', alpha=0.6, label='Gulf Stream')
ax.barh(decades, kuroshio_current, height=bar_height, color='cyan', alpha=0.6, label='Kuroshio')
ax.barh(decades + bar_height, sea_surface_temp, height=bar_height, color='purple', alpha=0.5, label='Sea Surface Temp')

# Labels
ax.set_ylabel('Decade', fontsize=12)
ax.set_xlabel('Value', fontsize=12)

# Legend
ax.legend(loc="upper right")

# Adjust layout
plt.tight_layout()
plt.show()