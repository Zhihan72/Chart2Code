import matplotlib.pyplot as plt
import numpy as np

# Define data for light intensity (in Lux) and average plant height (in cm)
light_intensity = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plant_height = np.array([15, 20, 25, 30, 35, 33, 31, 30, 28, 25])

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(light_intensity, plant_height, color='forestgreen', edgecolors='black', s=100, alpha=0.7)

# Add a trend line to show general growth pattern
z = np.polyfit(light_intensity, plant_height, 2)
p = np.poly1d(z)
plt.plot(light_intensity, p(light_intensity), "r--", linewidth=1.5)

# Remove textual elements
plt.xticks([])
plt.yticks([])

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.show()