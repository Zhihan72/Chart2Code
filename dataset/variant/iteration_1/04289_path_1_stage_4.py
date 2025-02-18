import matplotlib.pyplot as plt
import numpy as np

# Define the months as x-axis labels
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Rainfall data now has shuffled values to reflect randomness while maintaining dimension
rainfall = [70, 120, 50, 140, 110, 150, 60, 180, 100, 80, 70, 160]

# Average temperature data also shuffled to reflect randomness
avg_temperature = [12, 7, 27, 17, 28, 10, 22, 15, 20, 5, 25, 7]

# Create a figure and axis for the first plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Rainfall data plotted with markers and line style
ax1.plot(months, rainfall, marker='o', linestyle='-', color='mediumseagreen', linewidth=2)

# Create a second y-axis for average temperature data
ax2 = ax1.twinx()

# Average temperature data plotted with different markers and line style
ax2.plot(months, avg_temperature, marker='s', linestyle='--', color='darkorange', linewidth=2)

# Adjust layout to prevent overlapping
fig.tight_layout()

# Display the plot
plt.show()