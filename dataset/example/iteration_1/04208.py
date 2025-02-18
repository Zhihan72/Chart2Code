import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The Galactic Food Corporation (GFC) has surveyed different planets in the galaxy about their favorite food types.
# They are interested in understanding the culinary preferences across various planets to shape their marketing strategies.
# Got data of 4 planets – Earth, Mars, Jupiter, and Neptune.

# Planets surveyed
planets = ['Earth', 'Mars', 'Jupiter', 'Neptune']

# Food categories
food_categories = ['Fruits', 'Vegetables', 'Meat', 'Dairy', 'Grains']

# Preferences percentages schematized for each planet
preferences = [
    [30, 25, 20, 15, 10],  # Earth
    [10, 10, 40, 30, 10],  # Mars
    [15, 20, 30, 20, 15],  # Jupiter
    [20, 30, 20, 10, 20],  # Neptune
]

# Colors for food categories
colors = ['#FFD700', '#32CD32', '#FF6347', '#87CEFA', '#D2B48C']

# Create subplots for each planet
fig, axes = plt.subplots(2, 2, figsize=(12, 12), subplot_kw=dict(aspect="equal"))
fig.suptitle('Galactic Food Preferences Survey:\nA Study Across Different Planets', fontsize=16, fontweight='bold', y=0.92)

# Iterate through each planet to create pie charts
for i, ax in enumerate(axes.flat):
    wedges, texts, autotexts = ax.pie(
        preferences[i], labels=food_categories, autopct='%1.1f%%',
        startangle=140, colors=colors, pctdistance=0.85,
        wedgeprops=dict(width=0.3), explode=[0.05 if j == 0 else 0 for j in range(len(food_categories))],
        shadow=True
    )
    
    # Center circle for donut chart effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)

    # Adjust text properties
    for text in texts:
        text.set_fontsize(10)
        text.set_color('black')

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(9)
        autotext.set_weight('bold')

    # Title for individual pies
    ax.set_title(planets[i], fontsize=14, pad=15)

# Central legend for food categories
handles = [plt.Line2D([0], [0], color=colors[k], lw=4) for k in range(len(food_categories))]
fig.legend(handles, food_categories, loc='upper center', ncol=5, frameon=False, fontsize=12, title='Food Categories', title_fontsize=12)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.9])

# Display the plot
plt.show()