import matplotlib.pyplot as plt
import numpy as np

# Data for the pie chart with 'Mint' and 'Rocky Road' removed
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Cookie Dough', 'Pistachio']
percentages = [30, 25, 15, 10, 5]  # Adjusted percentage shares

# Colors for each ice cream flavor, corresponding to the remaining flavors
colors = ['#f3e5ab', '#7b3f00', '#ff69b4', '#d2b48c', '#93c572']

# Adjusted explode array; no longer exploding 'Mint' and 'Rocky Road'
explode = (0.1, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 8))

# Plotting the pie chart
wedges, texts, autotexts = ax.pie(
    percentages, 
    labels=flavors, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    explode=explode, 
    shadow=True
)

# Enhance text properties
for text in texts:
    text.set_fontsize(12)
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('black')

# Set the chart title
ax.set_title(
    'Favorite Ice Cream Flavors Among Kids in Summer Camp', 
    fontsize=16, 
    fontweight='bold', 
    pad=30
)

# Ensure the pie chart is a perfect circle
ax.axis('equal')

# Place the legend outside the pie chart
plt.legend(
    wedges, flavors,
    title="Ice Cream Flavors",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=12
)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()