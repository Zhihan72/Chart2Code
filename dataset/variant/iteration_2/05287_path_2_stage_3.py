import matplotlib.pyplot as plt
import numpy as np

decades = np.arange(1960, 2021, 10)

fiction_books = [220, 180, 310, 150, 280, 200, 250]
non_fiction_books = [140, 220, 160, 100, 180, 200, 120]

fiction_revenue = [700, 550, 800, 450, 750, 500, 600]
non_fiction_revenue = [500, 600, 450, 300, 350, 550, 400]

fig, ax1 = plt.subplots(figsize=(14, 8))

bar_width = 3
ax1.bar(decades - bar_width, fiction_books, width=bar_width, color='#6a5acd', alpha=0.7)
ax1.bar(decades, non_fiction_books, width=bar_width, color='#ff6347', alpha=0.7)

ax2 = ax1.twinx()
ax2.bar(decades - bar_width, fiction_revenue, width=bar_width, color='#6a5acd', alpha=0.3)
ax2.bar(decades, non_fiction_revenue, width=bar_width, color='#ff6347', alpha=0.3)

ax1.set_xlabel("Decades", fontsize=12)
ax1.set_ylabel("Books Published", fontsize=12)
ax2.set_ylabel("Revenue (Millions)", fontsize=12)

plt.tight_layout()
plt.show()