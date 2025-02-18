import matplotlib.pyplot as plt
import numpy as np

# Backstory: Visualize the annual distribution of fruit sales from a farmer's market over a 5-year span
years = ['2018', '2019', '2020', '2021', '2022']
fruits = ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries']

# Data representing the annual sales (in tons) for each type of fruit
sales_data = {
    'Apples': [25, 30, 22, 28, 35],
    'Bananas': [15, 20, 13, 18, 22],
    'Cherries': [10, 12, 8, 14, 9],
    'Dates': [5, 3, 4, 7, 6],
    'Elderberries': [8, 10, 9, 6, 11]
}

# Calculate the positions
years_count = len(years)
fruit_count = len(fruits)
bar_width = 0.15
year_positions = np.arange(years_count)

# Setting up the subplots for stacked bar chart and line chart with the same x-axis
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting stacked bar chart of fruit sales
bottoms = np.zeros(years_count)
bars = []
for fruit, sales in sales_data.items():
    bars.append(ax1.bar(year_positions, sales, bar_width, bottom=bottoms, label=fruit))
    bottoms += np.array(sales)

# Adding text annotations for bars
for bar in bars:
    for rect in bar:
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., rect.get_y() + height/2, f'{int(height)}',
                 ha='center', va='bottom', fontsize=8, color='white')

# Line chart subplot for total annual sales
total_sales = [sum(sales) for sales in zip(*sales_data.values())]
ax2 = ax1.twinx()
line = ax2.plot(years, total_sales, color='tab:orange', marker='o', label='Total Sales')

# Customizing the plot
ax1.set_title("Annual Distribution of Fruit Sales\nFarmer's Market Overview 2018-2022", fontsize=16, weight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Sales (in tons)", fontsize=12)
ax2.set_ylabel("Total Sales (in tons)", fontsize=12)
ax1.set_xticks(year_positions)
ax1.set_xticklabels(years)
ax1.legend(loc='upper left', title="Fruits")
ax2.legend(loc='upper right', title="Total Sales")

# Adding a grid for better readability
ax1.grid(True, axis='y', linestyle='--', alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()