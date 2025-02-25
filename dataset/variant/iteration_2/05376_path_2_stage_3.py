import matplotlib.pyplot as plt
import numpy as np

# Define star systems with coordinates (x, y), brightness (in arbitrary units)
star_systems = [
    [2, 3, 5.6],  
    [7, 1, 4.2],  
    [1, 9, 7.1],  
    [6, 8, 6.3],  
    [9, 5, 8.4]   
]

x_coords = [data[0] for data in star_systems]
y_coords = [data[1] for data in star_systems]
brightness = [data[2] for data in star_systems]

fig, ax = plt.subplots(figsize=(12, 8))

ax.scatter(x_coords, y_coords, s=[b*20 for b in brightness], c='blue', alpha=0.7, edgecolors='black')

ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()