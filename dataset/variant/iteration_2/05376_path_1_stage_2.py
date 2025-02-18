import matplotlib.pyplot as plt
import numpy as np

star_systems = [
    [2, 3, 5.6, 3],   
    [7, 1, 4.2, 5],    
    [1, 9, 7.1, 7],   
    [6, 8, 6.3, 4],    
    [9, 5, 8.4, 10],    
    [4, 4, 3.8, 2],
    [3, 6, 5.0, 6],    # Added star system
    [8, 2, 7.5, 8]     # Added star system
]

x_coords = [data[0] for data in star_systems]
y_coords = [data[1] for data in star_systems]
brightness = [data[2] for data in star_systems]
num_planets = [data[3] for data in star_systems]

star_names = [
    'Alpha Eridani', 
    'Beta Hydri', 
    'Gamma Centauri', 
    'Delta Orionis', 
    'Epsilon Pegasi', 
    'Zeta Reticuli',
    'Eta Cassiopeiae',   # Name for added star system
    'Theta Eridani'      # Name for added star system
]

fig, ax = plt.subplots(figsize=(12, 8))

scatter = ax.scatter(x_coords, y_coords, s=[b*20 for b in brightness], c=num_planets, cmap='plasma', alpha=0.7, edgecolors='black')

for i, name in enumerate(star_names):
    ax.annotate(name, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Number of Planets', fontsize=12)

plt.title("Stellar Activities in the Galactic Federation\nStar System Brightness and Number of Planets", fontsize=16, fontweight='bold')
plt.xlabel("Galactic X Coordinate", fontsize=12)
plt.ylabel("Galactic Y Coordinate", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()