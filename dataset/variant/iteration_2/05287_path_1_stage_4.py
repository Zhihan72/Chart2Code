import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2021, 10)
fiction_books = [180, 150, 250, 280, 310, 200, 220]
non_fiction_books = [100, 160, 120, 220, 180, 140, 200]

fiction_revenue = [500, 450, 700, 750, 800, 550, 600]
non_fiction_revenue = [300, 450, 350, 600, 500, 400, 550]

sorted_indices_fiction_books = np.argsort(fiction_books)
sorted_decades_fiction_books = decades[sorted_indices_fiction_books]
sorted_fiction_books = np.array(fiction_books)[sorted_indices_fiction_books]
sorted_fiction_revenue = np.array(fiction_revenue)[sorted_indices_fiction_books]

sorted_indices_non_fiction_books = np.argsort(non_fiction_books)
sorted_decades_non_fiction_books = decades[sorted_indices_non_fiction_books]
sorted_non_fiction_books = np.array(non_fiction_books)[sorted_indices_non_fiction_books]
sorted_non_fiction_revenue = np.array(non_fiction_revenue)[sorted_indices_non_fiction_books]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 3
ax1.bar(sorted_decades_fiction_books - bar_width, sorted_fiction_books, width=bar_width, color='#6a5acd', alpha=0.7)
ax1.bar(sorted_decades_non_fiction_books, sorted_non_fiction_books, width=bar_width, color='#ff6347', alpha=0.7)

ax2 = ax1.twinx()
ax2.bar(sorted_decades_fiction_books - bar_width, sorted_fiction_revenue, width=bar_width, color='#6a5acd', alpha=0.3)
ax2.bar(sorted_decades_non_fiction_books, sorted_non_fiction_revenue, width=bar_width, color='#ff6347', alpha=0.3)

plt.show()