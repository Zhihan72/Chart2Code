import matplotlib.pyplot as plt
import numpy as np

decades = ['60s', '70s', '80s', '90s', '00s']
genres = ['Fic', 'Non-fic', 'Sci-Fi', 'Mystery', 'Romance']

publication_counts = {
    'Fiction': [20, 25, 30, 28, 40],
    'Non-fiction': [10, 15, 25, 35, 45],
    'Science Fiction': [5, 10, 15, 20, 25],
    'Mystery': [8, 12, 18, 22, 30],
    'Romance': [12, 18, 22, 24, 35]
}

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['royalblue', 'seagreen', 'coral', 'goldenrod', 'violet']

for i, (color, decade) in enumerate(zip(colors, decades)):
    x_offsets = np.arange(len(genres)) + i * 0.15
    decade_data = [publication_counts[genre][i] for genre in publication_counts.keys()]
    ax.bar(x_offsets, decade_data, width=0.15, color=color, alpha=0.8)

ax.set_title('Book Genre Popularity Over Decades', fontsize=16, fontweight='bold')
ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel('# Books', fontsize=12)
ax.set_xticks(np.arange(len(genres)) + 0.3)
ax.set_xticklabels(genres, fontsize=10, rotation=45, ha='right')
plt.tight_layout()
plt.show()