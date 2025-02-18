import matplotlib.pyplot as plt
import numpy as np

# Backstory: This chart depicts the popular flavors of ice cream among teenagers in a fictional town called 'Sweetvale'.
# The data reflects the preferences in terms of flavor popularity.

# Data for the pie chart
flavors = ['Chocolate', 'Vanilla', 'Strawberry', 'Mint Chocolate', 'Cookie Dough', 'Rocky Road', 'Mango']
popularity = [25, 20, 15, 10, 10, 10, 10]  # Proportions sum to 100%

# Colors for each flavor
colors = ['#8B4513', '#F3E5AB', '#FF69B4', '#98FB98', '#FFE4B5', '#D2B48C', '#FFD700']

# Explode the 'Chocolate' and 'Vanilla' slices for emphasis
explode = (0.1, 0.1, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Plot pie chart
wedges, texts, autotexts = ax.pie(
    popularity, 
    labels=flavors, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=colors, 
    explode=explode,
    shadow=True,
    textprops=dict(color="black"),
    wedgeprops=dict(edgecolor='w', linewidth=1.5)
)

# Customizing text inside the wedges
plt.setp(autotexts, size=10, weight="bold")

# Title and legend setup
ax.set_title(
    "Ice Cream Flavor Preferences among Teenagers in Sweetvale", 
    fontsize=16, fontweight='bold', pad=20
)
ax.legend(
    wedges, flavors, title="Flavors", loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1)
)

# Improve layout
plt.tight_layout()

# Display the plot
plt.show()