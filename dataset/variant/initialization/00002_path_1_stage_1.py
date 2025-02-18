import matplotlib.pyplot as plt
import numpy as np

# Decades of exploration
decades = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])

# Sea surface temperatures (hypothetical data)
sea_surface_temp = np.array([14.5, 15.0, 15.3, 15.5, 15.7, 16.0, 16.2, 16.5])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))

# Create horizontal bar chart for sea surface temperatures
bar_width = 8  # Height of the bars when horizontal
ax.barh(decades, sea_surface_temp, height=bar_width, color='orange', alpha=0.5, label='Sea Surface Temperature (°C)')

# Titles and labels
ax.set_title('Sea Surface Temperature Over Decades', fontsize=14, pad=20)
ax.set_xlabel('Sea Surface Temperature (°C)', fontsize=12)
ax.set_ylabel('Decade', fontsize=12)

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.7)

# Legend
ax.legend(loc='lower right', fontsize=10, frameon=False)

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()