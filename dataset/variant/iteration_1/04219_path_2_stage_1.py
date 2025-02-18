import matplotlib.pyplot as plt
import numpy as np

# Define the stages and the number of projects at each stage
stages = [
    "Idea Generation", 
    "Prototype Development", 
    "Alpha Testing", 
    "Beta Testing", 
    "Market Introduction", 
    "Market Success"
]
projects = np.array([500, 300, 200, 100, 50, 30])

# Define the colors for each stage
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e4']

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Customize the funnel chart
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')  # Remove axes for a cleaner look

# Title
ax.set_title(
    'Tech Startup Innovation Funnel:\nFrom Idea to Market Success',
    fontsize=16, weight='bold', ha='center', va='bottom', pad=30
)

plt.tight_layout()

# Data for categories of initial ideas
categories = ['Software', 'Hardware', 'Service', 'Hybrid']
category_counts = [250, 150, 75, 25]

# Colors for the pie chart
pie_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create a new figure for the pie chart
fig2, ax2 = plt.subplots(figsize=(8, 8))

# Create donut pie chart
ax2.pie(category_counts, labels=categories, colors=pie_colors, autopct='%1.1f%%',
        startangle=140, wedgeprops={'edgecolor': 'black', 'width': 0.3})

# Title for the pie chart
ax2.set_title('Initial Idea Categories in Idea Generation Phase',
              fontsize=16, weight='bold', pad=20)

plt.tight_layout()

# Display both plots
plt.show()