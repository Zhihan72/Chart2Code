import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

encounters_data = np.array([
    [120, 80, 45], 
    [95, 70, 60],   
    [150, 50, 35], 
    [85, 90, 55]
])

fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(111, projection='3d')

num_parks = encounters_data.shape[0]
num_wildlife_types = encounters_data.shape[1]
single_color = 'blue'

for i in range(num_parks):
    x_positions = np.arange(num_wildlife_types)
    y_positions = [i] * num_wildlife_types
    z_positions = np.zeros(num_wildlife_types)
    
    ax.bar3d(
        x_positions, y_positions, z_positions, 
        dx=0.4, dy=0.4, dz=encounters_data[i], 
        color=single_color, alpha=0.9, edgecolor='k'
    )

ax.view_init(elev=35, azim=45)
plt.tight_layout()
plt.show()