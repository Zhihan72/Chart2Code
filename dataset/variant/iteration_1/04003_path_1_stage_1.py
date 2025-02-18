import matplotlib.pyplot as plt
import numpy as np

# Define years and fruits
years = np.array(['2018', '2019', '2020', '2021', '2022'])
fruits = ["Apples", "Bananas", "Oranges", "Grapes", "Strawberries"]

# Sales data for each fruit over the years (in tons)
apple_sales = np.array([250, 300, 275, 320, 310])
banana_sales = np.array([180, 220, 210, 230, 240])
orange_sales = np.array([200, 190, 210, 220, 240])
grape_sales = np.array([150, 160, 170, 175, 180])
strawberry_sales = np.array([90, 110, 115, 120, 130])

# Colors for each fruit
colors = ['#581845', '#DAF7A6', '#FFC300', '#FF5733', '#C70039']

# Stack the sales data for easy bar plotting
sales_data = np.vstack([apple_sales, banana_sales, orange_sales, grape_sales, strawberry_sales])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Define bar positions and width
bar_width = 0.1
x = np.arange(len(years))

# Plot each fruit's sales data as bar charts with an offset for each
for i, fruit in enumerate(fruits):
    ax.bar(x + i*bar_width, sales_data[i], width=bar_width, label=fruit, color=colors[i])

# Title and labels
ax.set_title("Annual Fruit Sales Analysis (2018-2022)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Sales (in tons)", fontsize=14)

# Customize x-axis with year labels
ax.set_xticks(x + bar_width * 2)
ax.set_xticklabels(years, fontsize=14)

# Add a legend
ax.legend(title='Fruits', fontsize=10, loc='upper right')

# Grid with different style and color
ax.grid(True, linestyle='-.', color='gray', alpha=0.5)

# Annotate highest and lowest sales for each fruit
for i, fruit in enumerate(fruits):
    max_sales = sales_data[i].max()
    min_sales = sales_data[i].min()
    ax.annotate(f'High: {max_sales}', xy=(sales_data[i].argmax() + i*bar_width, max_sales),
                xytext=(sales_data[i].argmax() + i*bar_width, max_sales + 10),
                arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10, color='blue')
    ax.annotate(f'Low: {min_sales}', xy=(sales_data[i].argmin() + i*bar_width, min_sales),
                xytext=(sales_data[i].argmin() + i*bar_width, min_sales - 20),
                arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=10, color='orange')

# Adjust the layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()