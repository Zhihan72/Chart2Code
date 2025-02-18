import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s']
genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Mystery', 'Romance']
publication_counts = {
    'Fiction': [20, 25, 30, 28, 40],
    'Non-fiction': [10, 15, 25, 35, 45],
    'Science Fiction': [5, 10, 15, 20, 25],
    'Mystery': [8, 12, 18, 22, 30],
    'Romance': [12, 18, 22, 24, 35]
}

data = [publication_counts[genre] for genre in genres]

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['royalblue', 'seagreen', 'coral', 'goldenrod', 'violet']

for i, (color, decade) in enumerate(zip(colors, decades)):
    x_offsets = np.arange(len(genres)) + i * 0.15
    decade_data = [publication_counts[genre][i] for genre in genres]
    ax.bar(x_offsets, decade_data, width=0.15, color=color, alpha=0.8)

ax.set_xlabel('Genres', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_xticks(np.arange(len(genres)) + 0.3)
ax.set_xticklabels(genres, fontsize=10, rotation=45, ha='right')
plt.tight_layout()
plt.show()