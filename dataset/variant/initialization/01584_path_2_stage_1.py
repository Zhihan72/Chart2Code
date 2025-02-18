import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Data preparation
genres = [
    'Fiction', 
    'Non-Fiction', 
    'Mystery/Thriller', 
    'Science Fiction/Fantasy', 
    'Romance', 
    'Historical', 
    'Young Adult'
]

popularity = [25, 20, 15, 15, 10, 8, 7]

# Enhanced color scheme using a gradient colormap
colors = cm.viridis(np.linspace(0, 1, len(genres)))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=[f'{genre}\n{pop}%' for genre, pop in zip(genres, popularity)], 
    colors=colors, 
    autopct=lambda p: f'{p:.1f}%', 
    startangle=140,
    pctdistance=0.8, 
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2),
    textprops={'fontsize': 10, 'weight': 'bold'}
)

# Draw circle for the donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Remove borders by setting axis off
ax.axis('off')

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()