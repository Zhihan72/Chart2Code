import matplotlib.pyplot as plt
import numpy as np

product_lines = ['Smartphones', 'Laptops', 'Accessories', 'Services', 'Software']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

revenue_data = [
    [45.6, 48.2, 50.1, 52.3],  
    [30.8, 33.6, 35.2, 37.8],  
    [10.5, 12.0, 11.8, 13.2],  
    [14.0, 15.8, 16.5, 17.9],  
    [20.1, 21.5, 22.4, 23.9]   
]

# Sort data for each quarter in descending order
sorted_revenue_data = []
for quarter in range(len(quarters)):
    quarterly_data = [revenue[quarter] for revenue in revenue_data]
    sorted_data = sorted(enumerate(quarterly_data), key=lambda x: x[1], reverse=True)
    sorted_indices = [x[0] for x in sorted_data]
    sorted_revenue_data.append(sorted_data)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A4', '#FFC133']

fig, axs = plt.subplots(2, 1, figsize=(12, 14))
ax1, ax2 = axs

bar_width = 0.15
bar_positions = np.arange(len(product_lines))

for quarter, data in enumerate(sorted_revenue_data):
    for i, (idx, revenue) in enumerate(data):
        ax1.bar(np.array([quarter]) * 1.5, revenue, color=colors[idx], width=bar_width, edgecolor='grey')
        ax1.text(quarter * 1.5, revenue + 0.5, f"{revenue:.1f}", ha='center', va='bottom', fontsize=10, color='black')
    
ax1.set_title('TechyGears Quarterly Revenue Analysis (Sorted) - 2023', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Quarters', fontsize=14)
ax1.set_ylabel('Revenue (in Millions USD)', fontsize=14)
ax1.set_xticks(np.arange(len(quarters)) * 1.5)
ax1.set_xticklabels(quarters)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

# Sort total_revenue and product_lines together for descending order
total_revenue_data = sorted(zip(total_revenue, product_lines, colors), reverse=True)
total_revenue, sorted_product_lines, sorted_colors = zip(*total_revenue_data)

ax2.barh(sorted_product_lines, total_revenue, color=sorted_colors, edgecolor='grey')

ax2.set_title('Total Annual Revenue by Product Line (Sorted) - 2023', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Total Revenue (in Millions USD)', fontsize=14)
ax2.set_ylabel('Product Lines', fontsize=14)

for i, total in enumerate(total_revenue):
    ax2.text(total + 1, i, f"{total:.1f}", va='center', ha='left', fontsize=12, color='black')

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()