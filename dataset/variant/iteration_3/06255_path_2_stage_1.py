import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Resource usage data (in thousands of units)
moon_crystals = np.array([5, 7, 9, 11, 14, 17, 20, 25, 30, 35, 40])
sun_gemstones = np.array([3, 4, 5, 6, 8, 9, 11, 13, 15, 17, 20])
star_dust = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20])
sky_pearls = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Aggregated data for the stacked area plot
resource_data = np.vstack([moon_crystals, sun_gemstones, star_dust, sky_pearls])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, resource_data, colors=['#C0C0C0', '#FFD700', '#ADD8E6', '#FF69B4'], alpha=0.8)

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()