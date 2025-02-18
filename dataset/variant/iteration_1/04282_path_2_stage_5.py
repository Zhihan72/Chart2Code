import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Biography', 'Science Fiction']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

books_sold = [
    [120, 150, 180, 170],
    [130, 160, 140, 150],
    [100, 110, 130, 125],
    [140, 135, 145, 160],
    [90, 95, 100, 105],
    [110, 115, 120, 130]
]

books_sold = np.array(books_sold)

fig, ax = plt.subplots(figsize=(12, 7))

bar_height = 0.15
y_indices = np.arange(len(quarters))

# New colors for the genres
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#ffff33']
for i in range(len(genres)):
    ax.barh(y_indices + i * bar_height, books_sold[i], height=bar_height, color=colors[i])

ax.set_yticks(y_indices + bar_height * 2.5)
ax.set_yticklabels([''] * len(quarters))

ax.set_axisbelow(True)

plt.tight_layout()
plt.show()