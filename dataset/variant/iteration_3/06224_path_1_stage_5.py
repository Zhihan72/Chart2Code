import matplotlib.pyplot as plt

tree_species = ['Redwood', 'Willow', 'Pine', 'Oak', 'Cherry Blossom', 'Birch', 'Maple', 'Baobab']
population_percentages = [5, 7, 5, 8, 20, 10, 30, 15]

# Manually shuffled color list
colors = ['#D2B48C', '#FF69B4', '#8B4513', '#A52A2A', '#8A2BE2', '#FF4500', '#228B22', '#ADFF2F']
explode = (0, 0, 0, 0, 0, 0, 0.1, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species, autopct='%1.1f%%',
                                  startangle=90, explode=explode, colors=colors, shadow=False,
                                  wedgeprops=dict(edgecolor='dimgrey', linestyle='--'))

for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(11)
    autotext.set_fontweight('normal')

for text in texts:
    text.set_fontsize(12)
    text.set_color('maroon')
    text.set_fontweight('bold')

plt.title('Magical Woods Arbor Population Overview\n (Stylish Edition)', fontsize=18, fontweight='light', pad=25)

ax.axis('equal')
plt.legend(wedges, tree_species, title="Tree Species", loc="upper right", fontsize=9, frameon=True, framealpha=0.3, edgecolor='blue')
plt.grid(visible=True, linestyle='-', linewidth=0.5, color='gray')
plt.tight_layout()
plt.show()