import matplotlib.pyplot as plt
import numpy as np

regions = ["Nord", "Sur", "Este", "Oeste"]
categories = ["Tech Gadgets", "Clothing", "Literature", "Games", "Food"]

sales_data = np.array([
    [120, 140, 90, 60, 150],
    [180, 160, 80, 110, 130],
    [90, 130, 100, 90, 120],
    [150, 110, 95, 100, 140],
])

months = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
product_trends = {
    "Tech Gadgets": [12, 15, 14, 16, 14, 20, 18, 17, 16, 19, 21, 22],
    "Clothing": [8, 9, 10, 12, 13, 15, 18, 17, 16, 14, 10, 9],
    "Literature": [4, 5, 5, 5, 6, 7, 6, 7, 6, 7, 8, 9],
    "Games": [3, 4, 5, 6, 7, 6, 8, 9, 7, 8, 9, 10],
    "Food": [20, 22, 25, 23, 25, 24, 26, 27, 28, 26, 25, 24],
}

trend_data = np.array([product_trends[category] for category in categories])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
mask = np.triu(np.ones_like(sales_data, dtype=bool))

cax = ax1.matshow(np.where(mask, np.nan, sales_data), cmap='plasma', aspect='auto')
ax1.set_xticks(np.arange(len(categories)))
ax1.set_yticks(np.arange(len(regions)))
ax1.set_xticklabels(categories, rotation=45, ha='left')
ax1.set_yticklabels(regions)

ax1.set_title('Avg. Monthly Sales by Locale and Type', pad=15)

for i in range(sales_data.shape[0]):
    for j in range(sales_data.shape[1]):
        if not mask[i, j]:
            ax1.text(j, i, f"{sales_data[i, j]:.0f}", ha='center', va='center', 
                     color='white' if sales_data[i, j] > 100 else 'black')

colors = ['#FF5733', '#C70039', '#581845', '#FFC300', '#DAF7A6']
for idx, (trend, color) in enumerate(zip(trend_data, colors)):
    ax2.plot(months, trend, color=color)

ax2.set_title('Prod. Sales Trends Monthly', pad=15)
ax2.set_xlabel('Months')
ax2.set_ylabel('Avg. Sales')

plt.tight_layout()
plt.show()