import matplotlib.pyplot as plt
import numpy as np

years = ['2016', '2017', '2018', '2019', '2020']
categories = ['Action Figures', 'Board Games', 'Dolls', 'Educational', 'Outdoor', 'Puzzles']

# Sales data
action_figures = [52, 56, 63, 66, 73]
board_games = [39, 41, 46, 48, 54]
dolls = [72, 77, 78, 88, 87]
educational = [29, 36, 41, 44, 47]
outdoor = [21, 24, 31, 34, 39]
puzzles = [9, 11, 15, 17, 19]

sales_data = [action_figures, board_games, dolls, educational, outdoor, puzzles]

colors = ['#FF8C00', '#1E90FF', '#FF1493', '#32CD32', '#8A2BE2', '#FFD700']

fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.1

x = np.arange(len(years))
for i, (category, color) in enumerate(zip(sales_data, colors)):
    ax.bar(x + i * bar_width, category, bar_width, color=color, edgecolor='grey')

ax.set_xticks(x + bar_width * (len(categories) - 1) / 2)
ax.set_xticklabels(years)
plt.tight_layout()
plt.show()