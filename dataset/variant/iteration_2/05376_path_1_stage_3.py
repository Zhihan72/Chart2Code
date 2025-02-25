import matplotlib.pyplot as plt
import numpy as np

star_systems = [
    [2, 3, 5.6, 3],   
    [7, 1, 4.2, 5],    
    [1, 9, 7.1, 7],   
    [6, 8, 6.3, 4],    
    [9, 5, 8.4, 10],    
    [4, 4, 3.8, 2],
    [3, 6, 5.0, 6],    
    [8, 2, 7.5, 8]     
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
    'Eta Cassiopeiae',   
    'Theta Eridani'      
]

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(x_coords, y_coords, s=[b*25 for b in brightness], c=num_planets, cmap='cool', alpha=0.6, edgecolors='r', marker='x')

for i, name in enumerate(star_names):
    ax.annotate(name, (x_coords[i], y_coords[i]), textcoords="offset points", xytext=(5,5), ha='left', fontsize=8, color='purple')

cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Number of Planets', color='blue')

plt.title("Galactic Star Systems\nBrightness vs Number of Planets", fontsize=14, fontweight='bold')
plt.xlabel("Galactic X", fontsize=11, color='darkgreen')
plt.ylabel("Galactic Y", fontsize=11, color='darkgreen')

ax.grid(False)

plt.tight_layout()
plt.show()