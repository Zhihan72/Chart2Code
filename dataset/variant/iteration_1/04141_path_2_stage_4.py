import matplotlib.pyplot as plt
import numpy as np

product_lines = [
    'Smartphones', 'Laptops', 'Accessories',
    'Services', 'Software', 'Wearables', 'AI Solutions'
]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

revenue_data = [
    [45.6, 48.2, 50.1, 52.3],
    [30.8, 33.6, 35.2, 37.8],
    [10.5, 12.0, 11.8, 13.2],
    [14.0, 15.8, 16.5, 17.9],
    [20.1, 21.5, 22.4, 23.9],
    [9.2, 10.3, 10.9, 12.0],
    [18.4, 19.6, 20.2, 21.5]
]

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A4', '#FFC133', '#33FFF6', '#F633FF']

total_revenue = [sum(revenue) for revenue in revenue_data]
sorted_indices = np.argsort(total_revenue)
sorted_revenue_data = [revenue_data[i] for i in sorted_indices]
sorted_colors = [colors[i] for i in sorted_indices]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))
bar_width = 0.1
bar_positions = np.arange(len(quarters))

for i in range(len(sorted_revenue_data)):
    ax1.bar(bar_positions + i * bar_width, sorted_revenue_data[i], color=sorted_colors[i], width=bar_width)

for i in range(len(sorted_revenue_data)):
    for j, value in enumerate(sorted_revenue_data[i]):
        ax1.text(j + i * bar_width, value + 0.5, f"{value:.1f}", ha='center', va='bottom', fontsize=10, color='black')

ax2.barh(product_lines, total_revenue, color=colors)

for i, total in enumerate(total_revenue):
    ax2.text(total + 1, i, f"{total:.1f}", va='center', ha='left', fontsize=12, color='black')

plt.tight_layout()
plt.show()