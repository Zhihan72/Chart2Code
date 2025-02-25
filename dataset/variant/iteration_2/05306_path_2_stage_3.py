import matplotlib.pyplot as plt
import numpy as np

# Original sales data
regions = ['North', 'South', 'East', 'West']
fruit_juice_sales = [1200, 1500, 1400, 1300]
soda_sales = [1800, 1600, 1700, 1500]

# Sort data by fruit juice sales
sorted_indices = np.argsort(fruit_juice_sales)
regions_sorted = [regions[i] for i in sorted_indices]
fruit_juice_sorted = [fruit_juice_sales[i] for i in sorted_indices]
soda_sorted = [soda_sales[i] for i in sorted_indices]

x = np.arange(len(regions))
width = 0.35

fig, ax1 = plt.subplots(figsize=(9, 8))

# Plot the sorted data
bars1 = ax1.bar(x - width/2, fruit_juice_sorted, width, color='#ff9999')
bars2 = ax1.bar(x + width/2, soda_sorted, width, color='#66b3ff')

ax1.set_title('Monthly Sales Performance of Beverages by Region in 2022', fontsize=16, fontweight='bold')
ax1.set_xlabel('Region', fontsize=13)
ax1.set_ylabel('Sales (in liters)', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(regions_sorted, fontsize=12)

def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 30, int(yval), va='center', ha='center', fontsize=11, fontweight='bold', color='black')

add_labels(ax1, bars1)
add_labels(ax1, bars2)

plt.tight_layout()
plt.show()