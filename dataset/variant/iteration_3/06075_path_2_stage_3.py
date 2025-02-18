import matplotlib.pyplot as plt
import numpy as np

popularity = [25, 20, 15, 10, 10, 10, 10]

# Manually shuffled colors
colors = ['#FFD700', '#8B4513', '#F3E5AB', '#FF69B4', '#98FB98', '#D2B48C', '#FFE4B5']

explode = (0.1, 0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

ax.pie(
    popularity, 
    startangle=90, 
    colors=colors, 
    explode=explode,
    shadow=True,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

plt.tight_layout()

plt.show()