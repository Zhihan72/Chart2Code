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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

bar_height = 0.2
bar_positions = np.arange(len(quarters))

for i, category in enumerate(categories):
    ax1.barh(bar_positions + i * bar_height, sales_data[i, :], height=bar_height, label=category)

ax1.set_title('Quarterly Sales Performance of Product Categories\nin Department Store (in Thousands of Dollars)', fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel('Quarters', fontsize=12)
ax1.set_xlabel('Sales ($)', fontsize=12)
ax1.set_yticks(bar_positions + bar_height * 1.5)
ax1.set_yticklabels(quarters, fontsize=10)
ax1.legend(title='Product Category', loc='upper left', bbox_to_anchor=(1, 1))

annual_sales = np.sum(sales_data, axis=1)

ax2.barh(categories, annual_sales, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])

for idx, category in enumerate(categories):
    ax2.annotate(f'{annual_sales[idx]:,}', 
                 xy=(annual_sales[idx], idx), 
                 xytext=(3, 0),
                 textcoords="offset points",
                 ha='left', va='center', fontsize=10, color='black')

ax2.set_title('Annual Sales Performance of Product Categories\nin Department Store (in Thousands of Dollars)', fontsize=16, fontweight='bold', pad=20)
ax2.set_ylabel('Product Categories', fontsize=12)
ax2.set_xlabel('Sales ($)', fontsize=12)

plt.tight_layout()
plt.show()