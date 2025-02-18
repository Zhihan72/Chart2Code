import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# AdventureLand is a theme park with multiple popular rides. To celebrate its 10th anniversary, the park management wants to showcase the popularity of its rides based on visitor preferences over the past decade.

# Data for the pie chart
ride_names = ['Dragon Coaster', 'Pirate Ship', 'Haunted Mansion', 'Safari Adventure', 'Water Rapids']
visitor_percentage = [25, 20, 15, 30, 10]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Setup the figure
fig, ax = plt.subplots(figsize=(10, 7))

# Create the pie chart
wedges, texts, autotexts = ax.pie(
    visitor_percentage,
    labels=ride_names,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    wedgeprops=dict(edgecolor='black'),
    explode=(0.1, 0, 0, 0.1, 0),
    shadow=True
)

# Improve text/annotation appearance
plt.setp(autotexts, size=12, weight="bold", color="white")
plt.setp(texts, size=10)

# Set main title and sub-title
plt.title('Visitor Preferences for AdventureLand Rides\n10th Anniversary Special', fontsize=16, fontweight='bold', color='navy', pad=20)

# Add a legend
ax.legend(
    wedges, 
    [f"{ride}: {percentage}%" for ride, percentage in zip(ride_names, visitor_percentage)], 
    title="Rides", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=10,
    title_fontsize=12
)

# Equal aspect ratio ensures that pie is drawn as a circle
ax.set_aspect('equal')

# Adjust layout
plt.tight_layout()

# Display the chart
plt.show()