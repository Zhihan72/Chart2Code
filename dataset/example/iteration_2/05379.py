import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Backstory: A futuristic society conducts an annual survey to determine the top leisure activities on different space colonies. Each colony is known for its unique blend of leisure offerings, which are evaluated across different aspects like Physical, Mental, Social, Artistic, and Relaxation benefits.

# List of colonies and leisure activities attributes
colonies = ['Colony A', 'Colony B', 'Colony C', 'Colony D']
attributes = ['Physical', 'Mental', 'Social', 'Artistic', 'Relaxation']

# Data for each colony
data = [
    [7, 9, 8, 6, 8],  # Colony A
    [6, 8, 7, 7, 9],  # Colony B
    [9, 7, 8, 6, 7],  # Colony C
    [8, 8, 6, 7, 8]   # Colony D
]

# Convert data to a Numpy array for easier manipulation
data = np.array(data)

# Number of attributes
num_attributes = len(attributes)

# Calculate the angle for each attribute on the radar chart
angles = np.linspace(0, 2 * pi, num_attributes, endpoint=False).tolist()
angles += angles[:1]  # Complete the loop to close the circle

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define colors for each colony
colors = ['#1f78b4', '#33a02c', '#e31a1c', '#ff7f00']

# Plot each colony's data
for i, colony_data in enumerate(data):
    values = colony_data.tolist()
    values += values[:1]  # Close the loop
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=colonies[i], color=colors[i])
    ax.fill(angles, values, color=colors[i], alpha=0.25)

# Add labels for each attribute
plt.xticks(angles[:-1], attributes, color='grey', size=10, fontweight='bold')

# Set radial labels
ax.set_rlabel_position(30)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="grey", size=8, fontweight='bold')
plt.ylim(0, 10)

# Add a title to the chart
plt.title("Galactic Leisure Survey:\nColony Leisure Activities Evaluation", size=14, color='navy', pad=20)

# Add a legend to the chart
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Colonies", fontsize='medium', title_fontsize='13')

# Automatically adjust the layout to prevent overlapping elements
plt.tight_layout()

# Display the radar chart
plt.show()