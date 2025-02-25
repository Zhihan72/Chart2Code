import matplotlib.pyplot as plt
import numpy as np

quarters = ['Q1', 'Q2', 'Q3', 'Q4']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books']
sales_data = {
    'Electronics': [400, 500, 300, 450],
    'Clothing': [350, 400, 420, 380],
    'Home & Kitchen': [300, 350, 400, 370],
    'Books': [150, 140, 130, 120],
}

colors = ['#ffb3e6', '#99ff99', '#ffcc99', '#c2c2f0']

fig, ax_bar = plt.subplots(figsize=(9, 8))

y = np.arange(len(quarters))
bar_height = 0.15

for i, category in enumerate(categories):
    sales = sales_data[category]
    ax_bar.barh(y + i * bar_height, sales, bar_height, color=colors[i], label=category)

ax_bar.set_title("Quarterly Sales 2022", fontsize=16, fontweight='bold', pad=20)
ax_bar.set_ylabel("Qtrs", fontsize=12)
ax_bar.set_xlabel("Units Sold", fontsize=12)
ax_bar.set_yticks(y + bar_height * (len(categories) - 1) / 2)
ax_bar.set_yticklabels(quarters, fontsize=12)
ax_bar.legend(title="Categories", fontsize=10)
ax_bar.xaxis.grid(True, linestyle='--', alpha=0.5)

for i, category in enumerate(categories):
    for j, value in enumerate(sales_data[category]):
        if value > 0:
            ax_bar.text(value + 10, y[j] + i * bar_height, f'{value}', va='center', ha='left', fontsize=9, color='black')

plt.tight_layout()
plt.show()