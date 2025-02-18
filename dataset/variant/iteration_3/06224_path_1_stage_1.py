import matplotlib.pyplot as plt
import numpy as np

# Altered plot showcasing fictional Arbor Population in Magical Woods

# Modified tree species and their corresponding population percentages
tree_species = ['Maple', 'Cherry Blossom', 'Baobab', 'Birch', 'Oak', 'Willow', 'Redwood', 'Pine']
population_percentages = [30, 20, 15, 10, 8, 7, 5, 5]

# Segment colors per tree species
colors = ['#FF4500', '#FF69B4', '#8A2BE2', '#D2B48C', '#8B4513', '#ADFF2F', '#A52A2A', '#228B22']

# Explosion setting to highlight 'Maple' tree species
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

# Initialize pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Generate the pie chart with modified labels
wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species, autopct='%1.1f%%',
                                  startangle=140, explode=explode, colors=colors, shadow=True,
                                  wedgeprops=dict(width=0.4, edgecolor='w'))

# Customization of text within pie chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Customization of labels outside the pie chart
for text in texts:
    text.set_fontsize(11)
    text.set_color('darkslategray')
    text.set_fontweight('semibold')

# Convert pie chart into a donut shape
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Update title with altered message, split into two lines
plt.title('Magical Woods Arbor Population\nDispersal Overview', fontsize=16, fontweight='bold', pad=20)

# Keep pie chart circular
ax.axis('equal')

# Modify legend to reflect new label setup
plt.legend(wedges, tree_species, title="Arbor Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Optimize layout
plt.tight_layout()

# Show the final visual
plt.show()