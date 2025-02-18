import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data for exoplanets
atmosphere_quality = [0.85, 0.90, 0.75, 0.70, 0.65, 0.80]
surface_water_content = [55, 40, 45, 30, 50, 60]
solar_radiation_levels = [0.9, 1.1, 1.0, 1.2, 0.8, 1.1]
potential_habitability = [250, 270, 200, 300, 150, 180]

# Set up the 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
scatter = ax.scatter(
    atmosphere_quality, 
    surface_water_content, 
    solar_radiation_levels, 
    s=potential_habitability, 
    c=potential_habitability, 
    cmap='viridis', 
    alpha=0.7, 
    edgecolors='w', 
    linewidth=0.5
)

# Adjust view angle for optimal display
ax.view_init(elev=20, azim=130)

# Remove annotations and labels
cbar = plt.colorbar(scatter, pad=0.1)

# Ensure layout is optimized
plt.tight_layout()

# Display the plot
plt.show()