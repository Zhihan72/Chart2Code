import matplotlib.pyplot as plt
import numpy as np

# Backstory: Comparing the popularity of various genres of books over a decade.

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

# Define colors for each genre
colors = ['dodgerblue', 'orangered', 'green', 'purple', 'gold']

# Plot the data for each genre
for idx, genre in enumerate(genres):
    ax.bar(x_indices + idx * bar_width, sales_data[idx], width=bar_width, label=genre, color=colors[idx], alpha=0.85)

# Adding labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Book Sales (in thousands)', fontsize=12)
ax.set_title('Book Sales Performance by Genre (2010-2020)', fontsize=16, fontweight='bold')

# Adjust x-axis ticks and labels
ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(years, rotation=45)

# Add value labels on top of each bar
for i in range(len(years)):
    for j in range(len(genres)):
        ax.text(i + j * bar_width, sales_data[j][i] + 1, str(sales_data[j][i]), ha='center', va='bottom', fontsize=9)

# Add a legend to the plot
ax.legend(title='Book Genres', loc='upper left', fontsize=10)

# Add grid lines for y-axis
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Adding text annotations for key points
key_annotations = {
    2015: "Non-Fiction outperforms \nOther Genres",
    2020: "Fiction remains the \nLeading Genre",
}
for year in key_annotations:
    idx = np.where(years == year)[0][0]
    ax.annotate(key_annotations[year], xy=(year, 250), xytext=(year, 280),
                arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10, color='black', ha='center')

# Adjust layout for the best fit
plt.tight_layout()

# Display the plot
plt.show()