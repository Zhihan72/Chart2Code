import matplotlib.pyplot as plt
import numpy as np

flavors = ['Strawberry', 'Banana', 'Mango']
sales_data = {
    'Strawberry': [150, 120, 130, 200, 180, 240, 250, 220, 210, 190, 160, 180],
    'Banana': [100, 80, 75, 95, 85, 105, 115, 110, 108, 102, 92, 104],
    'Mango': [90, 70, 65, 85, 75, 95, 100, 98, 94, 88, 72, 90]
}

total_sales = {flavor: sum(sales) for flavor, sales in sales_data.items()}
sorted_flavors = sorted(total_sales, key=total_sales.get, reverse=True)
sorted_sales_data = [sales_data[flavor] for flavor in sorted_flavors]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months_idx = np.arange(len(months))

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.25
single_color = 'skyblue'  # Consistent color for all bars

for i, flavor in enumerate(sorted_flavors):
    ax.bar(months_idx + i * bar_width, sorted_sales_data[i],
           width=bar_width, label=flavor, alpha=0.7, color=single_color)

ax.set_title('Smoothie Sales at Local Cafe', fontsize=16, fontweight='bold')
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Smoothies Sold', fontsize=14)
ax.set_xticks(months_idx + bar_width)
ax.set_xticklabels(months, fontsize=10, rotation=45)

ax.legend(title='Flavors', fontsize=10, title_fontsize='11', loc='upper right', shadow=True)
ax.grid(True, linestyle='--', alpha=0.4)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(1.5)
ax.set_ylim(0, 300)

for i, sales in enumerate(sorted_sales_data):
    for j, value in enumerate(sales):
        ax.text(j + i * bar_width, value + 5, str(value),
                ha='center', va='bottom', fontsize=8, color='navy')

plt.tight_layout()
plt.show()