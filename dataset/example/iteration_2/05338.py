import matplotlib.pyplot as plt
import numpy as np

# Define the backstory and title
# This chart represents the annual toy sales of different categories at a large department store over 5 years.
title = 'Annual Toy Sales in HappyMart Department Store\n(2016-2020)'

# Categories and years
years = ['2016', '2017', '2018', '2019', '2020']
categories = ['Action Figures', 'Board Games', 'Dolls', 'Educational', 'Outdoor', 'Puzzles']

# Sales data (in thousands of units for simplicity)
action_figures = [50, 55, 60, 65, 70]
board_games = [40, 42, 45, 50, 55]
dolls = [70, 75, 80, 85, 90]
educational = [30, 35, 40, 45, 50]
outdoor = [20, 25, 30, 35, 40]
puzzles = [10, 12, 14, 16, 18]

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

# Add labels, title and customize ticks
ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Years', fontsize=12)
ax.set_ylabel('Sales (in thousands of units)', fontsize=12)

# Add a legend
ax.legend(categories, loc='upper left', bbox_to_anchor=(1, 1), fontsize=10, title='Toy Categories')

# Annotate sales for each category in each year
for j, year in enumerate(years):
    for i, category in enumerate(categories):
        y_pos = sales_data[:, j].sum() - np.sum(sales_data[i+1:, j]) / 2
        if sale_value := sales_data[i, j]:  # sale_value for readability
            ax.text(j, y_pos, f'{sale_value}k',
                    ha='center', va='center', color='white', fontsize=10)

# Ensure layout is tight to prevent any overlap
plt.tight_layout()

# Show the plot
plt.show()