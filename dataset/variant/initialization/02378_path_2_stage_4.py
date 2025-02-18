import matplotlib.pyplot as plt
import numpy as np

decades = ['60s', '70s', '80s', '90s', '00s']
genres = ['Fic', 'Non-fic', 'Sci-Fi', 'Mystery', 'Romance', 'Fantasy']

publication_counts = {
    'Fiction': [20, 25, 30, 28, 40],
    'Non-fiction': [10, 15, 25, 35, 45],
    'Science Fiction': [5, 10, 15, 20, 25],
    'Mystery': [8, 12, 18, 22, 30],
    'Romance': [12, 18, 22, 24, 35],
    'Fantasy': [3, 7, 12, 18, 26]
}

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['royalblue', 'seagreen', 'coral', 'goldenrod', 'violet', 'mediumpurple']

# Prepare data for stacked histogram
stacked_data = np.array(list(publication_counts.values()))

# Plot stacked histogram
ax.hist(stacked_data.T, bins=np.arange(len(decades) + 1) - 0.5, stacked=True, color=colors)

ax.set_title('Book Genre Popularity Over Decades', fontsize=16, fontweight='bold')
ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('# Books', fontsize=12)
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, fontsize=10, rotation=45, ha='right')
ax.legend(publication_counts.keys(), title="Genres")
plt.tight_layout()
plt.show()