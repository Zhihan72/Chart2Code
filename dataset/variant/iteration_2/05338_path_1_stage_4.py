import matplotlib.pyplot as plt
import numpy as np

years = ['2016', '2017', '2018', '2019', '2020']
categories = ['Outdoor Fun', 'Playground Games', 'Learning Toys', 'Doll Collection']

outdoor = [20, 25, 30, 35, 40]
board_games = [40, 42, 45, 50, 55]
educational = [30, 35, 40, 45, 50]
dolls = [70, 75, 80, 85, 90]

sales_data = np.array([outdoor, board_games, educational, dolls])

colors = ['#32CD32', '#FF1493', '#8A2BE2', '#1E90FF']

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.6

for i in range(len(sales_data)):
    ax.bar(years, sales_data[i], width, bottom=np.sum(sales_data[:i], axis=0), color=colors[i])

ax.set_title('HappyMart Toy Yearly Sales Chart\n(2020-2016) Overview', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeframe of Sales', fontsize=12)
ax.set_ylabel('Units Sold (thousands)', fontsize=12)

for j, year in enumerate(years):
    for i in range(len(categories)):
        y_pos = sales_data[:, j].sum() - np.sum(sales_data[i+1:, j]) / 2
        if sale_value := sales_data[i, j]:
            ax.text(j, y_pos, f'{sale_value}k', ha='center', va='center', color='white', fontsize=10)

plt.tight_layout()
plt.show()