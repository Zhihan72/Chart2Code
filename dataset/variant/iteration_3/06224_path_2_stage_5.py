import matplotlib.pyplot as plt

# Shuffled tree species and population percentages while keeping their structure
tree_species = ['Baobab', 'Redwood', 'Cherry Blossom', 'Oak', 'Willow', 'Pine', 'Maple', 'Birch']
population_percentages = [5, 5, 7, 30, 8, 20, 10, 15]  # Aligned accordingly to the shuffled species
single_color = '#228B22'
explode = (0, 0, 0, 0.1, 0, 0, 0, 0)  # Keeping the explode now at 'Oak'

fig, ax = plt.subplots(figsize=(10, 7))
wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species,
                                  autopct='%1.1f%%', startangle=120,
                                  explode=explode, colors=[single_color] * len(tree_species), shadow=True)

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