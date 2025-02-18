import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2021', '2020', '2022']
fruits = ['Cherries', 'Bananas', 'Apples', 'Dates', 'Elderberries']

sales_data = {
    'Cherries': [10, 12, 8, 14, 9],
    'Bananas': [15, 20, 13, 18, 22],
    'Apples': [25, 30, 22, 28, 35],
    'Dates': [5, 3, 4, 7, 6],
    'Elderberries': [8, 10, 9, 6, 11]
}

years_count = len(years)
bar_width = 0.15
year_positions = np.arange(years_count)

fig, ax1 = plt.subplots(figsize=(14, 8))

bottoms = np.zeros(years_count)
for fruit, sales in sales_data.items():
    ax1.bar(year_positions, sales, bar_width, bottom=bottoms)
    bottoms += np.array(sales)

total_sales = [sum(sales) for sales in zip(*sales_data.values())]
ax2 = ax1.twinx()
ax2.plot(years, total_sales, color='tab:orange', marker='o')

ax1.set_xticks(year_positions)
ax1.set_xticklabels(years)

plt.tight_layout()
plt.show()