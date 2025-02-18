import matplotlib.pyplot as plt
import numpy as np

categories = ["Elec", "Fash", "Home", "Beaut", "Toys", "Books", "Sports", "Grocery"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_data = [
    [120, 110, 105, 100, 95, 110],
    [80, 85, 90, 85, 80, 75],
    [50, 55, 60, 65, 70, 75],
    [30, 35, 40, 45, 50, 55],
    [20, 30, 25, 35, 30, 40],
    [10, 15, 20, 25, 30, 35],
    [40, 45, 50, 55, 60, 65],
    [100, 120, 110, 130, 120, 140]
]

sales_data = np.sum(sales_data, axis=1)
sorted_indices = np.argsort(sales_data)  # To get ascending order. Use -sales_data for descending.

sorted_categories = [categories[i] for i in sorted_indices]
sorted_sales_data = np.array([sales_data[i] for i in sorted_indices])

fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(sorted_categories, sorted_sales_data, color='#66b3ff', edgecolor='black', linestyle='-')

ax.set_title('Total Sales by Category', fontsize=16, pad=20)
ax.set_ylabel('Total Sales (k USD)', fontsize=14)
ax.set_xticklabels(sorted_categories, rotation=45, ha='right', fontsize=12)

ax.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.9)
plt.tight_layout()

plt.show()