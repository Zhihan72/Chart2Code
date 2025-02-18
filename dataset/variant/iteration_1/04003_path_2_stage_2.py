import matplotlib.pyplot as plt
import numpy as np

years = np.array(['2018', '2019', '2020', '2021', '2022'])
fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries"]

# Altered sales data to simulate randomness while maintaining the structure
apple_sales = np.array([275, 250, 320, 300, 310])
banana_sales = np.array([220, 240, 230, 180, 210])
orange_sales = np.array([210, 240, 200, 190, 220])
grape_sales = np.array([170, 180, 150, 160, 175])
strawberry_sales = np.array([130, 120, 115, 90, 110])

colors = ['#581845', '#DAF7A6', '#C70039', '#FFC300', '#FF5733']

sales_data = np.vstack([apple_sales, banana_sales, orange_sales, grape_sales, strawberry_sales])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.1
x = np.arange(len(years))

for i, fruit in enumerate(fruits):
    ax.bar(x + i*bar_width, sales_data[i], width=bar_width, label=fruit, color=colors[i])

ax.set_title("Annual Fruit Sales Analysis (2018-2022)\nAn insight into the sales trends of different fruits in the local market", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Sales (in tons)", fontsize=12)
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years, fontsize=12)
ax.legend(title='Fruits', fontsize=10, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(True, linestyle='--', alpha=0.7)

for i, fruit in enumerate(fruits):
    max_sales = sales_data[i].max()
    min_sales = sales_data[i].min()
    max_year = years[sales_data[i].argmax()]
    min_year = years[sales_data[i].argmin()]
    ax.annotate(f'Highest {fruit} Sales: {max_sales} tons', xy=(sales_data[i].argmax() + i*bar_width, max_sales), xytext=(sales_data[i].argmax() + i*bar_width, max_sales + 20),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', color='red')
    ax.annotate(f'Lowest {fruit} Sales: {min_sales} tons', xy=(sales_data[i].argmin() + i*bar_width, min_sales), xytext=(sales_data[i].argmin() + i*bar_width, min_sales - 30),
                arrowprops=dict(facecolor='black', shrink=0.05), fontsize=10, ha='center', color='green')

plt.tight_layout()
plt.show()