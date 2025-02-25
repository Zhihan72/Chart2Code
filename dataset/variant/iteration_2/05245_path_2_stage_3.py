import matplotlib.pyplot as plt
import numpy as np

accessories = [
    'Portable Storage', 
    'Headphones', 
    'Smartwatches', 
    'Phone Cases', 
    'Screen Protectors', 
    'Bluetooth Speakers',
    'Battery Packs', 
    'Other', 
    'Chargers'
]
revenues = [18, 12, 14, 20, 10, 6, 7, 5, 8]

new_colors = [
    '#66ff66', 
    '#66ffff', 
    '#cc66ff', 
    '#ff6666', 
    '#ffcc66', 
    '#ff6666',
    '#ffcc66', 
    '#6666ff', 
    '#66ff66'
]

explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)

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
    "2023 Mobile Accessory Revenue Breakdown\n(Category, Billions USD)",
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
    title="Accessory Types", 
    loc="center left", 
    bbox_to_anchor=(1, 0, 0.5, 1), 
    fontsize=10
)

plt.tight_layout()

plt.show()