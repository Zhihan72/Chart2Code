import matplotlib.pyplot as plt
import numpy as np

publishers = ['Publisher A', 'Publisher C', 'Publisher D']
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Historical']

data = np.array([
    [120, 150, 80, 100, 90],     # Publisher A
    [90, 130, 110, 95, 85],      # Publisher C
    [170, 160, 150, 140, 130]    # Publisher D
])

years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']

fig, ax = plt.subplots(figsize=(12, 8))

num_years = len(years)
num_publishers = data.shape[0]

bar_width = 0.15
positions = np.arange(len(genres))

# Shuffled colors for publishers
colors = ['#32CD32', '#FFD700', '#FF6347']

for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    bar_positions = positions + idx * bar_width
    ax.bar(bar_positions, data[idx], width=bar_width, color=color, label=publisher, alpha=0.75)

ax.set_xlabel('Book Genres', fontsize=12)
ax.set_ylabel('Number of Publications', fontsize=12)
ax.set_title('Annual Book Publications by Genre\nAcross Major Publishers', fontsize=14, fontweight='bold')
ax.set_xticks(positions + bar_width * (num_publishers - 1) / 2)
ax.set_xticklabels(genres)

ax.legend(title='Publishers', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

for idx, (publisher, color) in enumerate(zip(publishers, colors)):
    bar_positions = positions + idx * bar_width
    for x, y in zip(bar_positions, data[idx]):
        plt.text(x, y + 2, y, ha='center', va='bottom', fontsize=10, color=color)

plt.tight_layout()
plt.show()