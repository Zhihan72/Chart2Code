import matplotlib.pyplot as plt
import numpy as np

# Decades of exploration
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Intensity of the ocean currents (arbitrary data for demonstration)
gulf_stream = np.array([5, 12, 20, 25, 35, 45, 60, 75])
kuroshio_current = np.array([3, 10, 15, 22, 30, 40, 55, 70])
antarctic_circumpolar = np.array([4, 9, 17, 22, 32, 42, 58, 68])

# Sea surface temperatures (hypothetical data)
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])

# Create the plot
fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot ocean currents
ax1.plot(decades, gulf_stream, marker='o', linestyle='-', color='b', linewidth=2)
ax1.plot(decades, kuroshio_current, marker='s', linestyle='--', color='g', linewidth=2)
ax1.plot(decades, antarctic_circumpolar, marker='^', linestyle=':', color='r', linewidth=2)

# Adding a secondary axis for the bar chart
ax2 = ax1.twinx()
bar_width = 8  # Width of the bars
ax2.bar(decades - bar_width / 2, sea_surface_temp, width=bar_width, color='orange', alpha=0.5)

# Titles and labels
ax1.set_xlabel('Decade', fontsize=12)
ax1.set_ylabel('Current Intensity (arbitrary units)', fontsize=12)
ax2.set_ylabel('Sea Surface Temperature (°C)', fontsize=12)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()