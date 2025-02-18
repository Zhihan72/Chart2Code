import matplotlib.pyplot as plt
import numpy as np

# Backstory: The Galactic Federation's Observation Committee has been tracking stellar activities across different sectors of the galaxy.
# Each point represents a star system with specific coordinates, brightness (luminosity), and number of planets. 

# Define star systems with coordinates (x, y), brightness (in arbitrary units), and number of planets
star_systems = [
    [2, 3, 5.6, 3],   # Alpha Eridani
    [7, 1, 4.2, 5],    # Beta Hydri
    [1, 9, 7.1, 7],    # Gamma Centauri
    [6, 8, 6.3, 4],    # Delta Orionis
    [9, 5, 8.4, 10],    # Epsilon Pegasi
    [4, 4, 3.8, 2]     # Zeta Reticuli
]

# Extract individual lists
x_coords = [data[0] for data in star_systems]
y_coords = [data[1] for data in star_systems]
brightness = [data[2] for data in star_systems]
num_planets = [data[3] for data in star_systems]

# Define names for each star system
star_names = ['Alpha Eridani', 'Beta Hydri', 'Gamma Centauri', 'Delta Orionis', 'Epsilon Pegasi', 'Zeta Reticuli']

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot with customized markers size and color based on brightness and number of planets
scatter = ax.scatter(x_coords, y_coords, s=[b*20 for b in brightness], c=num_planets, cmap='viridis', alpha=0.7, edgecolors='black')

# Annotate each point with star system name
for i, name in enumerate(star_names):
    ax.annotate(name, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Adding color bar for the number of planets
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Number of Planets', fontsize=12)

# Titles and labels
plt.title("Stellar Activities in the Galactic Federation\nStar System Brightness and Number of Planets", fontsize=16, fontweight='bold')
plt.xlabel("Galactic X Coordinate", fontsize=12)
plt.ylabel("Galactic Y Coordinate", fontsize=12)

# Grid
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()