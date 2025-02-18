import numpy as np
import matplotlib.pyplot as plt

# Define the data
sales_data = np.array([
    [120, 100, 110, 140, 150, 130, 145, 180, 160, 175, 190, 210],  # USA
    [90, 85, 100, 95, 105, 115, 120, 130, 140, 150, 160, 170],    # Canada
    [100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220],   # Germany
    [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170],     # Australia
    [80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]    # India
])

# Average monthly sales - across all countries
average_sales = sales_data.mean(axis=0)

# Create a figure with horizontal bar plot
fig, ax = plt.subplots(figsize=(14, 8))

bar_height = 0.15
index = np.arange(sales_data.shape[1])

# Plot individual country sales data using a horizontal bar chart
# Shuffled colors: original order [0: '#FF6347', 1: '#4682B4', 2: '#32CD32', 3: '#FFD700', 4: '#800080']
shuffled_colors = ['#FFD700', '#32CD32', '#800080', '#FF6347', '#4682B4']
for i in range(len(sales_data)):
    ax.barh(index + i * bar_height, sales_data[i], bar_height, color=shuffled_colors[i], alpha=0.75)

# Plot average monthly sales as a line on each bar
for avg in average_sales:
    ax.plot([avg]*len(index), index + 2*bar_height, color='black', linestyle='-', marker='o', linewidth=2, markersize=6)

# Remove textual elements
ax.set_yticks([])
ax.set_yticklabels([])
ax.set_title('')
ax.set_ylabel('')
ax.set_xlabel('')
ax.legend().remove()

plt.tight_layout()
plt.show()