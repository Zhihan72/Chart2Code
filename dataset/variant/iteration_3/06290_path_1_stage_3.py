import matplotlib.pyplot as plt
import numpy as np

publishers = ['Publisher A', 'Publisher C', 'Publisher D']
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Historical']

data = np.array([
    [120, 150, 80, 100, 90],     # Publisher A
    [90, 130, 110, 95, 85],      # Publisher C
    [170, 160, 150, 140, 130]    # Publisher D
])

fig, ax = plt.subplots(figsize=(12, 8))
colors = ['#32CD32', '#FFD700', '#FF6347']
positions = np.arange(len(genres))

bottom = np.zeros(len(genres))

# Create a stacked bar chart
for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    ax.bar(positions, data[idx], width=0.6, color=color, label=publisher, bottom=bottom, alpha=0.75)
    bottom += data[idx]

ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Number of Publications', fontsize=12)
ax.set_title('Annual Book Publications by Genre\nAcross Major Publishers', fontsize=14, fontweight='bold')
ax.set_xticks(positions)
ax.set_xticklabels(genres)

ax.legend(title='Publishers', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

for idx, genre_position in enumerate(positions):
    cumulative_height = 0
    for publisher_data, color in zip(data[:, idx], colors):
        cumulative_height += publisher_data
        ax.text(genre_position, cumulative_height - publisher_data / 2, str(publisher_data),
                ha='center', va='center', fontsize=10, color=color)

plt.tight_layout()
plt.show()