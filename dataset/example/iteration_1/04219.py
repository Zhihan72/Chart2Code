import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Title and backstory
# This funnel chart shows the journey of tech startup innovations through their phases
# from initial idea generation to successful market entry. 

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

# Calculate the width proportions for the trapezoids
widths = projects / projects[0]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Draw each stage as a funnel segment using trapezoids
for i in range(len(stages)):
    # Calculate the top and bottom widths for the trapezoid
    top_width = widths[i] if i == 0 else widths[i-1]
    bottom_width = widths[i]

    # Create the trapezoid
    trapezoid = patches.Polygon(
        [
            [(1 - top_width) / 2, i], [(1 + top_width) / 2, i], 
            [(1 + bottom_width) / 2, i + 1], [(1 - bottom_width) / 2, i + 1]
        ], closed=True, color=colors[i], edgecolor='black'
    )

    ax.add_patch(trapezoid)

    # Annotate each trapezoid with the stage name and project count
    ax.text(0.5, i + 0.5, f"{stages[i]}\n{projects[i]} Projects", 
            ha='center', va='center', fontsize=12, color='black', weight='bold')

# Customize the plot
ax.set_xlim(0, 1)
ax.set_ylim(0, len(stages))
ax.axis('off')  # Remove axes for a cleaner look

# Title and layout adjustments
ax.set_title(
    'Tech Startup Innovation Funnel:\nFrom Idea to Market Success',
    fontsize=16, weight='bold', ha='center', va='bottom', pad=30
)

plt.tight_layout()

# Second plot: Pie chart outlining the category distribution of ideas

# Sample data for categories of initial ideas
categories = ['Software', 'Hardware', 'Service', 'Hybrid']
category_counts = [250, 150, 75, 25]

# Colors for the pie chart
pie_colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Create a new figure for the pie chart
fig2, ax2 = plt.subplots(figsize=(8, 8))

# Create pie chart
ax2.pie(category_counts, labels=categories, colors=pie_colors, autopct='%1.1f%%',
        startangle=140, wedgeprops={'edgecolor': 'black'})

# Title for the pie chart
ax2.set_title('Initial Idea Categories in Idea Generation Phase',
              fontsize=16, weight='bold', pad=20)

plt.tight_layout()

# Display both plots
plt.show()