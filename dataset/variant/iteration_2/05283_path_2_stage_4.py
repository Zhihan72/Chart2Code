import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

sales_apples = [2, 3, 5, 7, 7, 9, 8, 11, 13, 14, 14, 17, 19, 18, 20, 22, 24, 26, 30, 37, 39, 43, 44, 47, 51, 46, 41, 39, 33, 29, 24, 21, 19, 17, 16, 14, 11, 9, 7, 6, 5, 6, 4, 3, 2, 3, 2.5, 3, 1.5, 2, 1.5, 1]
sales_bananas = [3, 3, 3, 4, 4, 4, 5, 5, 4.5, 4.5, 4.5, 4, 5, 5, 5, 5, 4.5, 5.5, 5.5, 6, 6.5, 6, 7, 7, 6.5, 7, 7, 7, 7.5, 7, 6.5, 7, 7.5, 7, 7, 7, 6.5, 7, 7, 7, 7, 7, 7, 7, 7, 6.5, 7, 7, 7, 7, 7, 7]
sales_cherries = [2, 2, 2, 3, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2, 3, 4, 5, 8, 9, 14, 18, 28, 30, 38, 44, 43, 35, 30, 29, 27, 24, 21, 20, 18, 16, 14, 11, 10, 9, 7, 5, 5, 4, 2, 3, 2, 2, 2, 3, 2, 1.5, 2]
sales_dates = [1.5, 1, 1, 1.5, 1, 1, 2, 1.5, 1, 1, 1, 1, 1, 1, 2, 42, 50, 62, 75, 78, 61, 41, 12, 6, 5, 5, 5, 6, 5, 5, 3.5, 3, 3, 2.5, 2.5, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1.5]

sales_data = np.vstack([sales_apples, sales_bananas, sales_cherries, sales_dates])

# New set of colors for improved clarity
colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(weeks, sales_data, colors=colors, alpha=0.9)

ax.set_xticks(np.arange(1, 53, 4))
ax.set_xlim(1, 52)
ax.set_ylim(0, 100)

plt.tight_layout()

plt.show()