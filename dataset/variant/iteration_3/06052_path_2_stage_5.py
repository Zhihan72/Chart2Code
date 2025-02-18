import matplotlib.pyplot as plt
import numpy as np

# Data setup
categories = ['Electronics', 'Furniture', 'Clothing', 'Toys', 'Groceries']
sales = [150, 90, 130, 120, 170]
satisfaction_rates = [85, 75, 70, 80, 90]

# Sorting the data in descending order of sales
sorted_indices = np.argsort(sales)[::-1]
categories = [categories[i] for i in sorted_indices]
sales = [sales[i] for i in sorted_indices]
satisfaction_rates = [satisfaction_rates[i] for i in sorted_indices]

colors = ['#e6194B', '#f58231', '#ffe119', '#3cb44b', '#42d4f4']
colors = [colors[i] for i in sorted_indices]

fig, ax1 = plt.subplots(figsize=(12, 8))
x_pos = np.arange(len(categories))

# Plotting the bar chart
ax1.bar(x_pos, sales, color=colors, alpha=0.7)
ax1.set_xticks(x_pos)
ax1.set_xticklabels([])  # Remove x-tick labels

# Plotting the line chart
ax2 = ax1.twinx()
ax2.plot(x_pos, satisfaction_rates, 'o-', color='green', markersize=10)

# Tight layout
fig.tight_layout()
plt.show()