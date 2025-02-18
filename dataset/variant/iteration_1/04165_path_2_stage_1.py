import matplotlib.pyplot as plt
import numpy as np

# Data preparation
screen_time = np.array([0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
sleep_quality = np.array([9, 8.5, 8, 7.5, 7, 6.5, 5.5, 5, 4.5, 4, 3.5, 3, 2.5])
sleep_disturbances = np.array([3, 2, 4, 6, 7, 9, 10, 12, 13, 15, 18, 20, 22])

# Create a figure and axis with dual y-axes
fig, ax1 = plt.subplots(figsize=(12, 8))

# Scatter plot 
ax1.scatter(screen_time, sleep_quality, c='skyblue', edgecolor='k', s=100, alpha=0.7)

# Secondary y-axis for sleep disturbances
ax2 = ax1.twinx()
ax2.plot(screen_time, sleep_disturbances, color='orange', linewidth=2, linestyle='--')

# Grid
ax1.grid(True, linestyle='--', alpha=0.6)

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()