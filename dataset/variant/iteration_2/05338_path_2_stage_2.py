import matplotlib.pyplot as plt
import numpy as np

# Categories and years
years = ['2016', '2017', '2018', '2019', '2020']
categories = ['Action Figures', 'Board Games', 'Dolls', 'Educational', 'Outdoor', 'Puzzles']

# Altered sales data
action_figures = [52, 56, 63, 66, 73]
board_games = [39, 41, 46, 48, 54]
dolls = [72, 77, 78, 88, 87]
educational = [29, 36, 41, 44, 47]
outdoor = [21, 24, 31, 34, 39]
puzzles = [9, 11, 15, 17, 19]

# Stack data for plotting
sales_data = np.array([action_figures, board_games, dolls, educational, outdoor, puzzles])

# Define colors for each toy category
colors = ['#FF8C00', '#1E90FF', '#FF1493', '#32CD32', '#8A2BE2', '#FFD700']

# Plotting setup
fig, ax = plt.subplots(figsize=(12, 8))

# Create a stacked bar chart for each year
width = 0.6
for i in range(len(sales_data)):
    ax.bar(years, sales_data[i], width, bottom=np.sum(sales_data[:i], axis=0), color=colors[i], edgecolor='grey')

plt.tight_layout()
plt.show()