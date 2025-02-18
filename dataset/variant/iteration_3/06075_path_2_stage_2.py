import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart
popularity = [25, 20, 15, 10, 10, 10, 10]

# Colors for each flavor
colors = ['#8B4513', '#F3E5AB', '#FF69B4', '#98FB98', '#FFE4B5', '#D2B48C', '#FFD700']

# Explode the 'Chocolate' and 'Vanilla' slices for emphasis
explode = (0.1, 0.1, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot donut chart without labels or text inside the wedges
ax.pie(
    popularity, 
    startangle=90, 
    colors=colors, 
    explode=explode,
    shadow=True,
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Create the donut hole by plotting a white circle in the center
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()