import matplotlib.pyplot as plt
import numpy as np

children_books = [14, 12, 13, 9, 11, 11, 14, 16, 15, 10, 10]
teens_books = [6, 11, 5, 7, 12, 8, 9, 5, 6, 10, 7]
adults_books = [17, 21, 15, 19, 16, 18, 12, 18, 15, 14, 14]
middle_aged_books = [11, 12, 13, 8, 10, 14, 7, 12, 10, 11, 9]
seniors_books = [7, 5, 5, 6, 8, 6, 5, 6, 5, 7, 4]

data = [children_books, teens_books, adults_books, middle_aged_books, seniors_books]

fig, ax = plt.subplots(figsize=(14, 9))
box = ax.boxplot(data, vert=False, patch_artist=True, labels=['']*len(data))

colors = ['lightblue', 'lightgreen', 'salmon', 'lightcoral', 'lightpink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

ax.grid(True, linestyle='-', alpha=0.7, axis='x')

plt.gca().set_aspect('auto', adjustable='box')
plt.tight_layout()

ax2 = ax.twiny()
book_trend = [np.mean(group) for group in data]
ax2.plot(np.arange(1, len(data)+1), book_trend, 's-', color='mediumpurple', linewidth=2)

plt.show()