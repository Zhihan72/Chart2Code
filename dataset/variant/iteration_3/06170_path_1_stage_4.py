import matplotlib.pyplot as plt
import numpy as np

regions = ['Nroth', 'South', 'Esat', 'West', 'Central']
products = ['Pro duct A', 'Product B', 'Pruduct C', 'Product D']

sales_data = {
    'Nroth': {'Pro duct A': [12, 15, 14, 18, 21, 25, 28, 30, 29, 27, 26, 24],
              'Product B': [8, 10, 11, 14, 15, 18, 20, 22, 23, 21, 19, 17],
              'Pruduct C': [5, 7, 8, 10, 12, 14, 16, 18, 17, 15, 13, 12],
              'Product D': [10, 12, 13, 15, 17, 20, 22, 23, 22, 21, 20, 19]},
    'South': {'Pro duct A': [10, 12, 11, 13, 16, 20, 24, 25, 26, 24, 22, 21],
              'Product B': [7, 8, 9, 12, 13, 15, 17, 18, 17, 16, 15, 14],
              'Pruduct C': [4, 5, 6, 8, 10, 12, 14, 15, 14, 13, 11, 10],
              'Product D': [8, 9, 10, 11, 13, 15, 17, 18, 17, 16, 15, 14]},
    'Esat': {'Pro duct A': [9, 10, 12, 15, 18, 22, 26, 28, 27, 26, 24, 23],
             'Product B': [6, 7, 8, 10, 11, 13, 15, 16, 15, 14, 12, 11],
             'Pruduct C': [3, 4, 5, 7, 9, 12, 14, 16, 15, 13, 11, 9],
             'Product D': [7, 8, 9, 11, 13, 15, 17, 18, 17, 14, 12, 10]},
    'West': {'Pro duct A': [11, 13, 14, 17, 19, 23, 27, 29, 28, 27, 25, 23],
             'Product B': [7, 9, 10, 13, 14, 16, 18, 20, 19, 18, 16, 15],
             'Pruduct C': [4, 6, 7, 9, 11, 13, 15, 17, 16, 15, 13, 11],
             'Product D': [9, 10, 11, 13, 15, 17, 19, 18, 17, 16, 15, 12]},
    'Central': {'Pro duct A': [13, 14, 16, 19, 21, 24, 27, 29, 28, 27, 25, 22],
                'Product B': [8, 9, 10, 12, 14, 16, 18, 19, 18, 17, 16, 15],
                'Pruduct C': [5, 6, 8, 10, 12, 15, 17, 19, 18, 17, 15, 14],
                'Product D': [11, 12, 13, 15, 17, 19, 21, 23, 22, 20, 19, 18]}
}

fig, axs = plt.subplots(3, 2, figsize=(14, 15), sharex=True, sharey=True)

subplot_order = [2, 3, 0, 1, 4]

for new_idx, region_idx in enumerate(subplot_order):
    ax = axs[new_idx // 2][new_idx % 2]
    months = list(range(1, 13))
    region = regions[region_idx]
    for product in products:
        ax.plot(months, sales_data[region][product], label=product, marker='^' if product == 'Pro duct A' else '+', linestyle='-' if product == 'Pruduct C' else '--')

    ax.set_title(f'{region} Region Sales', fontsize=12, fontweight='bold')
    ax.set_xlabel('Month', fontsize=10)
    ax.set_ylabel('Sales (in thousands)', fontsize=10)
    ax.grid(False)
    ax.legend(loc='upper right')

fig.suptitle('Monthly Sales Performance of Products in Different Regions', fontsize=16, fontweight='bold', y=1.02)

plt.tight_layout()

plt.show()