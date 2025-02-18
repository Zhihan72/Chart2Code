import matplotlib.pyplot as plt

# Altered tree species and population percentages
tree_species = ['Maple', 'Cherry Blossom', 'Oak', 'Birch', 'Willow', 'Redwood', 'Pine', 'Baobab']
population_percentages = [10, 7, 30, 15, 8, 5, 20, 5]

# Altered colors for each tree species segment
colors = ['#FF4500', '#FF69B4', '#8B4513', '#D2B48C', '#ADFF2F', '#A52A2A', '#228B22', '#8A2BE2']

# Explode to highlight a different tree species
explode = (0, 0, 0.1, 0, 0, 0, 0, 0)

fig, ax = plt.subplots(figsize=(10, 7))

# Plot the pie chart with altered text labels
wedges, texts, autotexts = ax.pie(population_percentages, labels=tree_species,
                                  autopct='%1.1f%%', startangle=120,
                                  explode=explode, colors=colors, shadow=True)

# Customize text inside the pie
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
    autotext.set_fontweight('bold')

# Customize labels outside the pie
for text in texts:
    text.set_fontsize(11)
    text.set_color('darkslategray')
    text.set_fontweight('semibold')

# Altered title
plt.title('Species of Trees in Magical Woodland', fontsize=16, fontweight='bold', pad=20)

# Draw pie as a circle
ax.axis('equal')

# Add a legend with altered title
plt.legend(wedges, tree_species, title="Species of Trees", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1), fontsize=10)

plt.tight_layout()
plt.show()