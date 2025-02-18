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

average_sales = sales_data.mean(axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
index = np.arange(len(months))

# Adjusting stylistic elements
colors = ['#FFD700', '#FF6347', '#800080', '#4682B4', '#32CD32']
hatches = ['/', '\\', '-', '|', '+']

# Change marker styles and line styles
line_styles = [':', '--', '-.', '-', ':']
markers = ['s', 'D', '>', '^', 'P']

# Plot individual country sales data
for i, country in enumerate(countries):
    ax.bar(index + i * bar_width, sales_data[i], bar_width, label=country, color=colors[i], alpha=0.75, hatch=hatches[i])

# Plot average monthly sales as a line
ax.plot(index + 2 * bar_width, average_sales, color='black', linestyle=line_styles[0], marker=markers[0], linewidth=2, markersize=8, label='Average Sales')

ax.set_title('Monthly Sales of Organic Fertilizers across Different Countries', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Months', fontsize=12)
ax.set_ylabel('Units Sold (in thousands)', fontsize=12)
ax.set_xticks(index + 2 * bar_width)
ax.set_xticklabels(months, rotation=45)

# Randomly altering legend position
legend_positions = ['best', 'upper left', 'upper right', 'lower left', 'lower right']
ax.legend(title='Countries', loc=legend_positions[0], fontsize=10)

# Add grid
ax.yaxis.grid(True)
ax.xaxis.grid(True, linestyle=':', color='gray', alpha=0.7)

plt.tight_layout()
plt.show()