import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2021, 10)
fiction_books = [150, 180, 200, 220, 250, 280, 310]
non_fiction_books = [100, 120, 140, 160, 180, 200, 220]

fiction_revenue = [450, 500, 550, 600, 700, 750, 800]
non_fiction_revenue = [300, 350, 400, 450, 500, 550, 600]

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

ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Number of Books Published", fontsize=12)
ax2.set_ylabel("Revenue in Millions (USD)", fontsize=12)

plt.show()