import matplotlib.pyplot as plt
import numpy as np

popularity = [25, 20, 15, 10, 10]
colors = ['#FFD700', '#8B4513', '#F3E5AB', '#FF69B4', '#98FB98']
explode = (0.1, 0.1, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(
    popularity, 
    startangle=90, 
    colors=colors, 
    explode=explode, 
    shadow=False,
    wedgeprops=dict(edgecolor='black', linestyle='--', linewidth=2)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white', edgecolor='blue', linestyle='-.', linewidth=2)
ax.add_artist(centre_circle)

plt.legend(['Gold', 'Bronze', 'Pale Yellow', 'Pink', 'Light Green'], loc='upper right', fontsize='small')
plt.grid(True, which='both', linestyle=':', linewidth=0.5)

plt.tight_layout()

plt.show()