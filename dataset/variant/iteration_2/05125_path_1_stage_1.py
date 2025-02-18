import matplotlib.pyplot as plt
import numpy as np

# Data for the favorite sci-fi franchises
franchises = ['Star Wars', 'Star Trek', 'Doctor Who', 'Dune', 'The Expanse', 'Others']
popularity_percentages = [30, 25, 15, 10, 10, 10]

# New set of colors for each franchise
colors = ['#ff4500', '#1e90ff', '#32cd32', '#ff8c00', '#6a5acd', '#ff1493']

# Explode the 'Star Wars' slice for emphasis
explode = (0.1, 0, 0, 0, 0, 0)

# Create the pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    popularity_percentages, 
    explode=explode, 
    labels=franchises, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=colors, 
    pctdistance=0.85,
    wedgeprops=dict(edgecolor='white', linewidth=2, alpha=0.9)
)

# Customize the text in wedges
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight('bold')

# Add a circle at the center transforming the pie chart into a donut chart
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
ax.add_artist(centre_circle)

# Set the title
plt.title('Favorite Science Fiction Franchises at Sci-Fi Convention 2023', fontsize=16, fontweight='bold', pad=20)

# Add legend
ax.legend(wedges, franchises, title="Franchises", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

# Ensure the pie chart is drawn as a circle
ax.set_aspect('equal')

# Automatically adjust layout for best presentation
plt.tight_layout()

# Display the chart
plt.show()