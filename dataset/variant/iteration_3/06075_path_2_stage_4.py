import matplotlib.pyplot as plt
import numpy as np

# Removed one or more data groups from the original dataset
popularity = [25, 20, 15, 10, 10]

# Adjust colors to match the remaining data groups
colors = ['#FFD700', '#8B4513', '#F3E5AB', '#FF69B4', '#98FB98']

# Adjust explode to match the remaining data groups
explode = (0.1, 0.1, 0, 0, 0)

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