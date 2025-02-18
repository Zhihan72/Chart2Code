import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analyzing the favorite ice cream flavors within a small town over different seasons

# Ice cream flavors
flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough', 'Butter Pecan', 'Mango']

# Seasonal flavor popularity percentages
winter_popularity = [20, 18, 12, 10, 15, 17, 8]
spring_popularity = [15, 20, 18, 12, 13, 10, 12]
summer_popularity = [10, 15, 22, 8, 10, 9, 26]
fall_popularity = [18, 17, 15, 14, 10, 11, 15]

# Define colors for each flavor using a set colormap
colors = plt.cm.tab10(np.linspace(0, 1, len(flavors)))

fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Subplot titles
season_titles = ["Winter Flavor Favorites", "Spring Flavor Favorites", "Summer Flavor Favorites", "Fall Flavor Favorites"]

# Data for subplots
seasonal_popularities = [winter_popularity, spring_popularity, summer_popularity, fall_popularity]

# Create pie charts for each season
for i, ax in enumerate(axs.flat):
    wedges, texts, autotexts = ax.pie(seasonal_popularities[i], labels=flavors, colors=colors, autopct='%1.1f%%',
                                      startangle=140, pctdistance=0.85,
                                      wedgeprops=dict(edgecolor='w'),
                                      explode=[0.05 if flavor == 'Mango' else 0 for flavor in flavors])
    
    # Draw circle for the donut hole effect
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    ax.add_artist(centre_circle)
    
    # Set each subplot title
    ax.set_title(season_titles[i], fontsize=14, fontweight='bold', pad=20)
    
    # Customize text properties
    for text in texts:
        text.set_fontsize(10)
    
    for autotext in autotexts:
        autotext.set_fontsize(9)
        autotext.set_fontweight('bold')
        autotext.set_color('black')

# Main title for the set of subplots
fig.suptitle('Favorite Ice Cream Flavors in a Small Town Across Seasons', fontsize=16, fontweight='bold', y=1.05)

# Adjust layout to avoid overlap
fig.tight_layout()

# Show the plots
plt.show()