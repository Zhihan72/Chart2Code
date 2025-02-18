import matplotlib.pyplot as plt
import numpy as np

# Project Backstory: Fruit Sales Over the Seasons
# The purpose of this chart is to visualize the fruit sales across different seasons in selected regions.
# There are two main parts: 
# 1. Bar chart showing sales volume of fruits in each season
# 2. Decorative pie chart showing the percentage distribution of each fruit from total sales

# Defined regions
regions = ['North', 'South', 'East', 'West']

# Seasons
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

# Sales volume data (in thousands of units), explicitly created for 3 fruits across 4 regions for each season
apple_sales = np.array([
    [10, 15, 20, 25],  # Winter
    [30, 35, 40, 45],  # Spring
    [40, 45, 50, 55],  # Summer
    [25, 30, 35, 40]   # Autumn
])

orange_sales = np.array([
    [20, 15, 10, 5],   # Winter
    [25, 30, 35, 40],  # Spring
    [35, 40, 45, 50],  # Summer
    [30, 35, 45, 40]   # Autumn
])

banana_sales = np.array([
    [15, 20, 25, 30],  # Winter
    [20, 25, 30, 35],  # Spring
    [30, 35, 45, 50],  # Summer
    [35, 40, 45, 50]   # Autumn
])

# Calculate total sales for pie chart
total_apple_sales = apple_sales.sum()
total_orange_sales = orange_sales.sum()
total_banana_sales = banana_sales.sum()

# Prepare pie chart data
labels = ['Apple', 'Orange', 'Banana']
sizes = [total_apple_sales, total_orange_sales, total_banana_sales]
colors = ['#ff9999','#66b3ff','#99ff99']
explode = (0.1, 0, 0)  # explode Apple slice for emphasis

# Create the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

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

# Plot pie chart
ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 10})
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax2.set_title('Total Sales Distribution by Fruit Type', fontsize=14, fontweight='bold', pad=20)

# Add an overall main title
fig.suptitle('Fruit Sales Analysis', fontsize=16, fontweight='bold', y=0.98)

# Adjust the layout to prevent overlapping
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Display the chart
plt.show()