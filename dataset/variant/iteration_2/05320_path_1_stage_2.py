import matplotlib.pyplot as plt
import numpy as np

# Define product categories
product_categories = ['Smartphones', 'Laptops', 'Tablets', 'Accessories']

# Monthly sales data (units sold) for each category over six months
sales_data = np.array([
    [500, 600, 700, 800, 850, 900],  # Smartphones
    [450, 475, 500, 520, 570, 600],  # Laptops
    [300, 320, 350, 370, 410, 450],  # Tablets
    [150, 180, 190, 200, 220, 230]   # Accessories
])

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
x_positions = np.arange(len(months))

# Define colors and shuffle them
colors = ['red', 'blue', 'green', 'orange']
# Manually shuffling colors
shuffled_colors = ['green', 'orange', 'red', 'blue']

# Plot bars with shuffled colors
for i, category in enumerate(product_categories):
    ax.bar(x_positions + i * bar_width, sales_data[i], bar_width, label=category, color=shuffled_colors[i])

ax.set_xlabel('Months', fontsize=14, weight='bold')
ax.set_ylabel('Units Sold', fontsize=14, weight='bold')
ax.set_title('Startup Monthly Sales Performance for 2023', fontsize=16, weight='bold', pad=20)
ax.set_xticks(x_positions + bar_width * (len(product_categories) - 1) / 2)
ax.set_xticklabels(months, fontsize=12)

for i, category_data in enumerate(sales_data):
    for j, sale in enumerate(category_data):
        ax.text(x_positions[j] + i * bar_width, sale + 5, f'{sale}', ha='center', va='bottom', fontsize=10, rotation=90)

ax.legend(title='Product Categories', fontsize=12, title_fontsize='13', frameon=True)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
plt.tight_layout()
plt.show()