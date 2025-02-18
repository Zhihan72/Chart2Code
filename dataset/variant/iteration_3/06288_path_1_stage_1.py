import matplotlib.pyplot as plt
import numpy as np

# Data
species = ["Andronian", "Xylok", "Zepherite", "Fermian", "Galzor", 
           "Ignitoid", "Hydrixian", "Eldarian", "Nebulon", "Vortix",
           "Lithorian", "Plazmoid", "Quarkian", "Solaran", "Astralan"]

# Heights (in meters)
heights = np.array([2.3, 1.8, 2.6, 1.5, 2.1, 3.0, 2.8, 2.2, 1.9, 2.4,
                    2.0, 2.9, 1.7, 3.1, 2.5])

# Weights (in kilograms)
weights = np.array([120, 95, 150, 75, 110, 180, 170, 140, 100, 130,
                    115, 185, 85, 190, 135])

# Planet Gravities (relative to Earth's gravity)
gravities = np.array([0.85, 0.95, 1.1, 1.25, 1.0, 0.9, 1.3, 1.15, 0.98, 1.05,
                      1.1, 1.08, 0.87, 1.2, 0.99])

# Bubble sizes (scaled by weight for visual emphasis)
bubble_sizes = weights * 2

# Colors based on gravity
colors = gravities

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot
scatter = ax.scatter(heights, weights, s=bubble_sizes, c=colors, cmap='viridis', alpha=0.8, edgecolors='w', linewidth=0.5)

# Setting up title and labels
ax.set_title("The Galactic Fauna: Study of Fictional Alien Species", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Height (meters)", fontsize=12)
ax.set_ylabel("Weight (kg)", fontsize=12)

# Annotate each point with the species name
for i, species_name in enumerate(species):
    ax.annotate(species_name, (heights[i], weights[i]), fontsize=10, 
                textcoords="offset points", xytext=(0,5), ha='center')

# Color bar to reflect gravities
cbar = plt.colorbar(scatter, ax=ax, pad=0.1)
cbar.set_label('Planet Gravity (relative to Earth)', fontsize=12)

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()