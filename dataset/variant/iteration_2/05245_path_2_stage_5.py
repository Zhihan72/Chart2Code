import matplotlib.pyplot as plt

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
    '#66ffff', 
    '#ffcc66', 
    '#66ff66', 
    '#ff6666', 
    '#66ff66', 
    '#6666ff',
    '#cc66ff', 
    '#ff6666', 
    '#ffcc66'
]

explode = (0, 0, 0, 0.1, 0, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(
    revenues, 
    labels=accessories, 
    colors=new_colors, 
    autopct='%1.1f%%', 
    startangle=90,
    explode=explode,
    pctdistance=0.8
)

for text in texts:
    text.set_fontsize(10)
    text.set_color('green')
for autotext in autotexts:
    autotext.set_fontsize(9)
    autotext.set_color('black')

plt.title(
    "2023 Mobile Accessory Revenue Breakdown\n(Category, Billions USD)",
    fontsize=14,
    fontweight='normal',
    color='purple',
    pad=15
)

plt.axis('equal')

ax.legend(
    wedges, 
    [f'{accessory}: ${revenue}B' for accessory, revenue in zip(accessories, revenues)], 
    title="Accessory Categories", 
    loc="upper right", 
    bbox_to_anchor=(1.25, 0.8), 
    fontsize=9
)

plt.grid(visible=True, linestyle='--', color='gray', linewidth=0.5)

plt.tight_layout()

plt.show()