import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
fruit_juice_sales = [1200, 1500, 1400, 1300]
soda_sales = [1800, 1600, 1700, 1500]

sorted_data = sorted(zip(fruit_juice_sales, soda_sales, regions), reverse=True)
fruit_juice_sales, soda_sales, regions = zip(*sorted_data)

x = np.arange(len(regions))
width = 0.35

fig, ax1 = plt.subplots(figsize=(9, 8))

# Different colors for fruit_juice_sales and soda_sales
fruit_juice_color = '#FF9999'
soda_color = '#66b3ff'
ax1.bar(x - width/2, fruit_juice_sales, width, color=fruit_juice_color, label='Fruit Juice Sales', hatch='/')
ax1.bar(x + width/2, soda_sales, width, color=soda_color, label='Soda Sales', linestyle='-', edgecolor='black')

ax1.set_xticks(x)
ax1.set_xticklabels(regions)
ax1.grid(axis='y', linestyle='-.', alpha=0.6)
ax1.legend(loc='upper left', frameon=False)

ax1.spines['top'].set_visible(False)  # Remove top border
ax1.spines['right'].set_visible(False)  # Remove right border

plt.tight_layout()
plt.show()