import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
creatures = ['Dragons', 'Phoenix', 'Unicorns', 'Mermaids', 'Centaurs', 'Valkyries', 'Minotaurs']
popularity = [35, 20, 15, 12, 8, 7, 3]

# Using a single color for all data groups
single_color = ['#FF5733'] * len(creatures)  # Red color for all sections

# Highlight the top favorite creature (Dragons)
explode = [0.1 if creature == 'Dragons' else 0 for creature in creatures]

# Creating the pie chart
plt.figure(figsize=(10, 10))
wedges, texts, autotexts = plt.pie(
    popularity, 
    explode=explode, 
    labels=creatures, 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=single_color,  # Apply consistent color
    pctdistance=0.85, 
    wedgeprops={'edgecolor': 'black'}, 
    shadow=True
)

# Customize the legend
plt.legend(wedges, creatures, title="Mythological Creatures", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Customize text properties
plt.setp(autotexts, size=10, color="white", weight="bold")
plt.setp(texts, size=12)

# Add a title
plt.title('Mysteria City Residents’ Favorite Mythological Creatures in 2023', fontsize=14, fontweight='bold', pad=20)

# Draw a circle for a doughnut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Ensure tidy layout
plt.tight_layout()

# Display the chart
plt.show()