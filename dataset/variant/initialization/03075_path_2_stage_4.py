import matplotlib.pyplot as plt
import numpy as np

distribution = np.array([30, 20, 15, 25, 10])
colors = ['#FFC300', '#900C3F', '#DAF7A6', '#33FFEC', '#FF5733']  # Shuffled colors
explode = (0, 0, 0.1, 0, 0)  # Changed explode to highlight the third segment

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(distribution, startangle=90,  # Changed start angle for a different rotation
       colors=colors, explode=explode, 
       wedgeprops=dict(width=0.4, edgecolor='black'))  # Changed width and added border color

ax.grid(True)  # Added grid for stylistic change
ax.legend(['A', 'B', 'C', 'D', 'E'], loc='upper left')  # Added legend with labels

plt.show()