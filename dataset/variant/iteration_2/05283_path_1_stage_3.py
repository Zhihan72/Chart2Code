import matplotlib.pyplot as plt
import numpy as np

weeks = np.arange(1, 53)

sales_apples = [2, 3, 5, 6, 7, 8, 9, 10, 12, 14, 15, 17, 18, 19, 21, 22, 23, 25, 30, 35, 40, 42, 45, 48, 50, 45, 42, 38, 32, 28, 25, 22, 20, 18, 15, 13, 12, 10, 8, 7, 6, 5, 4, 3, 3, 3, 2.5, 2.5, 2, 2, 1.5, 1.5]
sales_bananas = [3, 3, 3, 3, 4, 4, 4, 4.5, 4.5, 4.5, 4.5, 4.5, 5, 5, 5, 5, 5, 5.5, 6, 6, 6.5, 6.5, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
sales_cherries = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 7, 10, 15, 20, 30, 35, 40, 45, 42, 38, 32, 30, 28, 25, 22, 21, 20, 17, 15, 12, 10, 8, 7, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2]
sales_dates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 40, 50, 60, 70, 80, 60, 40, 10, 5, 5, 5, 5, 5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

sales_data = np.vstack([sales_apples, sales_bananas, sales_cherries, sales_dates])

# Shuffled the colors: originally it was ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
colors = ['#66b3ff', '#99ff99', '#ffcc99', '#ff9999']

fig, ax = plt.subplots(figsize=(14, 8))

ax.stackplot(weeks, sales_data, colors=colors, alpha=0.8)

ax.set_xticks(np.arange(1, 53, 4))
ax.set_xlim(1, 52)
ax.set_ylim(0, 100)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()