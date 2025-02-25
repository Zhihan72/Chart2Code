import matplotlib.pyplot as plt
import numpy as np

# Backstory: Distribution of Global Internet Users by Activity in 2023
# Imagine we live in 2023 and a global survey has just been completed to determine how people are using the internet. 
# The pie chart will display the percentage distribution of users across various activities.

# Data: Activities and their corresponding percentage shares
activities = ['Social Media', 'Entertainment', 'Online Shopping', 'Education', 'Work', 'News Reading', 'Other']
percentages = [30, 20, 15, 10, 10, 10, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6', '#c7f0c2']
explode = (0.05, 0, 0, 0, 0, 0, 0)  # Emphasize 'Social Media'

# Create pie chart with specific settings
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages, 
    colors=colors, 
    explode=explode, 
    labels=activities, 
    autopct='%1.1f%%', 
    startangle=90, 
    pctdistance=0.85,
    wedgeprops=dict(width=0.3),  # Create donut effect
    shadow=True
)

# Set properties for the labels and percentage texts
plt.setp(autotexts, size=10, weight="bold", color='white')
plt.setp(texts, size=10, weight='bold')

# Add legend with appropriate positioning to avoid overlap
ax.legend(wedges, activities, title="Internet Activities", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))

# Title and layout adjustments
ax.set_title("2023 Global Internet Users' Activity Distribution", fontsize=14, weight='bold', pad=20)

# Ensure that everything fits without overlapping
plt.tight_layout()

# Additional subplot: Bar chart representing mean time spent on each activity (hours per week)
mean_hours = [7.5, 5.0, 3.5, 2.5, 4.0, 2.0, 1.5]  # Mean hours spent per week
ax2 = fig.add_axes([0.8, 0.1, 0.15, 0.3])  # Positioning inset at the right
ax2.barh(activities, mean_hours, color=colors, edgecolor='black', height=0.5)
ax2.set_title('Mean Time (hrs/week)', fontsize=10)
ax2.set_xlim(0, max(mean_hours) + 1)
ax2.invert_yaxis()
ax2.set_xticks([])  # Hiding x-axis ticks for clarity

# Ensure the pie chart is a circle
ax.axis('equal')

# Display the plot
plt.show()