import matplotlib.pyplot as plt
import numpy as np

# Title and Backstory:
# 
# "Pet Popularity Contest in 2025"
# The humane society conducted a survey to determine the most beloved pets in 2025. 
# The results are in, and we have a visual representation of the survey results. The pie chart displays the proportion of various pets based on their popularity.

# Data for the pie chart
pets = ["Dogs", "Cats", "Rabbits", "Fish", "Birds", "Reptiles", "Hamsters"]
popularity = [45, 30, 5, 7, 6, 4, 3]

# Colors for each segment
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666']
explode = (0.05, 0.05, 0, 0, 0, 0, 0)  # Slightly explode the slices for Dogs and Cats as they are the most popular

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Pie chart
wedges, texts, autotexts = ax.pie(popularity, explode=explode, labels=pets, colors=colors, autopct='%1.1f%%', startangle=140,
                                  wedgeprops=dict(edgecolor='w', linewidth=2))

# Customizing texts for better visibility
for text in texts:
    text.set_fontsize(12)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(11)
    autotext.set_weight('bold')

# Title of the Pie Chart
plt.title("Pet Popularity Contest in 2025\nMost Beloved Pets Survey Results", fontsize=16, fontweight='bold', pad=30)

# Legend
ax.legend(wedges, pets, title="Pets", loc="center right", bbox_to_anchor=(1.25, 0.5), fontsize=10)

# Adjust layout to ensure clarity and avoid text overlap
plt.tight_layout()

# Displaying the plot
plt.show()