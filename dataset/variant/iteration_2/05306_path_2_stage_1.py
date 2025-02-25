import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
fruit_juice_sales = [1200, 1500, 1400, 1300]
soda_sales = [1800, 1600, 1700, 1500]
percentage_increase = [10, 12, 8, 15]

x = np.arange(len(regions))
width = 0.35

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

bars1 = ax1.bar(x - width/2, fruit_juice_sales, width, color='#ff9999')
bars2 = ax1.bar(x + width/2, soda_sales, width, color='#66b3ff')

ax1.set_title('Monthly Sales Performance of Beverages by Region in 2022', fontsize=16, fontweight='bold')
ax1.set_xlabel('Region', fontsize=13)
ax1.set_ylabel('Sales (in liters)', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(regions, fontsize=12)

def add_labels(ax, bars):
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2.0, yval + 30, int(yval), va='center', ha='center', fontsize=11, fontweight='bold', color='black')

add_labels(ax1, bars1)
add_labels(ax1, bars2)

bars3 = ax2.bar(x, percentage_increase, color='#ffcc99')

ax2.set_title('Percentage Increase in Total Beverage Sales by Region\n(compared to the previous year)', fontsize=16, fontweight='bold')
ax2.set_xlabel('Region', fontsize=13)
ax2.set_ylabel('Percentage Increase (%)', fontsize=13)
ax2.set_xticks(x)
ax2.set_xticklabels(regions, fontsize=12)

for bar in bars3:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2.0, yval + 1, f'{yval}%', va='center', ha='center', fontsize=11, fontweight='bold', color='black')

plt.tight_layout()
plt.show()