import matplotlib.pyplot as plt
import numpy as np

# Data definition
decades = np.array([1980, 1990, 2000, 2010, 2020])
sea_levels_ny = np.array([0, 12, 22, 35, 48])
sea_levels_la = np.array([0, 10, 20, 32, 50])
sea_levels_miami = np.array([0, 15, 25, 40, 60])
sea_levels_tokyo = np.array([0, 8, 18, 30, 45])
sea_levels_mumbai = np.array([0, 20, 30, 45, 65])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the data
ax.plot(decades, sea_levels_ny, marker='o', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_la, marker='s', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_miami, marker='^', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_tokyo, marker='d', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_mumbai, marker='*', linewidth=2, markersize=8)

# Add grid
ax.grid(True, linestyle='--', alpha=0.5)

# Set ticks
plt.xticks(decades)
plt.yticks(np.arange(0, 71, 10))

# Set the limits for clarity
ax.set_xlim(1975, 2025)
ax.set_ylim(0, 70)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()