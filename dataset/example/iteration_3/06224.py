import matplotlib.pyplot as plt
import numpy as np

# Backstory: Distribution of Tree Species in an Imaginary Forest
# The chart illustrates the diversity of tree species in the "Enchanted Forest" which includes both common and rare species.

# Tree species and their population percentages
tree_species = ['Oak', 'Pine', 'Birch', 'Maple', 'Willow', 'Cherry Blossom', 'Redwood', 'Baobab']
population_percentages = [30, 20, 15, 10, 8, 7, 5, 5]

# Colors for each tree species segment
colors = ['#8B4513', '#228B22', '#D2B48C', '#FF4500', '#ADFF2F', '#FF69B4', '#A52A2A', '#8A2BE2']

# Define explosion to highlight the most common species
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the pie chart
wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species, autopct='%1.1f%%',
                                  startangle=140, explode=explode, colors=colors, shadow=True,
                                  wedgeprops=dict(width=0.4, edgecolor='w'))

# Customize each text inside the pie chart
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Customize the labels outside the pie chart
for text in texts:
    text.set_fontsize(11)
    text.set_color('darkslategray')
    text.set_fontweight('semibold')

# Draw a circle at the center to transform the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Add a title, breaking it into two lines
plt.title('Tree Species Distribution\nin Enchanted Forest', fontsize=16, fontweight='bold', pad=20)

# Ensure the pie chart is drawn as a circle.
ax.axis('equal')

# Add a legend with tree species names
plt.legend(wedges, tree_species, title="Tree Species", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()