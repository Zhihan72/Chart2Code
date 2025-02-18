import matplotlib.pyplot as plt
import numpy as np

# Data inputs
years = np.arange(2010, 2024)
bandwidth = [5, 8, 12, 18, 28, 40, 55, 70, 85, 100, 120, 150, 170, 200]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Main line plot
ax.plot(years, bandwidth, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8)

# Customizing plot appearance
ax.set_xticks(years)
ax.set_xlim(2009, 2023)
ax.set_ylim(0, 220)
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Ensure layout fits all elements and text
plt.tight_layout()

# Display the plot
plt.show()