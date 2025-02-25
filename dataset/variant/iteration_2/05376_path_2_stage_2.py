import matplotlib.pyplot as plt
import numpy as np

# Define star systems with coordinates (x, y), brightness (in arbitrary units)
star_systems = [
    [2, 3, 5.6],   # Alpha Eridani
    [7, 1, 4.2],   # Beta Hydri
    [1, 9, 7.1],   # Gamma Centauri
    [6, 8, 6.3],   # Delta Orionis
    [9, 5, 8.4]    # Epsilon Pegasi
]

# Extract individual lists
x_coords = [data[0] for data in star_systems]
y_coords = [data[1] for data in star_systems]
brightness = [data[2] for data in star_systems]

# Define names for each star system
star_names = ['Alpha Eridani', 'Beta Hydri', 'Gamma Centauri', 'Delta Orionis', 'Epsilon Pegasi']

# Create scatter plot
fig, ax = plt.subplots(figsize=(12, 8))

# Scatter plot with customized markers size and consistent color based on brightness
ax.scatter(x_coords, y_coords, s=[b*20 for b in brightness], c='blue', alpha=0.7, edgecolors='black')

# Annotate each point with star system name
for i, name in enumerate(star_names):
    ax.annotate(name, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Titles and labels
plt.title("Stellar Activities in the Galactic Federation\nStar System Brightness", fontsize=16, fontweight='bold')
plt.xlabel("Galactic X Coordinate", fontsize=12)
plt.ylabel("Galactic Y Coordinate", fontsize=12)

# Grid
ax.grid(True, linestyle='--', alpha=0.5)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()