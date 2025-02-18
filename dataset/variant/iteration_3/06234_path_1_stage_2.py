import matplotlib.pyplot as plt
import numpy as np

# Species categories
species_count = [90, 12, 150, 45, 25, 15]

# Define colors with unique colors for better visualization
colors = ['#d4a0a7', '#c79efc', '#f0a6ca', '#a6e1fa', '#ceed99', '#f5d76e']

# Explode to emphasize Reptiles slice
explode = (0, 0, 0.1, 0, 0, 0)

# Create the figure and the primary subplot
fig, ax = plt.subplots(figsize=(10, 7))

# Pie Chart without labels and title
wedges, _ = ax.pie(species_count, labels=None, autopct=None, startangle=140,
                                  colors=colors, explode=explode, pctdistance=0.85)

# Add a circle at the center to transform pie chart into donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Automatically adjust layout
plt.tight_layout()

# Show the plot
plt.show()