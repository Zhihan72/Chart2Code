import matplotlib.pyplot as plt
import numpy as np

influence_matrix = np.array([
    [7, 5, 3, 4, 6],
    [6, 8, 2, 5, 7],
    [4, 7, 5, 3, 6],
    [3, 4, 9, 8, 5],
    [5, 6, 4, 7, 8],
    [6, 5, 7, 3, 9],
    [8, 3, 6, 9, 4],
])

fig, ax = plt.subplots(figsize=(10, 8))

cax = ax.imshow(influence_matrix, cmap='plasma', aspect='auto', interpolation='nearest')

ax.set_xticks([])
ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

for i in range(len(influence_matrix)):
    for j in range(len(influence_matrix[0])):
        ax.text(j, i, influence_matrix[i, j], ha='center', va='center', color='darkred', fontsize=12)

plt.tight_layout()

plt.show()