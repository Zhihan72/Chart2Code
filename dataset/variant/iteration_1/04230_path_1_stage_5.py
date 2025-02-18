import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2018', '2021', '2019', '2022']
fruits = ['Grapes', 'Elderberries', 'Bananas', 'Dates', 'Figs', 'Apples', 'Cherries']

sales_data = {
    'Grapes': [7, 8.5, 9, 6.5, 9.5],
    'Cherries': [-5, -6, -4, -7, -4.5],
    'Apples': [12.5, 15, 11, 14, 17.5],
    'Figs': [1, 2, 1.5, 0.5, 3],
    'Bananas': [7.5, 10, 6.5, 9, 11],
    'Dates': [-2.5, -1.5, -2, -3.5, -3],
    'Elderberries': [-4, -5, -4.5, -3, -5.5]
}

years_count = len(years)
bar_width = 0.5
year_positions = np.arange(years_count)

fig, ax = plt.subplots(figsize=(16, 10))

bottoms = np.zeros(years_count)
styles = ['x', 'D', 's', 'o', '*', '|', '\\']
colors = ['blue', 'orange', 'green', 'purple', 'red', 'pink', 'brown']
line_styles = ['-', '--', '-.', ':', '-', '--', ':']

for i, (fruit, sales) in enumerate(reversed(sales_data.items())):
    ax.bar(year_positions, sales, bar_width, bottom=bottoms, 
           label=fruit, color=colors[i], linestyle=line_styles[i], hatch=styles[i])

for fruit, sales in sales_data.items():
    for i, sale in enumerate(sales):
        ax.text(year_positions[i], sale + (4 if sale < 0 else -4), 
                f'{abs(sale)}', ha='center', va='center', fontsize=8, color='white')

ax.set_title("Colorful Fruit Trends\nMarket Analysis 2020-2022", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Time Period", fontsize=12)
ax.set_ylabel("Fruit Sales (tons)", fontsize=12)
ax.set_xticks(year_positions)
ax.set_xticklabels(years)
ax.axhline(0, color='black', linewidth=0.8)
ax.legend(loc='best', title="Different Fruits", fontsize=10, title_fontsize='13')

ax.grid(False)

plt.tight_layout()
plt.show()