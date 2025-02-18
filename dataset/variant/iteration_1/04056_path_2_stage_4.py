import numpy as np
import matplotlib.pyplot as plt

# Data: Monthly Sales (2022)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Define sales data in thousand units
vanilla_sales = np.array([12, 15, 13, 14, 18, 22, 30, 28, 25, 20, 18, 16])
chocolate_sales = np.array([10, 12, 11, 13, 15, 17, 25, 23, 19, 17, 16, 15])
strawberry_sales = np.array([8, 10, 9, 10, 11, 12, 20, 18, 15, 13, 12, 11])
cookies_cream_sales = np.array([5, 6, 5, 6, 8, 9, 14, 13, 12, 10, 9, 8])

sales_data = [vanilla_sales, chocolate_sales, strawberry_sales, cookies_cream_sales]
colors = ['#FFDDC1', '#D4E157', '#FF80AB', '#FFC107']

fig, ax = plt.subplots(figsize=(14, 8))

# Plotting grouped bar chart
n_flavors = len(sales_data)
bar_width = 0.15
x_indices = np.arange(len(months))

for i, (sales, color) in enumerate(zip(sales_data, colors)):
    ax.bar(x_indices + i * bar_width, sales, width=bar_width, color=color)

ax.set_xticks(x_indices + bar_width * (n_flavors - 1) / 2)
ax.set_xticklabels(months)

plt.tight_layout()
plt.show()