import matplotlib.pyplot as plt
import numpy as np

# Data Setup
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
rentals = np.array([12, 15, 18, 22, 25, 30, 35, 33, 28, 24, 20, 18])

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the line
ax.plot(months, rentals, marker='o', linestyle='-', color='darkblue', linewidth=2)

# Titles and labels
ax.set_title('Bicycle Rentals in Greenford - 2022', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Rentals (k)', fontsize=12)

# Set y-axis limits
ax.set_ylim(0, 40)

# Customize x-ticks
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45, fontsize=10)

plt.tight_layout()

# Show the plot
plt.show()