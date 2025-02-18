import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
products = ['Product A', 'Product B', 'Product C'] 

sales_data = {
    'North': {'Product A': [12, 15, 14, 18, 21, 25, 28, 30, 29, 27, 26, 24],
              'Product B': [8, 10, 11, 14, 15, 18, 20, 22, 23, 21, 19, 17],
              'Product C': [5, 7, 8, 10, 12, 14, 16, 18, 17, 15, 13, 12]},
    'South': {'Product A': [10, 12, 11, 13, 16, 20, 24, 25, 26, 24, 22, 21],
              'Product B': [7, 8, 9, 12, 13, 15, 17, 18, 17, 16, 15, 14],
              'Product C': [4, 5, 6, 8, 10, 12, 14, 15, 14, 13, 11, 10]},
    'East': {'Product A': [9, 10, 12, 15, 18, 22, 26, 28, 27, 26, 24, 23],
             'Product B': [6, 7, 8, 10, 11, 13, 15, 16, 15, 14, 12, 11],
             'Product C': [3, 4, 5, 7, 9, 12, 14, 16, 15, 13, 11, 9]},
    'West': {'Product A': [11, 13, 14, 17, 19, 23, 27, 29, 28, 27, 25, 23],
             'Product B': [7, 9, 10, 13, 14, 16, 18, 20, 19, 18, 16, 15],
             'Product C': [4, 6, 7, 9, 11, 13, 15, 17, 16, 15, 13, 11]}
}

fig, axs = plt.subplots(2, 2, figsize=(14, 10), sharex=True, sharey=True)

# New colors for the products
colors = ['#FF5733', '#33FF57', '#3357FF']

for idx, region in enumerate(regions):
    ax = axs[idx // 2][idx % 2]
    months = list(range(1, 13))
    for p_idx, product in enumerate(products):
        ax.plot(months, sales_data[region][product], label=product, marker='o', color=colors[p_idx])

    ax.set_title(f'{region} Region Sales', fontsize=12, fontweight='bold')
    ax.set_xlabel('Month', fontsize=10)
    ax.set_ylabel('Sales (in thousands)', fontsize=10)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()

fig.suptitle('Monthly Sales Performance of Products in Different Regions', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.show()