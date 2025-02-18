import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Data for pie chart with one data group removed
popularity = [25, 20, 15, 15, 10, 8]

# Color scheme using a gradient colormap
colors = cm.viridis(np.linspace(0, 1, len(popularity)))

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8))
wedges, texts = ax.pie(
    popularity, 
    labels=None,
    colors=colors, 
    autopct=None,
    startangle=140,
    pctdistance=0.8, 
    wedgeprops=dict(width=0.3, edgecolor='white', linewidth=2)
)

# Draw circle for donut chart
centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig.gca().add_artist(centre_circle)

# Remove borders by setting axis off
ax.axis('off')

plt.tight_layout()

# Display the plot
plt.show()