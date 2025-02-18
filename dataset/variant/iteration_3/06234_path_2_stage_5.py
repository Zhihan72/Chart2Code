import matplotlib.pyplot as plt

species_categories = [
    'Avian Friends', 'Scaled Wonders', 'Slithering Species', 'Hoppers', 
    'Tiny Flyers', 'Green Giants', 'Swimmers', 'Decomposers', 'Crawlers'
]
species_count = [12, 45, 25, 15, 150, 90, 30, 50, 20]
colors = ['#f5d76e', '#ceed99', '#a6e1fa', '#c79efc', '#f0a6ca', '#d4a0a7', 
          '#add8e6', '#90ee90', '#ffb6c1']

explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 6))
wedges, texts, autotexts = ax.pie(species_count, labels=species_categories, autopct='%1.1f%%',
                                  startangle=90, colors=colors, explode=explode, pctdistance=0.75)

for text in texts:
    text.set_fontsize(11)
    text.set_weight('normal')
    
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_color('darkblue')
    autotext.set_weight('bold')

plt.title("Biodiversity Survey - Expedition Fun!", fontsize=14, fontweight='normal', color='green', pad=15)
plt.legend(wedges, species_categories, title="Fauna & Flora", loc="upper left", bbox_to_anchor=(0.8, 0.6), shadow=False)

plt.grid(axis='y', linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()