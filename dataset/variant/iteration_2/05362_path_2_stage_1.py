import matplotlib.pyplot as plt
import numpy as np

# Years from 2050 to 2060
years = np.arange(2050, 2061)

# Artificial data for water consumption (in million gallons)
neo_tokyo_consumption = np.array([320, 330, 305, 295, 310, 290, 280, 275, 265, 250, 240])
metropolis_consumption = np.array([345, 340, 335, 320, 315, 310, 300, 285, 270, 260, 255])
omega_city_consumption = np.array([290, 295, 285, 280, 275, 265, 255, 250, 245, 230, 220])

# Create a figure and a single subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the water consumption data with markers
ax.plot(years, neo_tokyo_consumption, marker='o', linestyle='-', color='blue', linewidth=2, markersize=8)
ax.plot(years, metropolis_consumption, marker='s', linestyle='-', color='green', linewidth=2, markersize=8)
ax.plot(years, omega_city_consumption, marker='^', linestyle='-', color='red', linewidth=2, markersize=8)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()