import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
lettuce_varieties = ['Romaine', 'Butterhead', 'Iceberg', 'Arugula']

sales_data = np.array([
    [10, 12, 14, 15, 18, 20, 22, 23, 21, 19, 15, 11],
    [8, 9, 10, 12, 14, 17, 19, 18, 16, 14, 10, 9],
    [9, 11, 13, 14, 16, 18, 20, 21, 20, 18, 13, 10],
    [5, 6, 8, 10, 12, 14, 16, 17, 15, 12, 8, 6]
])

colors = ['#FF5722', '#673AB7', '#E91E63', '#03A9F4']  # Changed colors

fig, axs = plt.subplots(2, 1, figsize=(12, 10), constrained_layout=True)

for idx, variety in enumerate(lettuce_varieties):
    axs[0].bar(months, sales_data[idx], color=colors[idx], alpha=0.85, label=variety, edgecolor='black', hatch="/")  # Added edgecolor and hatching

axs[0].set_title('Monthly Lettuce Sales in 2023', fontsize=18, weight='bold', style='italic')  # Changed title style
axs[0].set_xlabel('Month', fontsize=14)
axs[0].set_ylabel('Sales (Thousands of Heads)', fontsize=14)
axs[0].legend(title='Variety', loc='lower left', fontsize=10)  # Moved and styled legend

axs[0].grid(True, which='both', linestyle='-.', linewidth=0.75, color='gray')  # Altered grid style

cumulative_sales_data = np.cumsum(sales_data, axis=0)
bottom = np.zeros(len(months))
for idx, (variety, color) in enumerate(zip(lettuce_varieties, colors)):
    axs[1].bar(months, sales_data[idx], bottom=bottom, color=color, alpha=0.85, label=variety, edgecolor='black', linestyle='dotted', hatch='\\')  # Added linestyle and changed hatching
    bottom += sales_data[idx]

axs[1].set_title('Portion of Lettuce Varieties Sold Each Month in 2023', fontsize=18, weight='bold', style='italic')  # Changed title style
axs[1].set_xlabel('Month', fontsize=14)
axs[1].set_ylabel('Sales (Thousands of Heads)', fontsize=14)
axs[1].legend(title='Variety', loc='upper center', bbox_to_anchor=(0.5, -0.10), ncol=4, fontsize=10)  # Adjusted legend layout

axs[1].grid(False)  # Removed grid from subplot

plt.tight_layout()
plt.show()