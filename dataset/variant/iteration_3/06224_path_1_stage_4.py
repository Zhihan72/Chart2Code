import matplotlib.pyplot as plt

tree_species = ['Redwood', 'Willow', 'Pine', 'Oak', 'Cherry Blossom', 'Birch', 'Maple', 'Baobab']
population_percentages = [5, 7, 5, 8, 20, 10, 30, 15]
colors = ['#A52A2A', '#ADFF2F', '#228B22', '#8B4513', '#FF69B4', '#D2B48C', '#FF4500', '#8A2BE2']
explode = (0, 0, 0, 0, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))

# Modified pie chart with different marker style and without shadow
wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species, autopct='%1.1f%%',
                                  startangle=90, explode=explode, colors=colors, shadow=False,
                                  wedgeprops=dict(edgecolor='dimgrey', linestyle='--'))

# Change autotext stylistic elements
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)
    autotext.set_fontweight('normal')

# Change text stylistic elements
for text in texts:
    text.set_fontsize(12)
    text.set_color('maroon')
    text.set_fontweight('bold')

# Alter the title and its styling
plt.title('Magical Woods Arbor Population Overview\n (Stylish Edition)', fontsize=18, fontweight='light', pad=25)

# Alter legend and add gridlines and border
ax.axis('equal')
plt.legend(wedges, tree_species, title="Tree Species", loc="upper right", fontsize=9, frameon=True, framealpha=0.3, edgecolor='blue')
plt.grid(visible=True, linestyle='-', linewidth=0.5, color='gray')
plt.tight_layout()
plt.show()