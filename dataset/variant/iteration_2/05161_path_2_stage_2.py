import matplotlib.pyplot as plt
import numpy as np

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
soft_drinks = ['Cola', 'Lemon-Lime', 'Ginger Ale', 'Root Beer', 'Orange Soda', 'Grape Drink']

cola_sales = [150, 160, 170, 180]
lemon_lime_sales = [90, 100, 120, 130]
ginger_ale_sales = [70, 80, 95, 110]
root_beer_sales = [50, 55, 60, 65]
orange_soda_sales = [80, 85, 100, 105]
grape_drink_sales = [60, 70, 85, 95]

sales_data = [cola_sales, lemon_lime_sales, ginger_ale_sales, root_beer_sales, orange_soda_sales, grape_drink_sales]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

fig, ax = plt.subplots(figsize=(14, 8))  # Adjusted figure size for better fit

bar_width = 0.13
index = np.arange(len(weeks))

for i, (sales, color, drink) in enumerate(zip(sales_data, colors, soft_drinks)):
    ax.bar(index + i * bar_width, sales, width=bar_width, color=color, edgecolor='black', label=drink, alpha=0.85)

ax.set_title('Weekly Soft Drink Sales Analysis', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Week', fontsize=12, fontweight='bold')
ax.set_ylabel('Liters Sold', fontsize=12, fontweight='bold')
ax.set_xticks(index + bar_width * (len(soft_drinks) - 1) / 2)
ax.set_xticklabels(weeks)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Soft Drink Type')
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()