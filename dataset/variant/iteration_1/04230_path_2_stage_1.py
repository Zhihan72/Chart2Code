import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2021', '2020', '2022']  # Altered the order of years
fruits = ['Cherries', 'Bananas', 'Apples', 'Dates', 'Elderberries']  # Altered the order of fruits

sales_data = {
    'Cherries': [10, 12, 8, 14, 9],
    'Bananas': [15, 20, 13, 18, 22],
    'Apples': [25, 30, 22, 28, 35],
    'Dates': [5, 3, 4, 7, 6],
    'Elderberries': [8, 10, 9, 6, 11]
}

years_count = len(years)
fruit_count = len(fruits)
bar_width = 0.15
year_positions = np.arange(years_count)

fig, ax1 = plt.subplots(figsize=(14, 8))

bottoms = np.zeros(years_count)
bars = []
for fruit, sales in sales_data.items():
    bars.append(ax1.bar(year_positions, sales, bar_width, bottom=bottoms, label=fruit))
    bottoms += np.array(sales)

for bar in bars:
    for rect in bar:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., rect.get_y() + height/2, f'{int(height)}',
                 ha='center', va='bottom', fontsize=8, color='white')

total_sales = [sum(sales) for sales in zip(*sales_data.values())]
ax2 = ax1.twinx()
line = ax2.plot(years, total_sales, color='tab:orange', marker='o', label='Total Sales')

ax1.set_title("Intriguing Chart of Fruit Totals\nMarket Span Study 2018-2022", fontsize=16, weight='bold', pad=20)
ax1.set_xlabel("Year Timeline", fontsize=12)
ax1.set_ylabel("Tonnage of Sales", fontsize=12)
ax2.set_ylabel("Overall Sales in Tons", fontsize=12)
ax1.set_xticks(year_positions)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', title="Fruit Varieties")
ax2.legend(loc='upper right', title="Summed Output")

ax1.grid(True, axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()