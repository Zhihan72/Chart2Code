import matplotlib.pyplot as plt
import numpy as np

decades = ['1960s', '1970s', '1980s', '1990s', '2000s']
genres = ['Fiction', 'Non-fiction', 'Science Fiction', 'Mystery', 'Romance']

# Publication counts are randomly shuffled manually within their groups
publication_counts = {
    'Fiction': [40, 20, 28, 30, 25],
    'Non-fiction': [35, 25, 10, 45, 15],
    'Science Fiction': [25, 15, 5, 20, 10],
    'Mystery': [30, 8, 22, 12, 18],
    'Romance': [24, 18, 22, 35, 12]
}

data = [publication_counts[genre] for genre in genres]
colors = ['seagreen', 'goldenrod', 'violet', 'coral', 'royalblue']

fig, ax = plt.subplots(figsize=(12, 8))

data = np.array(data)
data = np.transpose(data)

ax.hist(data, bins=np.arange(len(decades) + 1) - 0.5, stacked=True, label=genres, color=colors, alpha=0.8)

ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, fontsize=10, rotation=45, ha='right')
ax.legend(title='Genres', fontsize=10)
plt.tight_layout()
plt.show()