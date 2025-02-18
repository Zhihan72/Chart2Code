import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'East', 'West']
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

# Sales volume data
apple_sales = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [40, 45, 50, 55],
    [25, 30, 35, 40]
])
orange_sales = np.array([
    [20, 15, 10, 5],
    [25, 30, 35, 40],
    [35, 40, 45, 50],
    [30, 35, 45, 40]
])
banana_sales = np.array([
    [15, 20, 25, 30],
    [20, 25, 30, 35],
    [30, 35, 45, 50],
    [35, 40, 45, 50]
])

# Total sales for pie chart
total_apple_sales = apple_sales.sum()
total_orange_sales = orange_sales.sum()
total_banana_sales = banana_sales.sum()
labels = ['Apple', 'Orange', 'Banana']
sizes = [total_apple_sales, total_orange_sales, total_banana_sales]
colors = ['#ff9999', '#66b3ff', '#99ff99']
explode = (0.1, 0, 0)  # explode Apple slice for emphasis

# Create figure and subplots
fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8))

# Plot pie chart
ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 10})
ax2.axis('equal')
ax2.set_title('Total Sales Distribution by Fruit Type', fontsize=14, fontweight='bold', pad=20)

# Plot sales volume bar chart
x = np.arange(len(regions))
bar_width = 0.25

ax1.bar(x - bar_width, apple_sales.sum(axis=0), bar_width, label='Apple', color='#ff9999')
ax1.bar(x, orange_sales.sum(axis=0), bar_width, label='Orange', color='#66b3ff')
ax1.bar(x + bar_width, banana_sales.sum(axis=0), bar_width, label='Banana', color='#99ff99')

ax1.set_title('Seasonal Fruit Sales Across Regions', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Sales Volume (thousands)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(regions, fontsize=10)
ax1.legend(title='Fruit Type', loc='upper right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Add a main title
fig.suptitle('Fruit Sales Analysis', fontsize=16, fontweight='bold', y=0.98)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the chart
plt.show()