import matplotlib.pyplot as plt
import numpy as np

art_movements = ['Impressionism', 'Cubism', 'Art Deco', 'Minimalism', 'Surrealism']
design_styles = ['Futurism', 'Bauhaus', 'Brutalism', 'Eco Design', 'Postmodernism']

influence_matrix = np.array([
    [7, 5, 3, 4, 6],
    [6, 8, 2, 5, 7],
    [4, 7, 5, 3, 6],
    [3, 4, 9, 8, 5],
    [5, 6, 4, 7, 8],
])

fig, ax = plt.subplots(figsize=(10, 8))

cax = ax.imshow(influence_matrix, cmap='YlGnBu', aspect='auto', interpolation='nearest')

plt.colorbar(cax)

ax.set_xticks([])
ax.set_yticks([])

for i in range(len(art_movements)):
    for j in range(len(design_styles)):
        ax.text(j, i, influence_matrix[i, j], ha='center', va='center', color='darkred', fontsize=12)

plt.tight_layout()

plt.show()