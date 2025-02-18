import numpy as np
import matplotlib.pyplot as plt

# Backstory:
# We are conducting a "Fruit Nutritional Analysis" comparing the nutritional values of different fruits.
# The data collected is based on averages from nutritional studies.

# Define the categories and their respective scores
categories = ['Vitamin C', 'Fiber', 'Antioxidants', 'Natural Sugars', 'Water Content']
fruits = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Blueberry']

# Define scores for each fruit
data = {
    'Apple': [7, 6, 8, 8, 9],
    'Banana': [5, 5, 6, 9, 8],
    'Orange': [9, 6, 7, 7, 8],
    'Strawberry': [8, 7, 9, 5, 9],
    'Blueberry': [8, 7, 10, 5, 9]
}

# Number of variables/categories
num_vars = len(categories)

# Function to create a radar chart
def create_radar_chart(ax, data, label, color):
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    data += data[:1]
    angles += angles[:1]
    ax.fill(angles, data, color=color, alpha=0.25)
    ax.plot(angles, data, color=color, linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=11)

# Initialize subplot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Assign colors to each fruit
colors = ['#FF9999', '#FFE766', '#FFA07A', '#7FFFD4', '#B0E0E6']

# Plot each fruit's data on the radar chart
for fruit, color in zip(fruits, colors):
    create_radar_chart(ax, data[fruit], fruit, color)

# Set the title and legend
ax.set_title('Fruit Nutritional Analysis', size=16, weight='bold', pad=20)
ax.legend(fruits, loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the radar chart
plt.show()