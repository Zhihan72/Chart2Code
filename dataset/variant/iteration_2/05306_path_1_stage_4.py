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

# Apply a single color to both fruit_juice_sales and soda_sales
single_color = '#66b3ff'
ax1.bar(x - width/2, fruit_juice_sales, width, color=single_color)
ax1.bar(x + width/2, soda_sales, width, color=single_color)

ax1.set_xticks(x)
ax1.set_xticklabels([])  
ax1.grid(axis='y', linestyle='--', alpha=0.6)
ax1.legend().set_visible(False)  

plt.tight_layout()
plt.show()