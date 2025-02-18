import matplotlib.pyplot as plt
import numpy as np

# Data
species = ["Andronian", "Xylok", "Zepherite", "Fermian", "Galzor", 
           "Ignitoid", "Hydrixian", "Eldarian", "Nebulon", "Vortix"]

# Heights (in meters)
heights = np.array([2.3, 1.8, 2.6, 1.5, 2.1, 3.0, 2.8, 2.2, 1.9, 2.4])

# Weights (in kilograms)
weights = np.array([120, 95, 150, 75, 110, 180, 170, 140, 100, 130])

# Bubble sizes (scaled by weight for visual emphasis)
bubble_sizes = weights * 2

# Use a single color for all data points
single_color = 'blue'

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot
scatter = ax.scatter(heights, weights, s=bubble_sizes, c=single_color, alpha=0.8, edgecolors='w', linewidth=0.5)

# Setting up title and labels
ax.set_title("The Galactic Fauna: Study of Fictional Alien Species", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Height (meters)", fontsize=12)
ax.set_ylabel("Weight (kg)", fontsize=12)

# Annotate each point with the species name
for i, species_name in enumerate(species):
    ax.annotate(species_name, (heights[i], weights[i]), fontsize=10, 
                textcoords="offset points", xytext=(0,5), ha='center')

# Grid for readability
ax.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()