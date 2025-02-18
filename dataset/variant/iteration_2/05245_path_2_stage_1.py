import matplotlib.pyplot as plt
import numpy as np

accessories = ['Phone Cases', 'Screen Protectors', 'Chargers', 'Headphones', 'Smartwatches', 'Other']
revenues = [18, 12, 14, 20, 10, 6]

# New colors for the pie chart segments
new_colors = ['#ff6666', '#ffcc66', '#66ff66', '#66ffff', '#6666ff', '#cc66ff']

explode = (0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    revenues, 
    labels=accessories, 
    colors=new_colors, 
    autopct='%1.1f%%', 
    startangle=140,
    explode=explode,
    pctdistance=0.85,
    wedgeprops=dict(width=0.3)
)

for text in texts:
    text.set_fontsize(12)
    text.set_color('black')
for autotext in autotexts:
    autotext.set_fontsize(11)
    autotext.set_color('white')

plt.title(
    "Global Revenue Distribution of Mobile Phone Accessories in 2023\n(by Category, in Billions of Dollars)",
    fontsize=16,
    fontweight='bold',
    color='darkblue',
    pad=20
)

centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.axis('equal')

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