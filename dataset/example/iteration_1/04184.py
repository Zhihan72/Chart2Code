import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are analyzing the market share of different types of beverages over the year 2022
# We will plot a bar chart showing the monthly sales for three different beverage categories:
# Coffee, Tea, and Juice. Additionally, we will include a subplot showing the cumulative market share
# for the entire year for each beverage category.

# Monthly sales data in thousands of units for each beverage category
months = np.arange(1, 13)
coffee_sales = np.array([10, 12, 15, 18, 20, 22, 25, 27, 30, 33, 35, 40])
tea_sales = np.array([8, 9, 11, 13, 15, 16, 17, 19, 21, 23, 24, 26])
juice_sales = np.array([5, 6, 7, 8, 10, 11, 13, 14, 16, 18, 20, 22])

# Calculate cumulative sales over the year for the second subplot
cumulative_sales = np.array([sum(coffee_sales), sum(tea_sales), sum(juice_sales)])
beverages = ['Coffee', 'Tea', 'Juice']
colors = ['#8B4513', '#006400', '#FFD700']

# Create a 1x2 subplot layout
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# First subplot: Bar chart for monthly sales
width = 0.25  # Width of the bars
ax1.bar(months - width, coffee_sales, width=width, color='#8B4513', label='Coffee')
ax1.bar(months, tea_sales, width=width, color='#006400', label='Tea')
ax1.bar(months + width, juice_sales, width=width, color='#FFD700', label='Juice')

ax1.set_title('Monthly Beverage Sales in 2022', fontsize=16, fontweight='bold')
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Sales (thousands of units)', fontsize=14)
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax1.legend(loc='upper left', fontsize=12, title='Beverage Types')
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# Annotate each bar with the sales value
for i in range(len(months)):
    ax1.text(months[i] - width, coffee_sales[i], str(coffee_sales[i]), ha='center', va='bottom', fontsize=10)
    ax1.text(months[i], tea_sales[i], str(tea_sales[i]), ha='center', va='bottom', fontsize=10)
    ax1.text(months[i] + width, juice_sales[i], str(juice_sales[i]), ha='center', va='bottom', fontsize=10)

# Second subplot: Pie chart for cumulative sales
ax2.pie(cumulative_sales, labels=beverages, colors=colors, autopct='%1.1f%%', startangle=140, explode=(0.1, 0, 0))
ax2.set_title('Cumulative Market Share in 2022', fontsize=16, fontweight='bold')

# Automatically adjust the layout
plt.tight_layout()

# Show the plot
plt.show()