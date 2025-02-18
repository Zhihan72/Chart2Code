import matplotlib.pyplot as plt
import numpy as np

species_categories = ['Mammals', 'Birds', 'Reptiles', 'Amphibians', 'Insects', 'Plants']
species_count = [12, 45, 25, 15, 150, 90]
colors = ['#f5d76e', '#ceed99', '#a6e1fa', '#c79efc', '#f0a6ca', '#d4a0a7']

# Altering to emphasize Birds
explode = (0, 0.1, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 6))

# Changing pie chart stylistic elements
wedges, texts, autotexts = ax.pie(species_count, labels=species_categories, autopct='%1.1f%%',
                                  startangle=90, colors=colors, explode=explode, pctdistance=0.75)

for text in texts:
    text.set_fontsize(11)
    text.set_weight('normal')
    
for autotext in autotexts:
    autotext.set_fontsize(8)
    autotext.set_color('darkblue')
    autotext.set_weight('bold')

centre_circle = plt.Circle((0, 0), 0.60, fc='lightgray')
fig.gca().add_artist(centre_circle)

# Different chart title style
plt.title("Species Variety in Amazon Expedition 2023", fontsize=14, fontweight='normal', color='green', pad=15)

# Modifying legend
plt.legend(wedges, species_categories, title="Categories", loc="upper left", bbox_to_anchor=(0.8, 0.8), shadow=False)

plt.grid(axis='y', linestyle='--', linewidth=0.7)

plt.tight_layout()
plt.show()