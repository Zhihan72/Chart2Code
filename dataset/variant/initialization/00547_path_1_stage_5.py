import matplotlib.pyplot as plt
import numpy as np

all_books = [11, 12, 15, 9, 10, 
             5, 7, 8, 6, 10, 7, 
             12, 15, 14, 17, 19]

fig, ax = plt.subplots(figsize=(8, 6))

box = ax.boxplot(all_books, vert=True, patch_artist=True)

# Set the color of the box
box_color = plt.cm.viridis(0.5)
box['boxes'][0].set_facecolor(box_color)

# Eliminate stylistic elements
ax.set_xticks([])
ax.set_yticks([])

plt.show()