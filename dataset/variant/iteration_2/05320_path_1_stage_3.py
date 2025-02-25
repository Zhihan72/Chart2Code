import matplotlib.pyplot as plt
import numpy as np

product_categories = ['Smartphones', 'Laptops', 'Tablets', 'Accessories']
sales_data = np.array([
    [500, 600, 700, 800, 850, 900],
    [450, 475, 500, 520, 570, 600],
    [300, 320, 350, 370, 410, 450],
    [150, 180, 190, 200, 220, 230]
])

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.2
x_positions = np.arange(len(months))

marker_shapes = ['o', 's', 'D', '^']  # Manually shuffled marker shapes
linestyles = ['-', '--', '-.', ':']   # Manually shuffled line styles
colors = ['purple', 'brown', 'cyan', 'magenta']  # Manually shuffled colors

for i, category in enumerate(product_categories):
    ax.bar(x_positions + i * bar_width, sales_data[i], bar_width, label=category,
           edgecolor=colors[i], linestyle=linestyles[i], hatch=marker_shapes[i])

ax.set_xlabel('Months', fontsize=14)
ax.set_ylabel('Units Sold', fontsize=14)
ax.set_title('Startup Monthly Sales - 2023', fontsize=16)

ax.set_xticks(x_positions + bar_width * (len(product_categories) - 1) / 2)
ax.set_xticklabels(months, fontsize=12)

for i, category_data in enumerate(sales_data):
    for j, sale in enumerate(category_data):
        ax.text(x_positions[j] + i * bar_width, sale + 5, f'{sale}', ha='center', va='bottom', fontsize=10, rotation=90)

ax.legend(title='Product Categories', fontsize=12, title_fontsize='13')
plt.grid(True, linestyle='-', which='major', axis='y', color='lightgrey', alpha=0.7)

plt.tight_layout()
plt.show()