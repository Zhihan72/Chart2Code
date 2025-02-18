import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data for exoplanets
exoplanet_names = ['Kepler-452b', 'Proxima Centauri b', 'TRAPPIST-1d', 'LHS 1140b', 'GJ 667 Cc', 'HD 40307 g']
atmosphere_quality = [0.85, 0.90, 0.75, 0.70, 0.65, 0.80]  # Reordered values
surface_water_content = [55, 40, 45, 30, 50, 60]  # Reordered values
solar_radiation_levels = [0.9, 1.1, 1.0, 1.2, 0.8, 1.1]  # Reordered values
potential_habitability = [250, 270, 200, 300, 150, 180]  # Reordered values

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

# Titles and labels
ax.set_title("Exploring Exoplanetary Habitability:\nThe Galaxipedia Survey of 3D Bio-Signatures", fontsize=16, fontweight='bold')
ax.set_xlabel("Atmosphere Quality (normalized)", fontsize=12)
ax.set_ylabel("Surface Water Content (%)", fontsize=12)
ax.set_zlabel("Solar Radiation Levels (normalized)", fontsize=12)

# Annotate exoplanets
for i, name in enumerate(exoplanet_names):
    ax.text(atmosphere_quality[i], surface_water_content[i], solar_radiation_levels[i], name, fontsize=9, color='black')

# Add a color bar
cbar = plt.colorbar(scatter, pad=0.1)
cbar.set_label('Potential Habitability Index', fontsize=12)

# Ensure layout is optimized
plt.tight_layout()

# Display the plot
plt.show()