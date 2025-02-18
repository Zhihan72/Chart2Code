import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Backstory:
# The chart below compares the primary attributes of different classes in a fantasy role-playing game.
# Each class has distinct strengths and weaknesses which are outlined in the radar chart.

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
classes = ['Warrior', 'Mage', 'Rogue', 'Ranger']
colors = ['red', 'blue', 'green', 'purple']

# Calculate angles for each axis and make plot circular
angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a function to plot radar charts
def plot_radar_chart(ax, data, color, label):
    data += data[:1]
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.fill(angles, data, color=color, alpha=0.25)

# Initialize radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Add each class' data to the radar chart
for idx, class_data in enumerate(data):
    plot_radar_chart(ax, class_data, colors[idx], classes[idx])

# Enhance visual elements
ax.set_yticks([2, 4, 6, 8, 10])  # Set y-ticks to provide scale indicators
ax.set_yticklabels([str(i) for i in range(2, 12, 2)], color='gray')
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=10, color='black', weight='bold')

# Add radial grid for better readability
ax.yaxis.grid(True, color='lightgray', linestyle='--')
ax.xaxis.grid(True, color='lightgray', linestyle='--')

# Title and annotations
plt.title('Attributes of RPG Classes\nA Comparative Study', size=14, weight='bold', pad=20)

# Add legend for clarity
ax.legend(loc='upper right', bbox_to_anchor=(1.25, 1.1), fontsize=10, frameon=True)

# Additional decorations
for label, angle in zip(ax.get_xticklabels(), angles):
    label.set_horizontalalignment('center')

# Improve layout with tight_layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()