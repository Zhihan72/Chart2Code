import numpy as np
import matplotlib.pyplot as plt

# Defining the categories, fruits, and data for the radar chart
categories = ['Vitamin C', 'Fiber', 'Antioxidants', 'Natural Sugars', 'Water Content']
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry']

data = {
    'Apple': [7, 6, 8, 8, 9],
    'Banana': [5, 5, 6, 9, 8],
    'Orange': [9, 6, 7, 7, 8],
    'Strawberry': [8, 7, 9, 5, 9],
    'Blueberry': [8, 7, 10, 5, 9]
}

num_vars = len(categories)

# Create a single radar chart with fill areas
def create_radar_chart(ax, data, color):
    # Calculate angles for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    # Repeat the first value to close the circle
    data += data[:1]
    angles += angles[:1]
    
    # Fill the area within the radar chart
    ax.fill(angles, data, color=color, alpha=0.25)
    # Plot the outline of the radar chart
    ax.plot(angles, data, color=color, linewidth=2)
    # Remove yticks and xticks
    ax.set_yticklabels([])
    ax.set_xticks([])

# Create polar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define colors for each fruit
colors = ['#FF9999', '#FFE766', '#FFA07A', '#7FFFD4', '#B0E0E6']

# Plot each fruit's data in its color
for fruit, color in zip(fruits, colors):
    create_radar_chart(ax, data[fruit], color)

plt.tight_layout()
plt.show()