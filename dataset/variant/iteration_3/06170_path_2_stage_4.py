import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West', 'Central']
products = ['Product A', 'Product B', 'Product C', 'Product D']

sales_data = {
    'North': {'Product A': [12, 15, 14, 18, 21, 25, 28, 30, 29, 27, 26, 24],
              'Product B': [8, 10, 11, 14, 15, 18, 20, 22, 23, 21, 19, 17],
              'Product C': [5, 7, 8, 10, 12, 14, 16, 18, 17, 15, 13, 12],
              'Product D': [3, 6, 8, 11, 13, 16, 19, 21, 20, 19, 17, 15]},
    'South': {'Product A': [10, 12, 11, 13, 16, 20, 24, 25, 26, 24, 22, 21],
              'Product B': [7, 8, 9, 12, 13, 15, 17, 18, 17, 16, 15, 14],
              'Product C': [4, 5, 6, 8, 10, 12, 14, 15, 14, 13, 11, 10],
              'Product D': [2, 5, 7, 9, 11, 14, 16, 18, 17, 16, 14, 13]},
    'East': {'Product A': [9, 10, 12, 15, 18, 22, 26, 28, 27, 26, 24, 23],
             'Product B': [6, 7, 8, 10, 11, 13, 15, 16, 15, 14, 12, 11],
             'Product C': [3, 4, 5, 7, 9, 12, 14, 16, 15, 13, 11, 9],
             'Product D': [1, 3, 5, 7, 10, 13, 15, 17, 16, 15, 13, 12]},
    'West': {'Product A': [11, 13, 14, 17, 19, 23, 27, 29, 28, 27, 25, 23],
             'Product B': [7, 9, 10, 13, 14, 16, 18, 20, 19, 18, 16, 15],
             'Product C': [4, 6, 7, 9, 11, 13, 15, 17, 16, 15, 13, 11],
             'Product D': [2, 4, 6, 8, 11, 14, 16, 18, 17, 15, 14, 13]},
    'Central': {'Product A': [13, 16, 15, 19, 22, 26, 29, 31, 30, 28, 27, 25],
                'Product B': [9, 11, 12, 15, 16, 19, 21, 23, 24, 22, 20, 18],
                'Product C': [6, 8, 9, 11, 13, 15, 17, 19, 18, 16, 14, 13],
                'Product D': [4, 7, 9, 12, 14, 17, 20, 22, 21, 20, 18, 16]}
}

fig, axs = plt.subplots(2, 3, figsize=(14, 10), sharex=True, sharey=True)

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33AB']

for idx, region in enumerate(regions):
    ax = axs[idx // 3][idx % 3]
    months = list(range(1, 13))
    for p_idx, product in enumerate(products):
        ax.plot(months, sales_data[region][product], marker='o', color=colors[p_idx])

    ax.grid(True, linestyle='--', alpha=0.6)

axs[1][2].axis('off')

plt.tight_layout()
plt.show()