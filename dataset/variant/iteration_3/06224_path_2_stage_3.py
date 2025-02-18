import matplotlib.pyplot as plt

tree_species = ['Maple', 'Cherry Blossom', 'Oak', 'Birch', 'Willow', 'Redwood', 'Pine', 'Baobab']
population_percentages = [10, 7, 30, 15, 8, 5, 20, 5]
colors = ['#FF4500', '#FF69B4', '#8B4513', '#D2B48C', '#ADFF2F', '#A52A2A', '#228B22', '#8A2BE2']
explode = (0, 0, 0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species,
                                  autopct='%1.1f%%', startangle=120,
                                  explode=explode, colors=colors, shadow=True)

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(11)
    text.set_color('darkslategray')
    text.set_fontweight('semibold')

plt.title('Species of Trees in Magical Woodland', fontsize=16, fontweight='bold', pad=20)
ax.axis('equal')

plt.tight_layout()
plt.show()