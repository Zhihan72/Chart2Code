import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']

categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']
sales_data = {
    'Electronics': [400, 500, 300, 450],
    'Clothing': [350, 400, 420, 380],
    'Home & Kitchen': [300, 350, 400, 370],
    'Sports': [200, 250, 150, 200],
}

total_sales = {category: sum(sales) for category, sales in sales_data.items()}

colors = ['#dd1c77','#8c96c6','#72c58f','#fbb4ae']

sorted_categories = sorted(total_sales, key=total_sales.get, reverse=True)
sorted_colors = [x for _, x in sorted(zip(categories, colors), key=lambda pair: total_sales[pair[0]], reverse=True)]
sorted_sales_data = [sales_data[category] for category in sorted_categories]

fig, (ax_bar, ax_curve) = plt.subplots(2, 1, figsize=(12, 10))

bar_width = 0.15
x_positions = np.arange(len(quarters))

for i, category_sales in enumerate(sorted_sales_data):
    ax_bar.bar(x_positions + i * bar_width, category_sales, bar_width, color=sorted_colors[i])

ax_bar.set_xticks(x_positions + bar_width * (len(categories) - 1) / 2)
ax_bar.set_xticklabels([])  # Remove x-tick labels
ax_bar.yaxis.grid(True, linestyle='--', alpha=0.5)

for i, category_sales in enumerate(sorted_sales_data):
    for j, value in enumerate(category_sales):
        if value > 0:
            ax_bar.text(x_positions[j] + i * bar_width, value + 10, f'{value}', ha='center', va='bottom', fontsize=9, color='black')

for i, category in enumerate(sorted_categories):
    ax_curve.plot(quarters, sales_data[category], marker='o', linestyle='-', color=sorted_colors[i])

ax_curve.set_xticklabels([])  # Remove x-tick labels
ax_curve.yaxis.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()