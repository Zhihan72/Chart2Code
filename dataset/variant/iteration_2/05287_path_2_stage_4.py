import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2021, 10)

fiction_books = [220, 180, 310, 150, 280, 200, 250]
non_fiction_books = [140, 220, 160, 100, 180, 200, 120]

fiction_revenue = [700, 550, 800, 450, 750, 500, 600]
non_fiction_revenue = [500, 600, 450, 300, 350, 550, 400]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_height = 3
ax1.barh(decades - bar_height / 2, fiction_books, height=bar_height, color='#6a5acd', alpha=0.7, label="Fiction Books")
ax1.barh(decades + bar_height / 2, non_fiction_books, height=bar_height, color='#ff6347', alpha=0.7, label="Non-Fiction Books")

ax2 = ax1.twiny()
ax2.barh(decades - bar_height / 2, fiction_revenue, height=bar_height, color='#6a5acd', alpha=0.3, label="Fiction Revenue")
ax2.barh(decades + bar_height / 2, non_fiction_revenue, height=bar_height, color='#ff6347', alpha=0.3, label="Non-Fiction Revenue")

ax1.set_ylabel("Decades", fontsize=12)
ax1.set_xlabel("Books Published", fontsize=12)
ax2.set_xlabel("Revenue (Millions)", fontsize=12)

ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()