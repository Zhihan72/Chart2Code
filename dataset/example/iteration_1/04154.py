import matplotlib.pyplot as plt
import numpy as np

# Backstory: Survey on Fruit Preference in a Community for setting up a local Farmer's Market

# Data: Percentage preferences for different fruit types
fruit_types = ['Apples', 'Bananas', 'Cherries', 'Grapes', 'Oranges']
preferences_percentages = [25, 20, 15, 30, 10]

# Colors for each fruit segment
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']

# Create figure and subplots
fig, ax = plt.subplots(1, 2, figsize=(14, 8))

# Main Pie Chart: Fruit Preferences
wedges1, texts1, autotexts1 = ax[0].pie(
    preferences_percentages, labels=fruit_types, colors=colors, autopct='%1.1f%%',
    startangle=140, pctdistance=0.85, explode=(0.1, 0, 0, 0.1, 0), shadow=True
)

# Add a circle in the center to turn the pie chart into a donut chart
centre_circle1 = plt.Circle((0, 0), 0.70, fc='white')
ax[0].add_artist(centre_circle1)

# Ensure the pie is drawn as a circle
ax[0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Set title for the main pie chart
ax[0].set_title('Community Fruit Preferences for Local Market', fontsize=14, fontweight='bold', pad=20)

# Side Bar Chart: Detailed Insight on Grapes Subtypes
grape_subtypes = ['Red Grapes', 'Green Grapes', 'Black Grapes']
grape_preferences = [60, 25, 15]
grape_colors = ['#ff6666', '#99ff99', '#6666ff']

y_pos = np.arange(len(grape_subtypes))

ax[1].barh(y_pos, grape_preferences, color=grape_colors, edgecolor='black')
ax[1].set_yticks(y_pos)
ax[1].set_yticklabels(grape_subtypes)
ax[1].invert_yaxis()  # Reverse the order of grape subtypes

# Labeling
ax[1].set_xlabel('Percentage', fontsize=12)
for index, value in enumerate(grape_preferences):
    ax[1].text(value + 2, index, f'{value}%', va='center', ha='left', fontsize=10)

# Title for the bar chart
ax[1].set_title('Preference Distribution Among Grapes Subtypes', fontsize=14, fontweight='bold', pad=20)

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()