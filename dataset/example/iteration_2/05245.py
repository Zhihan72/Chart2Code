import matplotlib.pyplot as plt
import numpy as np

# Data Setup
# The data represents the global revenue distribution of different types of mobile phone accessories in 2023, in billions of dollars.
accessories = ['Phone Cases', 'Screen Protectors', 'Chargers', 'Headphones', 'Smartwatches', 'Other']
revenues = [18, 12, 14, 20, 10, 6]

# Colors for the pie chart segments
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']

# Explode the largest segment slightly to highlight it
explode = (0.1, 0, 0, 0, 0, 0)

# Create a pie chart
fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    revenues, 
    labels=accessories, 
    colors=colors, 
    autopct='%1.1f%%', 
    startangle=140,
    explode=explode,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3)  # Donut shape
)

# Enhance the text appearance
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

# Add title with contextual information
plt.title(
    "Global Revenue Distribution of Mobile Phone Accessories in 2023\n(by Category, in Billions of Dollars)",
    fontsize=16,
    fontweight='bold',
    color='darkblue',
    pad=20
)

# Draw the circle in the middle for donut chart appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

# Ensure the pie chart is drawn as a circle
plt.axis('equal')

# Add legend with additional context on the revenue
ax.legend(
    wedges, 
    [f'{accessory}: ${revenue}B' for accessory, revenue in zip(accessories, revenues)], 
    title="Accessories", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=10
)

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()