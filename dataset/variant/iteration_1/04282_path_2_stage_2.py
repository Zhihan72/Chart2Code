import matplotlib.pyplot as plt
import numpy as np

genres = ['Fiction', 'Non-Fiction', 'Mystery', 'Fantasy', 'Biography']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# Data (number of books sold in thousands)
books_sold = [
    [120, 150, 180, 170],  # Fiction
    [130, 160, 140, 150],  # Non-Fiction
    [100, 110, 130, 125],  # Mystery
    [140, 135, 145, 160],  # Fantasy
    [90, 95, 100, 105]     # Biography
]

books_sold = np.array(books_sold)

fig, ax = plt.subplots(figsize=(12, 7))

bar_height = 0.15
y_indices = np.arange(len(quarters))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
for i in range(len(genres)):
    ax.barh(y_indices + i * bar_height, books_sold[i], height=bar_height, color=colors[i])

# Removed text annotations
# Removed axis labels and title
ax.set_yticks(y_indices + bar_height * 2)
ax.set_yticklabels([''] * len(quarters))  # Removed group labels
plt.yticks(rotation=20)

ax.legend(frameon=False)  # Removed legend title

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()