import matplotlib.pyplot as plt
import numpy as np

coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']
sales_Q1 = [150, 200, 180, 220, 210]

# Sort sales data and coffee_types together in descending order
sorted_sales_indices = np.argsort(sales_Q1)[::-1]
sorted_coffee_types = [coffee_types[i] for i in sorted_sales_indices]
sorted_sales_Q1 = [sales_Q1[i] for i in sorted_sales_indices]

x = np.arange(len(sorted_coffee_types))
fig, ax = plt.subplots(figsize=(12, 7))

single_color = '#3498db'

# Plot sorted sales data
ax.bar(x, sorted_sales_Q1, color=single_color)

ax.set_xticks(x)
ax.set_xticklabels(sorted_coffee_types)

ax.yaxis.grid(True, linestyle=':', linewidth=1, alpha=0.3)

plt.tight_layout()
plt.show()