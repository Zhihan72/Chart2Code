import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories and the number of parameters (spokes)
categories = ['Attack', 'Defense', 'Magic', 'Speed', 'Health']
num_vars = len(categories)

# Attributes for each class
warrior = [8, 9, 2, 5, 10]
mage = [3, 4, 10, 6, 4]
rogue = [7, 5, 3, 10, 6]
ranger = [6, 6, 5, 8, 7]

# Combine data for ease of iteration
data = [warrior, mage, rogue, ranger]
colors = ['red', 'blue', 'green', 'purple']

# Calculate angles for each axis and make plot circular
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a function to plot radar charts
def plot_radar_chart(ax, data, color):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, data, color=color, alpha=0.25)

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Add each class' data to the radar chart
for idx, class_data in enumerate(data):
    plot_radar_chart(ax, class_data, colors[idx])

# Remove visual elements
ax.set_yticks([])  # Remove y-ticks as we are not displaying them
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='black', weight='bold')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()