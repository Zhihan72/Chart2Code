import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Define the categories (parameters)
parameters = ['Resolution', 'Battery Life', 'Processing Power', 'Camera Quality', 'Durability']

# Number of variables
num_vars = len(parameters)

# Define the specs for each type of phone (normalized to a scale of 1-10)
smartphones = {
    'Phone A': [8, 7, 9, 8, 6],
    'Phone B': [7, 6, 9, 6, 8],
    'Phone C': [9, 8, 7, 9, 7],
    'Phone D': [6, 8, 8, 7, 9]
}

# Function to create radar chart
def create_radar_chart(ax, data, categories, label, color):
    angles = np.linspace(0, 2 * pi, num_vars, endpoint=False).tolist()
    data = data + data[:1]  # Complete the loop
    angles += angles[:1]

    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2, linestyle='solid', label=label)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, fontweight='bold')

# Create the radar chart
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Colors for each phone
colors = {
    'Phone A': 'blue', 
    'Phone B': 'green', 
    'Phone C': 'red', 
    'Phone D': 'purple'
}

# Plot each smartphone
for phone, specs in smartphones.items():
    create_radar_chart(ax, specs, parameters, phone, colors[phone])

# Configure the chart's appearance
ax.set_title("Smartphone Comparison on Key Specifications", fontsize=14, fontweight='bold', pad=30)

# Add a legend
plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Phones")

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()