import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
lettuce_varieties = ['Romaine', 'Butterhead', 'Iceberg']

sales_data = np.array([
    [10, 12, 14, 15, 18, 20, 22, 23, 21, 19, 15, 11],
    [8, 9, 10, 12, 14, 17, 19, 18, 16, 14, 10, 9],
    [9, 11, 13, 14, 16, 18, 20, 21, 20, 18, 13, 10]
])

# Shuffled colors assigned manually
colors = ['#E91E63', '#FF5722', '#673AB7']

fig, axs = plt.subplots(2, 1, figsize=(12, 10), constrained_layout=True)

cumulative_sales_data = np.cumsum(sales_data, axis=0)
bottom = np.zeros(len(months))
for idx, (variety, color) in enumerate(zip(lettuce_varieties, colors)):
    axs[0].bar(months, sales_data[idx], bottom=bottom, color=color, alpha=0.85, label=variety, edgecolor='black', linestyle='dotted', hatch='\\')
    bottom += sales_data[idx]

axs[0].set_title('Portion of Lettuce Varieties Sold Each Month in 2023', fontsize=18, weight='bold', style='italic')
axs[0].set_xlabel('Month', fontsize=14)
axs[0].set_ylabel('Sales (Thousands of Heads)', fontsize=14)
axs[0].legend(title='Variety', loc='upper center', bbox_to_anchor=(0.5, -0.10), ncol=3, fontsize=10)
axs[0].grid(False)

for idx, variety in enumerate(lettuce_varieties):
    axs[1].bar(months, sales_data[idx], color=colors[idx], alpha=0.85, label=variety, edgecolor='black', hatch="/")

axs[1].set_title('Monthly Lettuce Sales in 2023', fontsize=18, weight='bold', style='italic')
axs[1].set_xlabel('Month', fontsize=14)
axs[1].set_ylabel('Sales (Thousands of Heads)', fontsize=14)
axs[1].legend(title='Variety', loc='lower left', fontsize=10)
axs[1].grid(True, which='both', linestyle='-.', linewidth=0.75, color='gray')

plt.tight_layout()
plt.show()