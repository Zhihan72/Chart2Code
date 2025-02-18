import matplotlib.pyplot as plt
import numpy as np

# Remove 'Books' data group
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

bars1 = ax1.bar(x_pos, sales, color=colors, alpha=0.7, label='Sales (in thousands)')
ax1.set_xlabel('Product Categories')
ax1.set_ylabel('Sales (in thousands)', color='black')
ax1.set_title('Q1 Sales Performance & Customer Satisfaction Comparison', fontsize=14, fontweight='bold')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(categories, rotation=45, ha='right')

ax2 = ax1.twinx()
line2, = ax2.plot(x_pos, satisfaction_rates, 'o-', color='green', label='Customer Satisfaction', markersize=10)
ax2.set_ylabel('Customer Satisfaction Rate (%)', color='green')

for i, v in enumerate(sales):
    ax1.text(i, v + 3, f"{v}", ha='center', fontweight='bold')

for i, v in enumerate(satisfaction_rates):
    ax2.text(i, v + 1, f"{v}%", ha='center', fontweight='bold', color='green')

lns = [bars1[0], line2]
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper left')

fig.tight_layout()
plt.show()