import matplotlib.pyplot as plt
import numpy as np

# Categories and their respective proportions
activities = [
    "Leisure & Entertainment", 
    "Work & Career", 
    "Health & Fitness", 
    "Education & Learning", 
    "Socializing", 
    "Travel & Exploration", 
    "Environmental Activities", 
    "Personal Development"
]

# Define proportions of each category on a scale of 100
activity_proportions = [20, 15, 10, 15, 12, 10, 8, 10]

# Use a single color for all activities
single_color = ['#66b3ff'] * len(activities)

# Explode the slices for emphasis on Leisure and Health
explode = (0.1, 0, 0.1, 0, 0, 0, 0, 0)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(
    activity_proportions, labels=activities, colors=single_color, explode=explode,
    autopct='%1.1f%%', startangle=90, pctdistance=0.85, shadow=True
)

# Adjusting the font size and style for the labels
plt.setp(texts, size=10, weight='bold', color='navy')
plt.setp(autotexts, size=10, color='white', weight='bold')

# Add a central circle to convert the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure that the pie chart is drawn as a circle
ax.axis('equal')

# Set the title with proper styling
ax.set_title("Favorite Activities in Zeropolis, 2123", fontsize=16, fontweight='bold', pad=40)

# Add a legend positioned outside the chart
ax.legend(wedges, activities, title="Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=12)

# Automatically adjust the layout to prevent overlapping
plt.tight_layout()

# Display the pie chart
plt.show()