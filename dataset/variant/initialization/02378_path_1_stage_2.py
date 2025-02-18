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
colors = ['royalblue', 'seagreen', 'coral', 'goldenrod', 'violet']

fig, ax = plt.subplots(figsize=(12, 8))

# Transpose data for stacking
data = np.array(data)  # Convert data to numpy array
data = np.transpose(data)  # Transpose to match the decades as rows

# Create a stacked histogram
ax.hist(data, bins=np.arange(len(decades) + 1) - 0.5, stacked=True, label=genres, color=colors, alpha=0.8)

ax.set_xlabel('Decades', fontsize=12)
ax.set_ylabel('Number of Books Published', fontsize=12)
ax.set_xticks(np.arange(len(decades)))
ax.set_xticklabels(decades, fontsize=10, rotation=45, ha='right')
ax.legend(title='Genres', fontsize=10)
plt.tight_layout()
plt.show()