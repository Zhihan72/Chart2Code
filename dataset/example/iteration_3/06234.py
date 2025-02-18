import matplotlib.pyplot as plt
import numpy as np

# Backstory: The pie chart showcases the percentage breakdown of different types of species 
# that were discovered in an unexplored Amazon rainforest sector during an expedition in 2023.
# The data reflects the diversity of flora and fauna found in a small protected region of the rainforest.

# Species categories
species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects', 'Plants']

# Number of discovered species in each category
species_count = [12, 45, 25, 15, 150, 90]

# Define colors with unique colors for better visualization
colors = ['#d4a0a7', '#c79efc', '#f0a6ca', '#a6e1fa', '#ceed99', '#f5d76e']

# Explode to emphasize Insects slice
explode = (0, 0, 0, 0, 0.1, 0)

# Create the figure and the primary subplot
fig, ax = plt.subplots(figsize=(10, 7))

# Pie Chart with detailed percentage
wedges, texts, autotexts = ax.pie(species_count, labels=species_categories, autopct='%1.1f%%', startangle=140,
                                  colors=colors, explode=explode, pctdistance=0.85)

# Customize text for better readability
for text in texts:
    text.set_fontsize(10)
    text.set_weight('bold')
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')
    autotext.set_weight('bold')

# Add a circle at the center to transform pie chart into donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add title and subtitle to provide more context
plt.title("Species Distribution Discovered in\nAmazon Rainforest Expedition 2023",
          fontsize=16, fontweight='bold', pad=20)

# Add a legend with a subtle shadow
plt.legend(wedges, species_categories, title="Species", loc="center left", bbox_to_anchor=(1, 0.5), shadow=True)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()