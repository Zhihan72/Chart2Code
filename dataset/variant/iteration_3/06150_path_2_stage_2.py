import matplotlib.pyplot as plt
import numpy as np

# Data inputs
years = np.arange(2010, 2024)
bandwidth = [5, 8, 12, 18, 28, 40, 55, 70, 85, 100, 120, 150, 170, 200]
latency = [200, 190, 170, 150, 125, 100, 85, 70, 60, 50, 45, 40, 35, 30]  # Made-up data series

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Main line plot for bandwidth
ax.plot(years, bandwidth, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8, label='Bandwidth')

# Added line plot for latency
ax.plot(years, latency, color='green', marker='s', linestyle='--', linewidth=2, markersize=8, label='Latency')

# Customizing plot appearance
ax.set_xticks(years)
ax.set_xlim(2009, 2023)
ax.set_ylim(0, 220)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding legend to identify data series
ax.legend()

# Ensure layout fits all elements and text
plt.tight_layout()

# Display the plot
plt.show()