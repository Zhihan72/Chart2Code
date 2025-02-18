import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2005, 2021)

# Data for sustainability efforts in EcoVille (in arbitrary units)
waste_reduction = [5, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 46, 52, 59, 65, 72]
water_conservation = [3, 4, 5, 7, 9, 12, 15, 19, 23, 28, 33, 39, 45, 52, 59, 67]
green_energy = [1, 2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95]
community_awareness = [2, 3, 4, 6, 8, 10, 13, 16, 20, 24, 29, 35, 41, 48, 56, 65]
urban_greenery = [2, 3, 5, 8, 11, 15, 19, 24, 30, 37, 44, 52, 61, 71, 82, 94]

# Aggregated data for the stacked area chart
sustainability_efforts = np.vstack([waste_reduction, water_conservation, green_energy, community_awareness, urban_greenery])

# Plotting setup
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area plot
ax.stackplot(years, sustainability_efforts, colors=['#33A1C9', '#76C1A1', '#FFD33C', '#FF5733', '#C70039'], alpha=0.8)

# Removing textual elements: title, axis labels, tick labels, legend, and annotations
ax.set_xticks([])
ax.set_yticks([])

# Removing x and y axis labels
ax.set_xlabel('')
ax.set_ylabel('')

# Removing grid lines if desired
ax.grid(False)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()