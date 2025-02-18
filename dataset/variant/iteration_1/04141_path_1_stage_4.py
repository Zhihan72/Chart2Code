import matplotlib.pyplot as plt
import numpy as np

product_lines = ['Software', 'Laptops', 'Smartphones', 'Services', 'Accessories']
quarters = ['Q3', 'Q1', 'Q4', 'Q2']

revenue_data = [
    [50.1, 45.6, 52.3, 48.2],  
    [35.2, 30.8, 37.8, 33.6],  
    [11.8, 10.5, 13.2, 12.0],  
    [16.5, 14.0, 17.9, 15.8],  
    [22.4, 20.1, 23.9, 21.5] 
]

sorted_revenue_data = [
    [(2, 52.3), (0, 50.1), (4, 23.9), (3, 17.9), (1, 37.8)], 
    [(2, 45.6), (0, 45.6), (4, 20.1), (3, 14.0), (1, 30.8)],
    [(2, 52.3), (0, 50.1), (4, 23.9), (3, 17.9), (1, 37.8)],
    [(2, 45.6), (0, 48.2), (4, 21.5), (3, 15.8), (1, 33.6)]
]

colors = ['#3357FF', '#33FF57', '#FF5733', '#FF33A4', '#FFC133']

fig, axs = plt.subplots(2, 1, figsize=(12, 14))
ax1, ax2 = axs

bar_width = 0.15
bar_positions = np.arange(len(product_lines))

for quarter, data in enumerate(sorted_revenue_data):
    for i, (idx, revenue) in enumerate(data):
        ax1.bar(np.array([quarter]) * 1.5, revenue, color=colors[idx], width=bar_width, edgecolor='grey')
        ax1.text(quarter * 1.5, revenue + 0.5, f"{revenue:.1f}", ha='center', va='bottom', fontsize=10, color='black')

ax1.set_title('Revenue Analysis of Quarters - 2023', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Quarter Periods', fontsize=14)
ax1.set_ylabel('Earnings (Mil. USD)', fontsize=14)
ax1.set_xticks(np.arange(len(quarters)) * 1.5)
ax1.set_xticklabels(quarters)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

total_revenue = [211.7, 137.4, 196.2, 92.1, 47.5]
sorted_product_lines = ['Software', 'Accessories', 'Smartphones', 'Laptops', 'Services']
sorted_colors = ['#3357FF', '#FF33A4', '#FF5733', '#33FF57', '#FFC133']

ax2.barh(sorted_product_lines, total_revenue, color=sorted_colors, edgecolor='grey')

ax2.set_title('Annual Revenue by Product - 2023', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Total Revenue (Mil. USD)', fontsize=14)
ax2.set_ylabel('Product Categories', fontsize=14)

for i, total in enumerate(total_revenue):
    ax2.text(total + 1, i, f"{total:.1f}", va='center', ha='left', fontsize=12, color='black')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()