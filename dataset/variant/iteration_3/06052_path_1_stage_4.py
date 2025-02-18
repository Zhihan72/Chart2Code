import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Furniture', 'Clothing', 'Books', 'Toys', 'Groceries']
sales = [150, 90, 130, 80, 120, 170]

# Sort sales and categories based on sales in descending order
sorted_indices = np.argsort(sales)[::-1]
sorted_sales = [sales[i] for i in sorted_indices]
sorted_categories = [categories[i] for i in sorted_indices]
colors = ['#2ca02c', '#9467bd', '#1f77b4', '#8c564b', '#ff7f0e', '#d62728']

fig, ax1 = plt.subplots(figsize=(12, 8))

x_pos = np.arange(len(sorted_categories))

ax1.bar(x_pos, sorted_sales, color=colors, alpha=0.7)

# Remove borders
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax1.set_xticks(x_pos)
ax1.set_xticklabels(sorted_categories)

fig.tight_layout()
plt.show()