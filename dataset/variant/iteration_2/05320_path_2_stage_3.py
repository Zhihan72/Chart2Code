import matplotlib.pyplot as plt
import numpy as np

product_categories = ['Smartphones', 'Laptops', 'Wearables', 'Accessories']
sales_data = np.array([
    [500, 600, 700, 800, 850, 900],
    [450, 475, 500, 520, 570, 600],
    [200, 220, 250, 270, 290, 310],
    [150, 180, 190, 200, 220, 230]
])
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.15
x_positions = np.arange(len(months))
bar_color = 'steelblue'  # Consistent color for all bars

for i, category in enumerate(product_categories):
    ax.bar(x_positions + i * bar_width, sales_data[i], bar_width, color=bar_color)

ax.set_xlabel('Months', fontsize=14, weight='bold')
ax.set_ylabel('Units Sold', fontsize=14, weight='bold')
ax.set_title('Startup Monthly Sales Performance for 2023', fontsize=16, weight='bold', pad=20)
ax.set_xticks(x_positions + bar_width * (len(product_categories) - 1) / 2)
ax.set_xticklabels(months, fontsize=12)

for i, category_data in enumerate(sales_data):
    for j, sale in enumerate(category_data):
        ax.text(x_positions[j] + i * bar_width, sale + 5, f'{sale}', ha='center', va='bottom', fontsize=10, rotation=90)

plt.tight_layout()
plt.show()