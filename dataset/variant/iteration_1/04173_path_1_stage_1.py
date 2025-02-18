import matplotlib.pyplot as plt
import numpy as np

categories = ['Electronics', 'Clothing', 'Groceries', 'Household Items', 'Books']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

sales_data = np.array([
    [120, 130, 115, 140],
    [80, 90, 85, 100],
    [150, 160, 155, 170],
    [70, 75, 65, 80],
    [50, 55, 60, 65],
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

bar_width = 0.2
bar_positions = np.arange(len(categories))

colors = ['skyblue', 'lightcoral', 'lightgreen', 'khaki']
hatches = ['/', '\\', 'o', '-', '|']

for i, quarter in enumerate(quarters):
    ax1.bar(bar_positions + i * bar_width, sales_data[:, i], width=bar_width, color=colors[i % len(colors)], label=quarter, hatch=hatches[i % len(hatches)])

ax1.set_title('Quarterly Sales Performance\n(in Thousands of Dollars)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Product Categories', fontsize=12)
ax1.set_ylabel('Sales ($K)', fontsize=12)
ax1.set_xticks(bar_positions + bar_width * 1.5)
ax1.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)

ax1.legend(title='Quarter', loc='best', shadow=True, frameon=False)
ax1.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5, color='gray')

annual_sales = np.sum(sales_data, axis=1)
ax2.bar(categories, annual_sales, color=['#17becf', '#bcbd22', '#e377c2', '#7f7f7f', '#8c564b'], linestyle='--', edgecolor='gray')

for idx, category in enumerate(categories):
    ax2.annotate(f'{annual_sales[idx]:,}', 
                 xy=(idx, annual_sales[idx]), 
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, color='black')

ax2.set_title('Annual Sales Performance\n(in Thousands of Dollars)', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Product Categories', fontsize=12)
ax2.set_ylabel('Sales ($K)', fontsize=12)
ax2.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()