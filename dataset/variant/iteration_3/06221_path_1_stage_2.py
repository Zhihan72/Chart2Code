import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Book genres
genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery"]

# Annual book sales data (in thousands)
sales_data = np.array([
    [150, 160, 170, 185, 200, 195, 210, 220, 230, 245, 260],  # Fiction
    [100, 115, 130, 140, 150, 165, 170, 180, 190, 200, 210],  # Non-Fiction
    [75, 80, 90, 95, 110, 120, 130, 140, 150, 160, 170],      # Science Fiction
    [50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150],      # Fantasy
    [40, 45, 50, 60, 70, 80, 90, 100, 110, 120, 130],        # Mystery
])

# Setup figure and axes
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15
x_indices = np.arange(len(years))

# Shuffle colors for each genre
colors = ['green', 'gold', 'orangered', 'dodgerblue', 'purple']

# Plot the data for each genre with shuffled colors
for idx, genre in enumerate(genres):
    ax.bar(x_indices + idx * bar_width, sales_data[idx], width=bar_width, color=colors[idx], alpha=0.85)

# Adjust x-axis ticks
ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(years, rotation=45)

# Add grid lines for y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adjust layout for the best fit
plt.tight_layout()

# Display the plot
plt.show()