import matplotlib.pyplot as plt
import numpy as np

# The imaginary backstory: Survey of Preferred Fruit Flavors in a Local Market
# This survey was conducted among 1000 local residents to understand their preferred fruit flavors.
flavors = ['Apple', 'Banana', 'Strawberry', 'Pineapple', 'Orange', 'Grapes']
preferences = [300, 200, 150, 100, 150, 100]  # Number of preferences for each flavor

# Colors for each fruit flavor slice
colors = ['#FF9999', '#FFD700', '#FF69B4', '#FFDAB9', '#FFA500', '#9ACD32']

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

# Explode the slice with the highest preference 'Apple'
explode = [0.1 if i == max(preferences) else 0 for i in preferences]

# Plotting the pie chart with custom settings
wedges, texts, autotexts = ax.pie(
    preferences, explode=explode, labels=flavors, colors=colors, autopct='%1.1f%%', shadow=True, 
    startangle=140, pctdistance=0.85, textprops={'fontsize': 9, 'color': 'black'}
)

# Draw a circle at the center to transform it into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Set title with line break for clarity
ax.set_title('Survey of Preferred Fruit Flavors\nAmong Local Residents', fontsize=14, fontweight='bold', pad=20)

# Optimize placement of the legend outside the pie chart
ax.legend(wedges, flavors, title="Flavors", loc="center left", bbox_to_anchor=(1, 0.5))

# Automatically adjust subplot parameters to give specified padding
plt.tight_layout()

# Display the chart
plt.show()