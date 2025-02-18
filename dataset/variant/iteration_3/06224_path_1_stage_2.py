import matplotlib.pyplot as plt

tree_species = ['Maple', 'Cherry Blossom', 'Baobab', 'Birch', 'Oak', 'Willow', 'Redwood', 'Pine']
population_percentages = [30, 20, 15, 10, 8, 7, 5, 5]
colors = ['#FF4500', '#FF69B4', '#8A2BE2', '#D2B48C', '#8B4513', '#ADFF2F', '#A52A2A', '#228B22']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species, autopct='%1.1f%%',
                                  startangle=140, explode=explode, colors=colors, shadow=True,
                                  wedgeprops=dict(edgecolor='w'))

for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

for text in texts:
    text.set_fontsize(11)
    text.set_color('darkslategray')
    text.set_fontweight('semibold')

plt.title('Magical Woods Arbor Population\nDispersal Overview', fontsize=16, fontweight='bold', pad=20)

ax.axis('equal')
plt.legend(wedges, tree_species, title="Arbor Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)
plt.tight_layout()
plt.show()