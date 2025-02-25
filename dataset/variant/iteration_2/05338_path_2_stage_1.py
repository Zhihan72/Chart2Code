import matplotlib.pyplot as plt
import numpy as np

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

# Ensure layout is tight to prevent any overlap
plt.tight_layout()

# Show the plot
plt.show()