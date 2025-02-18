import matplotlib.pyplot as plt
import numpy as np

# Data Setup
accessories = ['Cases', 'Protectors', 'Chargers', 'Headphones', 'Watches', 'Other']
revenues = [18, 12, 14, 20, 10, 6]

# Colors and explode for pie chart
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
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
    wedgeprops=dict(width=0.3)
)

# Enhance text appearance
for text in texts:
    text.set_fontsize(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

# Add title
plt.title(
    "Mobile Accessories Revenue in 2023",
    fontsize=16,
    fontweight='bold',
    color='darkblue',
    pad=20
)

# Donut chart appearance
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)
plt.axis('equal')

# Add legend
ax.legend(
    wedges, 
    [f'{accessory}: ${revenue}B' for accessory, revenue in zip(accessories, revenues)], 
    title="Accessories", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=10
)

plt.tight_layout()
plt.show()