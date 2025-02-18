import matplotlib.pyplot as plt
import numpy as np

weeks = ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4']
soft_drinks = ['Cola', 'L-Lime', 'G-Ale', 'R-Beer', 'O-Soda', 'G-Drink']

cola_sales = [150, 160, 170, 180]
lemon_lime_sales = [90, 100, 120, 130]
ginger_ale_sales = [70, 80, 95, 110]
root_beer_sales = [50, 55, 60, 65]
orange_soda_sales = [80, 85, 100, 105]
grape_drink_sales = [60, 70, 85, 95]

sales_data = [cola_sales, lemon_lime_sales, ginger_ale_sales, root_beer_sales, orange_soda_sales, grape_drink_sales]
new_colors = ['#3cb44b', '#f58231', '#4363d8', '#e6194b', '#911eb4', '#ffe119']

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.13
index = np.arange(len(weeks))

for i, (sales, color, drink) in enumerate(zip(sales_data, new_colors, soft_drinks)):
    ax.bar(index + i * bar_width, sales, width=bar_width, color=color, edgecolor='grey', label=drink, alpha=0.75, hatch='//')

ax.set_title('Soft Drink Sales', fontsize=16, pad=20)
ax.set_xlabel('Week', fontsize=12)
ax.set_ylabel('Liters', fontsize=12)
ax.set_xticks(index + bar_width * (len(soft_drinks) - 1) / 2)
ax.set_xticklabels(weeks)

ax.legend(loc='best', fontsize=10)
ax.yaxis.grid(True, linestyle='-.', linewidth=0.5)

plt.tight_layout()
plt.show()