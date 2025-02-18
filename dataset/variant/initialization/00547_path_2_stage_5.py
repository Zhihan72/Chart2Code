import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

children_books = [14, 12, 13, 9, 11, 11, 14, 16, 15, 10, 10]
teens_books = [6, 11, 5, 7, 12, 8, 9, 5, 6, 10, 7]
adults_books = [17, 21, 15, 19, 16, 18, 12, 18, 15, 14, 14]
middle_aged_books = [11, 12, 13, 8, 10, 14, 7, 12, 10, 11, 9]
seniors_books = [7, 5, 5, 6, 8, 6, 5, 6, 5, 7, 4]

data = [children_books, teens_books, adults_books, middle_aged_books, seniors_books]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(data, vert=True, patch_artist=True,
           labels=['Children', 'Teens', 'Adults', 'Middle-aged', 'Seniors'])

ax.set_ylabel('Number of Books')

colors = ['lightblue', 'lightgreen', 'salmon', 'lightcoral', 'lightpink']
# for patch, color in zip(ax['boxes'], colors):
#     patch.set_facecolor(color)
for patch, color in zip(ax.boxplot(data, vert=True)['boxes'], colors):
    patch = mpatches.PathPatch(patch.get_path(), color=color)
    patch.set_facecolor(color)

ax.grid(True, linestyle='-', alpha=0.7, axis='y')

plt.tight_layout()
plt.show()