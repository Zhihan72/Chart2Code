import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking average sea levels at major coastal cities over several decades
# Title: "Rising Waters: The Increasing Threat of Sea Level Rise"
# X-label: Decade
# Y-label: Average Sea Level (mm above baseline)
# Cities: ['New York', 'Los Angeles', 'Miami', 'Tokyo', 'Mumbai']
# Time Period: 1980-2020

# Defining the data
decades = np.array([1980, 1990, 2000, 2010, 2020])
sea_levels_ny = np.array([0, 12, 22, 35, 48])
sea_levels_la = np.array([0, 10, 20, 32, 50])
sea_levels_miami = np.array([0, 15, 25, 40, 60])
sea_levels_tokyo = np.array([0, 8, 18, 30, 45])
sea_levels_mumbai = np.array([0, 20, 30, 45, 65])

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 7))

# Plot the data
ax.plot(decades, sea_levels_ny, marker='o', label='New York', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_la, marker='s', label='Los Angeles', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_miami, marker='^', label='Miami', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_tokyo, marker='d', label='Tokyo', linewidth=2, markersize=8)
ax.plot(decades, sea_levels_mumbai, marker='*', label='Mumbai', linewidth=2, markersize=8)

# Adding annotations for significant points
ax.annotate('Hurricane Sandy', xy=(2010, 35), xytext=(2010, 40),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('Massive Coral Bleaching', xy=(2010, 40), xytext=(2000, 60),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Set titles and labels
ax.set_title("Rising Waters: The Increasing Threat of Sea Level Rise", fontsize=16, fontweight='bold')
ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Average Sea Level (mm above baseline)', fontsize=12)

# Add grid
ax.grid(True, linestyle='--', alpha=0.5)

# Set ticks
plt.xticks(decades)
plt.yticks(np.arange(0, 71, 10))

# Set the limits for clarity
ax.set_xlim(1975, 2025)
ax.set_ylim(0, 70)

# Create a legend
ax.legend(title='Cities', loc='upper left', fontsize=11)

# Optimize layout
plt.tight_layout()

# Display the plot
plt.show()