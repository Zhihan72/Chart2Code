import matplotlib.pyplot as plt
import numpy as np

years = ['2016', '2017', '2018', '2019', '2020']
categories = ['Outdoor Fun', 'Playground Games', 'Learning Toys', 'Doll Collection']

outdoor = np.array([20, 25, 30, 35, 40])
board_games = np.array([40, 42, 45, 50, 55])
educational = np.array([30, 35, 40, 45, 50])
dolls = np.array([70, 75, 80, 85, 90])

# Calculate differences from a central point, assuming equal divergence for demonstration
# Positive indicates above the mean, negative below
total_sales = outdoor + board_games + educational + dolls
average_sales = total_sales / 2

outdoor_div = outdoor - average_sales
board_games_div = board_games - average_sales
educational_div = educational - average_sales
dolls_div = dolls - average_sales

diverging_data = np.array([outdoor_div, board_games_div, educational_div, dolls_div])
colors = ['#32CD32', '#FF1493', '#8A2BE2', '#1E90FF']

fig, ax = plt.subplots(figsize=(12, 8))
width = 0.6

for i in range(len(diverging_data)):
    ax.bar(years, diverging_data[i], width, bottom=np.sum(diverging_data[:i], axis=0), color=colors[i], label=categories[i])

ax.axhline(0, color='black',linewidth=0.8)  # Central axis line
ax.set_title('HappyMart Diverging Sales Chart\n(2020-2016) Overview', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Timeframe of Sales', fontsize=12)
ax.set_ylabel('Deviation from Average Sales (thousands)', fontsize=12)

for j, year in enumerate(years):
    for i, category in enumerate(categories):
        y_pos = np.sum(diverging_data[:i+1, j]) - diverging_data[i, j] / 2
        if sale_value := diverging_data[i, j]:
            ax.text(j, y_pos, f'{int(sale_value)}k', ha='center', va='center', color='black', fontsize=10)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()