import numpy as np
import matplotlib.pyplot as plt

# Define the data
months = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
]
countries = ['USA', 'Canada', 'Germany', 'Australia', 'India']
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
index = np.arange(len(months))

# Plot individual country sales data using a horizontal bar chart
colors = ['#FF6347', '#4682B4', '#32CD32', '#FFD700', '#800080']
for i, country in enumerate(countries):
    ax.barh(index + i * bar_height, sales_data[i], bar_height, label=country, color=colors[i], alpha=0.75)

# Plot average monthly sales as a line on each bar
for i, avg in enumerate(average_sales):
    ax.plot([avg]*len(index), index + 2*bar_height, color='black', linestyle='-', marker='o', linewidth=2, markersize=6, label='Average Sales' if i == 0 else "")

# Set Title and Labels
ax.set_title('Monthly Sales of Organic Fertilizers across Different Countries', fontsize=16, fontweight='bold', pad=20)
ax.set_ylabel('Months', fontsize=12)
ax.set_xlabel('Units Sold (in thousands)', fontsize=12)
ax.set_yticks(index + 2 * bar_height)
ax.set_yticklabels(months, rotation=0)
ax.legend(title='Countries', loc='upper right', fontsize=10)

# Make sure everything fits without overlap
plt.tight_layout()

# Display the plot
plt.show()