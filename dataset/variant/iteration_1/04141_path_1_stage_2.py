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

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A4', '#FFC133']

fig, axs = plt.subplots(2, 1, figsize=(12, 14))
ax1, ax2 = axs

bar_width = 0.15
bar_positions = np.arange(len(quarters))

for i, product in enumerate(product_lines):
    ax1.bar(bar_positions + i * bar_width, revenue_data[i], color=colors[i], width=bar_width, edgecolor='grey')

ax1.set_title('TechyGears Quarterly Revenue Analysis for 2023', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Quarters', fontsize=14)
ax1.set_ylabel('Revenue (in Millions USD)', fontsize=14)
ax1.set_xticks(bar_positions + (len(product_lines) - 1) * bar_width / 2)
ax1.set_xticklabels(quarters)

for i, product in enumerate(product_lines):
    for j, value in enumerate(revenue_data[i]):
        ax1.text(j + i * bar_width, value + 0.5, f"{value:.1f}", ha='center', va='bottom', fontsize=10, color='black')

# Removing spines and grid from ax1
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

total_revenue = [sum(revenue) for revenue in revenue_data]
ax2.barh(product_lines, total_revenue, color=colors, edgecolor='grey')

ax2.set_title('Total Annual Revenue by Product Line - 2023', fontsize=16, fontweight='bold', pad=20)
ax2.set_xlabel('Total Revenue (in Millions USD)', fontsize=14)
ax2.set_ylabel('Product Lines', fontsize=14)

for i, total in enumerate(total_revenue):
    ax2.text(total + 1, i, f"{total:.1f}", va='center', ha='left', fontsize=12, color='black')

# Removing spines from ax2
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

plt.tight_layout()
plt.show()